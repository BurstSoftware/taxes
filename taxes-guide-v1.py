import streamlit as st
import pandas as pd

# Streamlit app
st.title("Tax Filing Help")

# Filing methods
filing_methods = ["Tax Software", "Tax Professional", "IRS Free File"]
selected_filing_method = st.selectbox("Choose a filing method", filing_methods)

# Tax software section
if selected_filing_method == "Tax Software":
    st.header("Tax Software")
    st.write("Use tax software like TurboTax, H&R Block, or TaxAct to guide you through the filing process.")
    st.write("Which tax software do you want to use?")
    software_options = ["TurboTax", "H&R Block", "TaxAct"]
    selected_software = st.selectbox("Select a tax software", software_options)
    if selected_software == "TurboTax":
        st.write("You can use TurboTax to file your taxes online or through their mobile app.")
        st.write("TurboTax offers a free trial and then it costs $59.99 for federal returns and $39.99 for state returns.")
    elif selected_software == "H&R Block":
        st.write("You can use H&R Block to file your taxes online or through their mobile app.")
        st.write("H&R Block offers a free trial and then it costs $59.99 for federal returns and $39.99 for state returns.")
    elif selected_software == "TaxAct":
        st.write("You can use TaxAct to file your taxes online or through their mobile app.")
        st.write("TaxAct offers a free trial and then it costs $49.95 for federal returns and $29.95 for state returns.")

# Tax professional section
elif selected_filing_method == "Tax Professional":
    st.header("Tax Professional")
    st.write("Hire a certified tax professional to prepare and file your taxes.")
    st.write("What type of tax professional do you need?")
    professional_options = ["CPA", "EA", "Enrolled Agent"]
    selected_professional = st.selectbox("Select a tax professional", professional_options)
    if selected_professional == "CPA":
        st.write("A Certified Public Accountant (CPA) is a certified professional who has passed the Uniform CPA Examination.")
        st.write("They can help you with tax preparation, auditing, and consulting.")
    elif selected_professional == "EA":
        st.write("An Enrolled Agent (EA) is a certified professional who has passed the Special Enrollment Examination.")
        st.write("They can help you with tax preparation, auditing, and consulting.")
    elif selected_professional == "Enrolled Agent":
        st.write("An Enrolled Agent (EA) is a certified professional who has passed the Special Enrollment Examination.")
        st.write("They can help you with tax preparation, auditing, and consulting.")

# IRS Free File section
elif selected_filing_method == "IRS Free File":
    st.header("IRS Free File")
    st.write("If you earn $69,000 or less, you may be eligible for free tax filing through the IRS Free File program.")
    st.write("How do you qualify for IRS Free File?")
    qualification_options = ["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"]
    selected_qualification = st.selectbox("Select your filing status", qualification_options)
    if selected_qualification == "Single":
        st.write("If you are single and earn $69,000 or less, you may be eligible for IRS Free File.")
        st.write("You can file your taxes for free through the IRS Free File program.")
    elif selected_qualification == "Married Filing Jointly":
        st.write("If you are married filing jointly and earn $69,000 or less, you may be eligible for IRS Free File.")
        st.write("You can file your taxes for free through the IRS Free File program.")
    elif selected_qualification == "Married Filing Separately":
        st.write("If you are married filing separately and earn $69,000 or less, you may be eligible for IRS Free File.")
        st.write("You can file your taxes for free through the IRS Free File program.")
    elif selected_qualification == "Head of Household":
        st.write("If you are head of household and earn $69,000 or less, you may be eligible for IRS Free File.")
        st.write("You can file your taxes for free through the IRS Free File program.")

# Final section
st.header("Final Steps")
st.write("Once you have chosen your filing method, you can start preparing and filing your taxes.")
st.write("Remember to double-check your information and make sure you are eligible for any tax credits or deductions.")
st.write("If you have any questions or need help, you can contact a tax professional or the IRS directly.")
