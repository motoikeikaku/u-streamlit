from multiprocessing import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

larest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    larest_iteration.text(f'Interration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'


left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右だよ～ん')

expander1 = st.beta_expander('問合せ1')
expander1.write('問合せ1の回答')
expander2 = st.beta_expander('問合せ2')
expander2.write('問合せ2の回答')
expander3 = st.beta_expander('問合せ3')
expander3.write('問合せ3の回答')


text = st.text_input('あなたの趣味は？')
condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたの趣味:',text
'コンディション：',condition


#option = st.selectbox(
#    'あなたが好きな数字は？',
#    list(range(1,11))
#)
#'あなたの好きな数字は',option,'です。'

#if st.checkbox('Show Image'):
#    img = Image.open('sample.jpg')
#    st.image(img,caption='kitakamigawa',use_column_width=True)

#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)
#st.table(df.style.highlight_max(axis=0))

"""
df= pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
"""
#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#st.map(df)



