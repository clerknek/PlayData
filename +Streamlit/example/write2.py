
import streamlit as st
import pandas as pd
import numpy as np


col1, col2 = st.columns(2)
# 출력
col1.title('제목')
col1.header('중제목')
col1.subheader('소제목')
col1.write('일반 글 1')
col1.write('일반 글 2')

# 마크다운 문법도 인식이 된다.
col2.write("# Header1")
col2.write("## Header2")
col2.write("### Header3")
col2.write("**Bold**")

# 데이터를 넣어 줄 수 있다.
st.write('# 데이터')
def get_data():
    df = pd.DataFrame({
        "A":np.arange(0, 10, 1),
        "B":np.arange(0, 1, 0.1)
    })
    return df

data = get_data()

st.dataframe(data)
