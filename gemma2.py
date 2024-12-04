
#### 로컬에 저장한 젬마2 2B 모델을 사용한 챗봇


import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 페이지 설정
st.set_page_config(page_title="Gemma 챗봇", layout="wide")

@st.cache_resource
def load_model():
    model_path = r"C:\Users\admin\.cache\huggingface\hub\models--google--gemma-2-2b-it\snapshots\299a8560bedf22ed1c72a8a11e7dce4a7f9f51f8"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",
        torch_dtype=torch.float16
    )
    return tokenizer, model

# 모델과 토크나이저 로드
tokenizer, model = load_model()

# 제목
st.title("Gemma2 2B 챗봇")

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
if prompt := st.chat_input("메시지를 입력하세요"):
    # 사용자 메시지 표시
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 챗봇 응답 생성
    with st.chat_message("assistant"):
        with st.spinner("생각중..."):
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
            outputs = model.generate(
                **inputs,
                max_length=1024,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
