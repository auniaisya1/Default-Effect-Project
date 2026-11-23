
import streamlit as st
import random

st.set_page_config(
    page_title="Default Effect Research",
    page_icon="📋",
    layout="centered"
)

st.title("The Impact of the Default Effect on Human Choices")

st.write(
    "Welcome to our research questionnaire. "
    "This study aims to investigate how pre-selected "
    "options may influence human decision-making."
)

st.info(
    "Your participation is voluntary. "
    "Please answer all questions honestly."
)

st.divider()

# Assign experimental group
if "group" not in st.session_state:
    st.session_state.group = random.choice(["A", "B"])

group = st.session_state.group
default_option = "Yes" if group == "A" else "No"

# Section A
st.header("Section A: Demographic Information")

age = st.selectbox(
    "1. What is your age?",
    [
        "Select your age",
        "18–20 years old",
        "21–23 years old",
        "24–26 years old",
        "27–30 years old",
        "Above 30 years old"
    ]
)

gender = st.radio(
    "2. What is your gender?",
    ["Male", "Female", "Prefer not to say"]
)

st.divider()

# Section B
st.header("Section B: Decision-Making Scenarios")

st.write("Please choose the option that best represents your decision.")

st.subheader("3. Mobile Application Notifications")

st.write(
    "Imagine you have just installed a new mobile application. "
    "The application has automatically selected your notification preference."
)

st.caption(f"Pre-selected option: {default_option}")

notification = st.radio(
    "What would you choose?",
    ["Yes", "No"],
    index=0 if default_option == "Yes" else 1,
    horizontal=True
)

st.subheader("4. Online Shopping Newsletter")

newsletter = st.radio(
    "Would you like to subscribe to the website's newsletter?",
    ["Yes", "No"],
    horizontal=True
)

st.subheader("5. Digital Receipt")

receipt = st.radio(
    "Would you like to receive a digital receipt by email?",
    ["Yes", "No"],
    horizontal=True
)

st.subheader("6. Food Delivery Cutlery")

cutlery = st.radio(
    "Would you like to add cutlery to your food order?",
    ["Yes", "No"],
    horizontal=True
)

st.subheader("7. Gift Wrapping")

gift = st.radio(
    "Would you like to add gift-wrapping services to your purchase?",
    ["Yes", "No"],
    horizontal=True
)

st.divider()

# Section C
st.header("Section C: General Opinions and Awareness")

awareness = st.radio(
    "8. How often do you notice options that have already been selected for you?",
    ["Always", "Often", "Sometimes", "Rarely", "Never"]
)

influence = st.radio(
    "9. Do you think pre-selected options can influence your decisions?",
    ["Yes", "No", "Not sure"]
)

reason = st.radio(
    "10. What is the main reason you might keep an option already selected for you?",
    [
        "Convenience and saves time",
        "I do not notice the selected option",
        "I trust the platform's recommendation",
        "I do not have a strong preference",
        "Other reasons"
    ]
)

st.divider()

# Submit questionnaire
if st.button("Submit Questionnaire", type="primary"):

    if age == "Select your age":
        st.error("Please select your age before submitting.")

    else:
        response = {
            "Group": group,
            "Age": age,
            "Gender": gender,
            "Q3_Notifications": notification,
            "Q4_Newsletter": newsletter,
            "Q5_Receipt": receipt,
            "Q6_Cutlery": cutlery,
            "Q7_Gift_Wrapping": gift,
            "Q8_Awareness": awareness,
            "Q9_Influence": influence,
            "Q10_Reason": reason
        }

        st.success("Thank you! Your answers have been recorded.")
        st.write("Your response:")
        st.json(response)
