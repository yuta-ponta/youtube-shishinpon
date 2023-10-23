# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('streamlit 超入門') 


st.write ('プレグレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'interacion{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
    
'Done!!!!'
    
left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3')



#ィション：',condition

#'あなたの好きな数字は',option,'です。'
#if st.checkbox('show Image'):
 #   img = Image.open('main.png')
  #  st.image(img,caption='shinya',use_column_width=True)



