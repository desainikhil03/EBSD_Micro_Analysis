import streamlit as st

def create_sidebar():
    with st.sidebar:
        st.title("Navigation")
        
        # Create navigation options
        selected = st.radio(
            "Select Analysis Tool",
            options=[
                "Home",
                "EBSD Deep Clean",
                "Data Analysis (Coming Soon)",
                "Pattern Recognition (Coming Soon)",
                "Advanced Statistics (Coming Soon)"
            ]
        )
        
        return selected 