# Usefull libraries
import streamlit as st
from functions import footer
from streamlit_option_menu import option_menu
from htbuilder import HtmlElement, div, hr, a, p, img, styles
from htbuilder.units import percent, px

# Menu laterale
with st.sidebar:
    selected = option_menu(
        "Topics", 
        ["Microsoft Fabric", 'Qlik'], 
        icons = ['✅house', 'gear'], 
        menu_icon = "cast", 
        default_index = 0,
        styles = {
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#479e92"},
        }
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


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Footer (le funzioni utilizzate sono in functions.py)
if __name__ == "__main__":
    myargs = [ "Made in ", footer.image_render('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4', width = px(25), height = px(25)), 
        " by ", footer.link_render("https://www.linkedin.com/in/samuele-campitiello-ph-d-913b90104/", "Samuele Campitiello") ]
    footer.footer(*myargs)
