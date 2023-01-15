import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
st.title('Supermarket Sales Data Analysis')

df = pd.read_csv('supermarket.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.text('')
st.header('Top ten selling stores:')

tptn = df.nlargest(10, 'store_sales')

st.bar_chart(data=tptn, x='store_id', y='store_sales')

st.text('')
st.header('Lowest selling stores:')

st.bar_chart(data=df.nsmallest(10, 'store_sales'), x='store_id', y='store_sales')
st.subheader('')
st.subheader('Average daily customer visits were :green[786.350446]')

avg = st.radio(
    "Select to view highest or lowest stores based on item availability.",
    ('Highest', 'Lowest'))

if avg == 'Highest':
    st.bar_chart(data=df.nlargest(10, 'items_available'), x='store_id', y='items_available')
elif avg == 'Lowest':
    st.bar_chart(data=df.nsmallest(10, 'items_available'), x='store_id', y='items_available')
else:
    st.write("You didn\'t select an option.")

# sta=sns.scatterplot(data=df, x='store_area', y='daily_customer_count')
# plt.show(sta)