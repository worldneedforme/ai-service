# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI




chat_model = ChatOpenAI()

st.title('AI 기업 애널리스트')
content = st.text_input('알기 원하는 기업에 대해서 입력하세요 : ')

if st.button('RUN AI'):
    with st.spinner('작성중..'):
        result  = chat_model.predict(content + "에 대한 주요제품과 기업의 강점과 약점 100자 내외로 알려줘")
        st.write(result)









