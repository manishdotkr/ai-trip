import streamlit as st
from utils import *

st.set_page_config(page_title="TRAVEL ITINERARY GUIDE APP")
st.title("AI Travel Itineary Guide System 🤖 📑")
st.subheader("Planing your vacations 📝")

place = st.text_input("Enter the place you wanted to visit")
start_date = st.date_input("Enter dates of your travel")
day_count = st.number_input("Enter number of days of your travel", min_value= 0)
submit_button = st.button("Get started")
 
if submit_button and day_count and place:
    with st.spinner("Geting best plan for your vacation..."):
        data = top5_results(place, day_count)
        titles, links, snippets = extractinfo(data)
        url_data = load(links)
        response = generate(url_data, start_date, day_count)
        st.write(response)
        # print(response)