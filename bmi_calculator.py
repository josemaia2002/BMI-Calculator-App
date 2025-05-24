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

def calculate_bmi(height, weight, unit):
    bmi = (weight/(height*height))

    if unit == "Imperial (lbs/in)":
        bmi *= 703
        
    return bmi

def display_bmi(bmi):
    st.subheader("Results")
    st.metric(label="Your BMI", value=f"{bmi:.2f}")
    
    # BMI classification
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    st.write(f"Category: {category}")
    # st.progress(min(bmi/40, 1.0))

def main():
    st.header("BMI calculator App")

    # Unit selector
    unit = st.radio("Select measurement system", ["Metric (kg/m)", "Imperial (lbs/in)"])

    if unit == "Imperial (lbs/in)":
        height = st.number_input("Enter your height (in inches)", min_value=20, max_value=100, value=67)
        weight = st.number_input("Enter your weight (in pounds)", min_value=50, max_value=700, value=154)
    else:
        height = st.number_input("Enter your height (in meters)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
        weight = st.number_input("Enter your weight (in kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.1)
    
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(height, weight, unit)
        display_bmi(bmi)

if __name__ == "__main__":
    main()