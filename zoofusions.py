import streamlit as st
from PIL import Image

# Load the logo image
logo = Image.open('C:\\Marina Business\\zoo fusions\\Logo\ZooFusions_logo.png')

# Display logo and business title
st.image(logo, width=300)
st.title("ZooFusions")
st.subheader("Cat & Dog Products | Online Veterinary Consultations")

# Sidebar navigation
menu = ["Executive Summary", "Business Objectives", "Market Research", 
        "Business Model", "Services and Products", "Operations Plan", 
        "Marketing Plan", "Financial Plan", "Risk Analysis", "Pitch"]
choice = st.sidebar.selectbox("Menu", menu)

# Load content based on menu choice
if choice == "Executive Summary":
    st.header("Executive Summary")
    st.write("""
    ZooFusions is a dedicated platform for cat and dog owners in Canada. Our goal is to provide a 
    one-stop solution for online veterinary consultations, pet products, and grooming services.
    """)

# Load content based on menu choice
if choice == "Executive Summary":
    st.header("Executive Summary")
    st.write("""
    PetCare Online Canada aims to be the leading platform in Canada for pet owners
    seeking convenient veterinary consultations, grooming tutorials, and pet health tracking.
    """)

elif choice == "Business Objectives":
    st.header("Business Objectives")
    st.write("""
    - **Year 1**: Launch in major Canadian cities and reach 10,000 users.
    - **Year 2-3**: Expand nationwide and introduce premium services.
    - **Year 5**: Establish PetCare Online Canada as the go-to platform in the industry.
    """)

# Repeat for other sections

elif choice == "Pitch":
    st.header("Investor Pitch")
    st.write("""
    **PetCare Online Canada** is set to revolutionize pet care by offering online veterinary services, 
    grooming tutorials, and an e-commerce platform. With the growing pet care market, this platform 
    is positioned for rapid growth, targeting tech-savvy pet owners in urban and underserved regions.
    """)
    if st.button("Download Pitch"):
        # Logic to generate and download the pitch as PDF
        st.write("Download initiated...")
