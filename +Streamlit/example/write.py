
import streamlit as st
import pandas as pd
import numpy as np


# 출력
st.title('제목')
st.header('중제목')
st.subheader('소제목')
st.write('일반 글 1')
st.write('일반 글 2')

# 마크다운 문법도 인식이 된다.
st.write("# Header1")
st.write("## Header2")
st.write("### Header3")
st.write("**Bold**")

# 데이터를 넣어 줄 수 있다.
def get_data():
    df = pd.DataFrame({
        "A":np.arange(0, 10, 1),
        "B":np.arange(0, 1, 0.1)
    })
    return df

data = get_data()

st.write(data)
st.dataframe(data)
