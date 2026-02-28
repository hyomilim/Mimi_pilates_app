import streamlit as st
import datetime

# 1. 디자인 꾸미기 (대문 이미지와 제목)
st.set_page_config(page_title="Mimi Pilates", page_icon="🧘")

st.title("🧘 Mimi Pilates")
st.subheader("Movement is life. Life is movement.")

# (선택) 로고 이미지가 있다면 주소를 넣을 수 있어요. 일단 샘플 이미지를 띄워볼게요.
st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&q=80&w=500", caption="오늘도 건강한 하루 되세요!")

st.divider() # 구분선

# 2. 예약 기능 (이름, 날짜, 시간 선택)
col1, col2 = st.columns(2) # 화면을 반으로 나눕니다.

with col1:
    name = st.text_input("Name", placeholder="Type your full name")
    workout_type = st.selectbox("Session", ["Trial lesson", "Private lessons"])

with col2:
    # 오늘 날짜부터 선택 가능하게 설정
    date = st.date_input("Reservation Date", datetime.date.today())
    time = st.time_input("Reservation Time", datetime.time(9, 0)) # 기본값 오전 9시

# 3. 예약 버튼 로직
if st.button("🗓️ Apply Reservation", use_container_width=True):
    if name:
        st.balloons() # 축하 풍선 효과!
        st.success(f"### Booking Confirmed\n\n**{name}**, **{date} {time}**에 **{workout_type}** Your appointment has been received.")
        st.info("We will send you a confirmation text shortly after review.")
    else:
        st.warning("Please type your Full name.")
