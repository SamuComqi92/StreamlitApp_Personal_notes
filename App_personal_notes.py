# Usefull libraries
import streamlit as st
from streamlit_option_menu import option_menu

# Menu laterale
with st.sidebar:
    selected = option_menu(
        "Topics", 
        ["Microsoft Fabric", 'Qlik'], 
        icons = ['house', 'gear'], 
        menu_icon = "cast", 
        default_index = 0
    )
    
if selected == "Qlik":
    menu_2 = option_menu(
        None, 
        ["Qlik 1", "Qlik 2"], 
        icons = ['house', 'gear'], 
        menu_icon = "cast", 
        default_index = 0, 
        orientation = "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgrey"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "lightgrey"},
            "nav-link-selected": {"background-color": "#6eb241"},
        }
    )

    st.write("Vediamo che succede")

elif selected == "Microsoft Fabric" :
    menu_3 = option_menu(
        None, 
        ["Fabric 1", "Fabric 2"], 
        icons = ['house', 'gear'], 
        menu_icon = "cast", 
        default_index = 0, 
        orientation = "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgrey"},
            "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "lightgrey"},
            "nav-link-selected": {"background-color": "#239583"},
        }
    )
    
    st.write("Vediamo Fabric")