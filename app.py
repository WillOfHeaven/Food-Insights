import base64
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from PIL import Image
st.set_page_config(page_title='Food Insights', page_icon="🐔", layout="wide")
page_bg_m = """
<style>
[data-testid="stAppViewContainer"] {
background-size: cover;
ba
}
</style>
"""

st.sidebar.title(
    'All data is from the UN Food and Agriculture Organization (FAO)')
st.sidebar.markdown('''
                    [Link to the data](http://www.fao.org/faostat/en/#data)
                    [Link to the data dictionary](http://www.fao.org/faostat/en/#definitions)             
                    ''')
st.markdown(page_bg_m, unsafe_allow_html=True)
st.subheader("Waffle Hacks 2023 official Submission")
st.title('Unlocking the Power of Data: Food Insights - Illuminating Pathways to Food Security')
image = Image.open('img2.jpg')
st.image(image, caption='Let there be no hunger.')
st.subheader(
    "There are almost 59 % more people facing hunger in the world than the entire population of India.")
st.subheader("The world produces enough food to feed everyone. Yet, 690 million people still go to bed on an empty stomach each night. ")
st.subheader("Read the @FAO's interactive story to learn more: https://www.fao.org/interactive/state-of-food-security-nutrition/en/ #SOFI2022")
st.subheader("Why insights on Food Insecurity data is important ?")
st.write("✔️  Identifying Vulnerable Populations: Food security data helps pinpoint groups at risk and enables targeted assistance.")
st.write("✔️  Informing Policy Decisions: Data aids policymakers in understanding hunger levels, trends, and evaluating the impact of existing policies.")
st.write("✔️  Monitoring Progress: Data allows for tracking initiatives' effectiveness and making necessary adjustments.")
st.write("✔️  Resource Allocation: Data guides efficient distribution of resources to areas with high food insecurity.")
st.write("✔️  Early Warning Systems: Data analysis helps develop early warning systems for potential food crises, facilitating timely interventions.")
st.write("✔️  Sustainable Development: Data supports progress towards zero hunger goals, identifying root causes and informing holistic strategies.")
st.sidebar.subheader("Data for insights on Food Insecurity")
st.subheader(" How many people in the world are hungry?")
# Load_data
df = pd.read_csv('data2.csv')
df1 = pd.read_csv('data4.csv')
df5 = pd.read_csv('data5.csv')

# st.write(df1.shape)
# st.write(df1.describe())
# st.write(df1)
# st.write(df5.columns)
refined_df = df1[['Area', 'Value', 'Element', 'Year']]
# df5 = df5[['Area','Value','Element','Year']]
# st.write(refined_df)
# st.bar_chart()
# st.write(df5)
st.subheader(
    "Prevalence of severe food insecurity in the total population (percent) (3-year average)")
country = st.text_input('Country : ', 'Algeria')
query_string = f"Area == '{country}'"
# st.write(query_string)
# st.write(df5)
df2 = refined_df.query(query_string)
df5 = df5.query(query_string)
# mean_value = df5['Value'].mean()
# st.write(df5)
df5 = df5[['Value', 'Year']]
df5['Start'] = pd.to_datetime(df5['Year'].str.split('-').str[0]).dt.date
df5['End'] = pd.to_datetime(df5['Year'].str.split('-').str[1]).dt.date
# df5['Middle'] = pd.to_datetime(df5['Year'].str.split('-').str[1]).dt.year-1
# df5['Interval'] = pd.date_range(start={pd.to_datetime(df5['Year'].str.split('-').str[0]).dt.date}, end={pd.to_datetime(df5['Year'].str.split('-').str[1]).dt.date})
# df5['Interval1'] = pd.date_range(start= df5['Start'],end=df5['End'])
# df5['Interval1'] = df5.apply(lambda row: pd.date_range(start=row['Start'], end=row['End']), axis=1)
# df5['Width'] = df['End']-df5['Start']
# df5 = df5.sort_values('Middle')
# fig, ax = plt.subplots()

st.bar_chart(data=df5, y=['Start', 'End'], x='Value',
             width=0, height=0, use_container_width=True)
# st.subheader()
# st.write(df5.describe)
# df2 = df2[['Year','Value']]
# df2 = refined_df[{refined_df['Area']== 'India'}]
# st.write(df2.columns)
# st.write(df2)
st.write(df5)
# refined_df = df[['Domain','Area','Element','Item','Year','Unit','Value']]
# st.write(refined_df.shape)
# st.write(refined_df.head())
# st.write(df.describe())
# st.write(refined_df)
