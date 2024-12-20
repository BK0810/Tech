
#### git push ####
# git add <파일 이름>               # 스테이징 영역에 파일 추가
# git commit -m "작업 내용 설명"
# git push origin main             # git Repository로 push (로컬저장소의 변경내용을 원격저장소로 보냄)

# git reset <파일 이름>             # 스테이징 영역에서 파일 뺴기
# git status                       # git 현재상태 확인 
# git log                          # git 로그 확인


#### git pull ####
# git pull origin main             # git Repository로 pull (원격저장소의 변경내용을 로컬저장소로 가져옴)   


# github repository
# https://github.com/BK0810/streamlit_app


# 스트림릿(Streamlit) 30일 챌린지
# https://wikidocs.net/book/14530

# 스트림릿 커뮤니티 클라우드
# https://share.streamlit.io/
# https://bk0810.streamlit.app/


# 실행명령어: streamlit run streamlit_app.py
# 종료명령어: ctrl + c

# https://home.openweathermap.org/api_keys
# 16d5b28a66665229c4d27b8e410d62ad




# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np

# 앱 제목
st.title("Streamlit 체험 앱")

# 간단한 텍스트
st.write("Streamlit을 사용하여 대화형 웹 앱을 만들어 보세요!")


st.write("n8n")


if st.button("클릭하세요"):
    st.write("버튼이 눌렸습니다!")
#else:
#    st.write("버튼을 눌러주세요.")



# 텍스트 입력 필드 생성
user_input = st.text_input("도시명을 입력하세요", "서울")  # 기본값은 "서울"

# 입력한 값을 출력
st.write("입력한 도시:", user_input)


st.write("git push 테스트")


