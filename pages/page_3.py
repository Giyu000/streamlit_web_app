import streamlit as st
import pandas as pd

# データ分析関連
df = pd.read_csv('./data/list.csv', index_col='月')
st.line_chart(df)
st.bar_chart(df['2024'])
