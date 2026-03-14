import streamlit as st

st.title("Currency Converter App")

amount = st.number_input("Enter Amount")

conversion = st.selectbox(
    "Select Conversion",
    ("INR to USD", "USD to INR", "INR to EUR")
)

if st.button("Convert"):

    if conversion == "INR to USD":
        result = amount * 0.012

    elif conversion == "USD to INR":
        result = amount * 83

    elif conversion == "INR to EUR":
        result = amount * 0.011

    st.write("Converted Amount:", result)