import streamlit as st
import requests

# OpenWeatherMap API 설정
API_KEY = "16d5b28a66665229c4d27b8e410d62ad"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# 한글-영어 도시명 매핑
CITY_MAPPING = {
    "서울": "Seoul",
    "부산": "Busan",
    "인천": "Incheon",
    "대구": "Daegu",
    "대전": "Daejeon",
    "광주": "Gwangju",
    "울산": "Ulsan",
    "제주": "Jeju",
    "과천": "Gwacheon",
    # 필요한 도시를 추가할 수 있습니다
}

# 사용자 입력 받기
user_input = st.text_input("도시명을 입력하세요:", "")

if user_input:
    # 한글 도시명을 영어로 변환
    city_name = CITY_MAPPING.get(user_input, user_input)
    
    # API 요청 파라미터 설정
    params = {
        "q": city_name,  # 변환된 도시명 사용
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    
    try:
        # API 요청
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            # 날씨 정보 추출
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"] 
            weather_desc = data["weather"][0]["description"]
            
            # 결과 출력
            st.write(f"## {city_name}의 현재 날씨")
            st.write(f"🌡️ 기온: {temp:.1f}°C")
            st.write(f"💧 습도: {humidity}%")
            st.write(f"🌤️ 날씨: {weather_desc}")
        else:
            st.error("도시를 찾을 수 없습니다. 올바른 도시명을 입력해주세요.")
            
    except Exception as e:
        st.error("날씨 정보를 가져오는데 실패했습니다. 잠시 후 다시 시도해주세요.")
