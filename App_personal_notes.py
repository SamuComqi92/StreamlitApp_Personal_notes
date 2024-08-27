# --------------------------------------------------------------------------------------------------------------------------------------------
# Usefull libraries
import streamlit as st
from functions import footer
from streamlit_option_menu import option_menu
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px

# --------------------------------------------------------------------------------------------------------------------------------------------
# Usefull functions
def load_text(filename):
    with open(filename, 'r') as f:
        return f.read()
  
# --------------------------------------------------------------------------------------------------------------------------------------------
# Titles & Icons
Menu_icon = "menu-up"
Main_topics = ["Microsoft Fabric", 'Qlik (work in progress)']
Main_icons = ['clipboard-data', 'graph-up-arrow']
Section_Fabric = ["1. Fabric OneLake", "2. Data Engineering - Lakehouse"]
Section_Fabric_icons = ['caret-right-fill', 'caret-right-fill']
Section_Qlik = [""]
Section_Qlik_icons = ['caret-right-fill', 'caret-right-fill']


# --------------------------------------------------------------------------------------------------------------------------------------------
# Page settings
st.set_page_config(layout="wide")

# Sidebar width
st.markdown(
    """
    <style>
        section[data-testid = "stSidebar"] {
            width: 400px !important;
        }
    </style>
    """,
    unsafe_allow_html = True,
)

# Section navigation style
Nav_styles = {
    "container": {"padding": "0!important", "background-color": "#dbdbdb"},
    "nav-link": {"font-size": "17px", "text-align": "center", "margin": "0px", "--hover-color": "#c7c5c5"},
    "nav-link-selected": {"background-color": "#239583"},
}


# --------------------------------------------------------------------------------------------------------------------------------------------
# Menu laterale
with st.sidebar:
    selected = option_menu(
        "Topics", 
        Main_topics, 
        icons = Main_icons, 
        menu_icon = Menu_icon, 
        default_index = 0,
        styles = {
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#dbdbdb"},
            "nav-link-selected": {"background-color": "#479e92"},
        }
    )


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Text loader
Fabric_1_OneLake = load_text("Text/Fabric_1_OneLake.txt")
Fabric_2_Data_Engineering_Lakehouse = load_text("Text/Fabric_2_Data_Engineering_Lakehouse.txt")

########### Microsoft Fabric ############
if selected == "Microsoft Fabric" :
    menu_fabric = option_menu(
        None, 
        Section_Fabric, 
        icons = Section_Fabric_icons, 
        default_index = 0, 
        orientation = "horizontal",
        styles = Nav_styles
    )

    # General notes description
    st.markdown("""
    **Notes description**
    
    **Microsoft Fabric** is *web-based platform all-in-one solution* to work with data, from the ingestion to the data trasformation and the final visualization and delivery. 
    It offers the possibility to see and work with every aspect of data, including the possibility to implement Machine Learning models.

    These notes have been collected after following the Microsoft eLearning materials and while exploring the main *Fabric* features using a *Trial licence*.
    """)

    st.divider() 
    
    if menu_fabric == "1. Fabric OneLake" :
        st.markdown(Fabric_1_OneLake)
        
    if menu_fabric == "2. Data Engineering - Lakehouse" :
        st.markdown(Fabric_2_Data_Engineering_Lakehouse)


# ---------------------------------------------------------------------------------------------------
########### Qlik ############
elif selected == "Qlik (work in progress)":
    menu_qlik = option_menu(
        None, 
        Section_Qlik, 
        icons = Section_Qlik_icons, 
        default_index = 0, 
        orientation = "horizontal",
        styles = Nav_styles
    )

    # General notes description
    st.markdown("""
    **Notes description**

    *Work in Progress*
    """)

    st.divider() 
    
    if menu_qlik == "" :
        st.markdown("""
        *Work in Progress*
        """
        )



# --------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Footer (le funzioni utilizzate sono in functions.py)
if __name__ == "__main__":
    myargs = [ "Made in ", footer.image_render('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4', width = px(25), height = px(25)), 
        " by ", footer.link_render("https://www.linkedin.com/in/samuele-campitiello-ph-d-913b90104/", "Samuele Campitiello") ]
    footer.footer(*myargs)
