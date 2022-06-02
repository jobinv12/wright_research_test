from decimal import DivisionByZero
import streamlit as st
import json
import requests

st.header("Wright Research Assignment")

symbol = st.text_input("Enter a Stock Name")

try:
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"symbol":symbol,"region":"US"}

    headers = {
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
        "X-RapidAPI-Key": "a3574400c7msh4b85b54650440f4p160771jsn8c983708a9cb"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    last_traded_price = response["prices"][0]["close"] 
    open_high = response["prices"][0]["open"]
    low_close = response["prices"][0]["close"]

    #todays price  - yesterdays price
    price_change_today = response["prices"][0]["close"] - response["prices"][1]["open"] 

    price = response["prices"][0]["close"]
    two_weeks_price = response["prices"][9]["close"]
    total = price - two_weeks_price
    percentage_price_change_2weeks = (total/two_weeks_price)*100

    st.write("Last Traded price: ","{:.2f}".format(last_traded_price))
    st.write("Open High: ", "{:.2f}".format(open_high))
    st.write("Low Close: ", "{:.2f}".format(low_close))
    st.write("Price Change Today: ", "{:.2f}".format(price_change_today))
    st.write("% Price Change in 2 weeks: ", "{:.2f}".format(percentage_price_change_2weeks))

except IndexError:
    st.info("Enter correct symbol.")

except requests.JSONDecodeError:
    st.info("Enter a symbol in search box.")
