import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 페이지 설정
st.set_page_config(page_title="AI 챗봇", layout="wide")

@st.cache_resource
def load_model():
    with st.spinner('모델을 로딩중입니다...'):
        tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
        model = AutoModelForCausalLM.from_pretrained(
            "distilgpt2",
            device_map="auto",
            torch_dtype=torch.float16
        )
        st.success('모델 로딩 완료!')
        return tokenizer, model

# 시작 메시지
st.title("AI 챗봇")

# 모델과 토크나이저 로드
tokenizer, model = load_model()

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
        with st.spinner('답변을 생성중입니다...'):
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_length=100,  # 짧은 응답 생성
                    temperature=0.7,
                    top_p=0.9,
                    pad_token_id=tokenizer.eos_token_id,
                    num_return_sequences=1
                )
            
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            # 입력 프롬프트 제거
            response = response[len(prompt):].strip()
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
