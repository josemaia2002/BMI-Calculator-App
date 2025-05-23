import streamlit as st

st.set_page_config(
    page_title="BMI calculator app",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "# This is a BMI calculator app developed by Jose Maia!"
    }
)  

def calculate_bmi(height, weight):
    bmi = weight/(height*height)
    return bmi

def display_bmi(bmi):
    st.write("BMI")
    st.write("Your BMI is ", bmi)
    

def main():
    st.header("BMI calculator App")
    height = st.number_input("Enter your height")
    weight = st.number_input("Enter your weight")
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight)
        display_bmi(bmi)

if __name__ == "__main__":
    main()