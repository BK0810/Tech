import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 페이지 설정
st.set_page_config(page_title="AI 챗봇", layout="wide")

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
    model = AutoModelForCausalLM.from_pretrained(
        "facebook/opt-350m", 
        device_map="auto",
        torch_dtype=torch.float16
    )
    return tokenizer, model

# 모델과 토크나이저 로드
tokenizer, model = load_model()

# 제목 설정
st.title("AI 챗봇")

# 세션 스테이트 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 내용 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요"):
    # 사용자 메시지 표시
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 챗봇 응답 생성
    with st.chat_message("assistant"):
        chat_input = tokenizer(prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **chat_input,
                max_length=1024,
                temperature=0.7,
                top_p=0.9,
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
