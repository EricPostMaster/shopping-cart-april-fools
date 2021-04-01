# Streamlit
#!pip install streamlit
import streamlit as st
import streamlit.components.v1 as stc
import time

st.markdown(
    """<style>
        col1 {text-align: right !important}
    </style>
    """, unsafe_allow_html=True) 


st.title("Should you return your shopping cart?")
st.write("""Shopping cart, buggy, trolley, wagon... Each day, scores of hapless humans 
            grapple with the dilemma of whether they "should" return their shopping cart
            to a return corral. This app solves that problem with four quick questions!""")

# How many functional legs do you have?
legs = st.selectbox(
    "How many functional legs do you have?",
    ("2", "Fewer than 2")
)

# Did you walk into the store?
walk = st.selectbox(
    "Did you walk into the store?",
    ("Yes", "No")
)

# Is there a cart return within 100 feet?
cart = st.slider(
    "How many feet to the nearest cart return?",
    min_value=0,
    max_value=200,
    value=100
)

# Do you have kids with you?
kids = st.slider(
    "How many kids do you have with you?",
    min_value=0,
    max_value=50,
    value=0
)

with st.spinner("Using totally unbiased AI to see if you have a good excuse..."):
    time.sleep(2.5)

# Result column
col1, col2 = st.beta_columns([1,1.5])

with col1:
    st.markdown("<h2 style='text-align: right;'>Verdict:</h2>", unsafe_allow_html=True)

with col2:
    # If you have 2 functional legs, return your dang cart!
    if legs == "2":
        st.header("Return your cart!")
    else:
        st.header("Okay, you get a pass.")

st.write("")
col1, col2, col3 = st.beta_columns([1,6,1])

with col1:
    st.write("")
with col2:
    st.image("https://i.imgflip.com/amucx.jpg",
            caption="Happy April Fool's Day :) Put your cart away!")
with col3:
    st.write("")




# cart = st.selectbox(
#     "Is there a cart return within 100 feet?",
#     ("Yes", "No")
# )
# kids = st.selectbox(
#     "Do you have kids with you?",
#     ("Yes", "No")
# )
# my_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.005)
#     my_bar.progress(percent_complete + 1)