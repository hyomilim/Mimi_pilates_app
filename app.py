import streamlit as st
import datetime

# 1. 디자인 꾸미기 (대문 이미지와 제목)
st.set_page_config(page_title="Mimi Pilates", page_icon="🧘")

st.title("🧘 Mimi의 필라테스 스튜디오")
st.subheader("나를 위한 온전한 시간, 예약을 도와드릴게요.")

# (선택) 로고 이미지가 있다면 주소를 넣을 수 있어요. 일단 샘플 이미지를 띄워볼게요.
st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&q=80&w=500", caption="오늘도 건강한 하루 되세요!")

st.divider() # 구분선

# 2. 예약 기능 (이름, 날짜, 시간 선택)
col1, col2 = st.columns(2) # 화면을 반으로 나눕니다.

with col1:
    name = st.text_input("회원 성함", placeholder="성함을 입력하세요")
    workout_type = st.selectbox("운동 종류", ["개인 레슨", "그룹 필라테스", "듀엣 레슨"])

with col2:
    # 오늘 날짜부터 선택 가능하게 설정
    date = st.date_input("예약 날짜", datetime.date.today())
    time = st.time_input("예약 시간", datetime.time(10, 0)) # 기본값 오전 10시

# 3. 예약 버튼 로직
if st.button("🗓️ 예약 신청하기", use_container_width=True):
    if name:
        st.balloons() # 축하 풍선 효과!
        st.success(f"### 예약 완료!\n\n**{name}**님, **{date} {time}**에 **{workout_type}** 예약이 접수되었습니다.")
        st.info("관리자가 확인 후 확정 문자를 보내드립니다.")
    else:
        st.warning("성함을 입력해 주세요!")
