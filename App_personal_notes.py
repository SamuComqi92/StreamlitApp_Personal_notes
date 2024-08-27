# --------------------------------------------------------------------------------------------------------------------------------------------
# Usefull libraries
import streamlit as st
from functions import footer
from streamlit_option_menu import option_menu
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px

# --------------------------------------------------------------------------------------------------------------------------------------------
# Titles & Icons
Menu_icon = "menu-up"
Main_topics = ["Microsoft Fabric", 'Qlik']
Main_icons = ['clipboard-data', 'graph-up-arrow']
Section_Fabric = ["Fabric section 1", "Fabric section 2"]
Section_Fabric_icons = ['house', 'gear']
Section_Qlik = ["Qlik section 1", "Qlik section 2"]
Section_Qlik_icons = ['house', 'gear']


# --------------------------------------------------------------------------------------------------------------------------------------------
# Page settings
st.set_page_config(layout="wide")

# Sidebar width
st.markdown(
    """
    <style>
        section[data-testid = "stSidebar"] {
            width: 500px !important;
        }
    </style>
    """,
    unsafe_allow_html = True,
)


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
            "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "lightgrey"},
            "nav-link-selected": {"background-color": "#479e92"},
        }
    )

if selected == "Microsoft Fabric" :
    menu_3 = option_menu(
        None, 
        Section_Fabric, 
        icons = Section_Fabric_icons, 
        default_index = 0, 
        orientation = "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgrey"},
            "nav-link": {"font-size": "17px", "text-align": "center", "margin":"0px", "--hover-color": "lightgrey"},
            "nav-link-selected": {"background-color": "#239583"},
        }
    )
    
    st.write("Text Text Text")


elif selected == "Qlik":
    menu_2 = option_menu(
        None, 
        Section_Qlik, 
        icons = Section_Qlik_icons, 
        default_index = 0, 
        orientation = "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgrey"},
            "nav-link": {"font-size": "17px", "text-align": "center", "margin":"0px", "--hover-color": "lightgrey"},
            "nav-link-selected": {"background-color": "#6eb241"},
        }
    )

    st.write("Text Text Text")



# --------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Footer (le funzioni utilizzate sono in functions.py)
if __name__ == "__main__":
    myargs = [ "Made in ", footer.image_render('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4', width = px(25), height = px(25)), 
        " by ", footer.link_render("https://www.linkedin.com/in/samuele-campitiello-ph-d-913b90104/", "Samuele Campitiello") ]
    footer.footer(*myargs)
