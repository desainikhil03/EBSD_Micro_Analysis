import streamlit as st
from components.sidebar import create_sidebar
from pages.ebsd_deep_clean import render_ebsd_clean_page

def setup_page_config():
    st.set_page_config(
        page_title="EBSD Microstructure Analysis",
        page_icon="🔬",
        layout="wide"
    )

def main():
    setup_page_config()
    
    # Create sidebar and get selected option
    selected_page = create_sidebar()
    
    # Render appropriate page based on selection
    if selected_page == "EBSD Deep Clean":
        render_ebsd_clean_page()
    else:
        # Home page
        st.title("Welcome to EBSD Microstructure AI-based Analysis")
        st.write("""
        This platform provides advanced tools for analyzing EBSD microstructure data using 
        artificial intelligence techniques. Select an option from the sidebar to begin your analysis.
        """)
        
        st.markdown("""
        ### Available Tools:
        1. **EBSD Deep Clean** - Clean and process EBSD data files (.ang/.ctf)
        2. **Data Analysis** - (Coming Soon)
        3. **Pattern Recognition** - (Coming Soon)
        4. **Advanced Statistics** - (Coming Soon)
        """)

if __name__ == "__main__":
    main() 