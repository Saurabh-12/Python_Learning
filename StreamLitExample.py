import streamlit as st
import numpy as np
import time

# streamlit.slider(label, min_value=None, max_value=None, value=None, step=None, format=None)
st.slider("Slider", min_value=0, max_value=100, value=5, step=5, format="horizental")

url = st.text_input('Enter URL')
st.write('The Entered URL is', url)

st.checkbox('Show dataframe')


# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 1 second, so the change is clearer.
time.sleep(4)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)

import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

'''
# Club and Nationality App
This very simple webapp allows you to select and visualize players from certain clubs and certain nationalities.
'''
df = st.cache(pd.read_csv)("football_data.csv")

clubs = st.sidebar.multiselect('Show Player for clubs?', df['Club'].unique())
nationalities = st.sidebar.multiselect('Show Player from Nationalities?', df['Nationality'].unique())

new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
st.write(new_df)

# Create distplot with custom bin_size
fig = px.scatter(new_df, x ='Overall',y='Age',color='Name')

'''
### Here is a simple chart between player age and overall
'''

st.plotly_chart(fig)