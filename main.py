import  streamlit as st

st.title("welcome to aktech")
st.header("latest iphones")
import streamlit as st

iphones = [
    {
        "model": "iPhone 13 Pro",
        "display": "6.1-inch Super Retina XDR display",
        "camera": "Triple 12MP camera system",
        "chip": "A15 Bionic chip",
        "price": "$999",
    },
    {
        "model": "iPhone 13",
        "display": "6.1-inch Super Retina XDR display",
        "camera": "Dual 12MP camera system",
        "chip": "A15 Bionic chip",
        "price": "$799",
    },
    {
        "model": "iPhone 13 mini",
        "display": "5.4-inch Super Retina XDR display",
        "camera": "Dual 12MP camera system",
        "chip": "A15 Bionic chip",
        "price": "$699",
    },
]


        st.write(f"Camera: {iphone['camera']}")
        st.write(f"Chip: {iphone['chip']}")
        st.write(f"Price: {iphone['price']}")  
st.title("New iPhones")

# Display a list of iPhone models
selected_model = st.selectbox("Select an iPhone model", [iphone['model'] for iphone in iphones])

# Display the specifications for the selected iPhone
for iphone in iphones:
    if iphone['model'] == selected_model:
        st.header(iphone['model'])
        st.write(f"Display: {iphone['display']}")

