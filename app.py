import streamlit as st

st.title("Mimi의 필라테스 스튜디오 🧘")
st.write("반갑습니다! 예약 시스템을 준비 중입니다.")

name = st.text_input("성함을 입력해주세요")
if st.button("예약하기"):
    st.success(f"{name}님, 예약 신청이 완료되었습니다!")
