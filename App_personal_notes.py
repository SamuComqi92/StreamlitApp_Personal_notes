# --------------------------------------------------------------------------------------------------------------------------------------------
# Usefull libraries
from PIL import Image
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
Main_topics = ["Landing page", "Microsoft Fabric", 'Qlik to Power BI (WIP)']
Main_icons = ['house', 'clipboard-data', 'graph-up-arrow']
Section_Fabric = ["1. Fabric OneLake", "2. Data Engineering - Lakehouse", "3. Data Engineering – Data Factory: Pipelines", "4. Data Engineering – Data Factory: Dataflows", "5. Data Warehouse", "6. Data Science", "7. Real-Time Analytics", "8. Data Activator", "9. Administration aspects of Microsoft Fabric"]
Section_Fabric_icons = ['caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill']
Section_Qlik = [""]
Section_Qlik_icons = ['caret-right-fill', 'caret-right-fill']


# --------------------------------------------------------------------------------------------------------------------------------------------
# Page settings
st.set_page_config(layout = "wide")

# Sidebar width
st.markdown( """<style>section[data-testid = "stSidebar"] {width: 400px !important;}</style>""", unsafe_allow_html = True )

# Radio button formatting (from web)
st.html("""
    <style>
        /* convert radio to list of buttons */
        div[role="radiogroup"] {
            flex-direction:row;
        }
        input[type="radio"] + div {
            background: #e8e8e8  !important;
            color: #000000;
            border-radius: 10px !important;
            padding: 8px 18px !important;
        }
        input[type="radio"][tabindex = "0"] + div {
            background: #239583 !important;
            color: #000000 !important;
        }
        input[type = "radio"][tabindex = "0"] + div p {
            color: #ffffff !important;
        }
        div[role = "radiogroup"] label > div:first-child {
            display: none !important;
        }
        div[role = "radiogroup"] label {
            margin-right: 0px !important;
        }
        div[role = "radiogroup"] {
            gap: 12px;
        }
    </style>
""")

# Section navigation style
Nav_styles = {
    "nav-link": {"font-size": "14px", "text-align": "center", "margin": "3px", "--hover-color": "#c7c5c5"},
    "nav-link-selected": {"background-color": "#239583"},
}


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Text loader
Fabric_0_Introduction = load_text("Text/Fabric_0_Introduction.txt")
Fabric_1_OneLake = load_text("Text/Fabric_1_OneLake.txt")
Fabric_2_Data_Engineering_Lakehouse = load_text("Text/Fabric_2_Data_Engineering_Lakehouse.txt")
Fabric_2_1_Create_a_Lakehouse = load_text("Text/Fabric_2.1_Create_a_Lakehouse.txt")
Fabric_2_2_Create_Notebooks = load_text("Text/Fabric_2.2_Create_Notebooks.txt")
Fabric_2_2_1_Create_tables = load_text("Text/Fabric_2.2.1_Create_tables.txt")
Qlik2PBI_0_Introduction = load_text("Text/Qlik2PBI_0_Introduction.txt")

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


########### Landing page ############
if selected == "Landing page" :
    st.markdown("""
    #### **Welcome to My Digital Notebook**
    
    I designed this space to collect *my notes* on different topics, from programming to machine learning and systems dedicated to data management, manipulation and visualization.
    
    I have collected a lot of notes over the last 2-3 years and decided to collect them here in an orderly manner.
    
    Obviously, it will take some time to write everything down and what I include will be subject to future changes and additions, based on my explorations and testing.
    
    The web page is public so anyone can have access.
    
    Enjoy 😃
    """
    )

    st.divider()

    # Fabric introduction
    st.image(Image.open(r'images/Logo_Fabric_2.png'), width = 150)
    st.markdown(Fabric_0_Introduction)

    st.write("")
    
    # Qlik to Power BI introduction
    st.image(Image.open(r'images/Qlik_to_PBI.png'), width = 150)
    st.markdown(Qlik2PBI_0_Introduction)


########### Microsoft Fabric ############
elif selected == "Microsoft Fabric" :

    # Title and logo
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(Image.open(r'images/Logo_Fabric.png'), width = 480)

    st.write("Navigate using the below menu:")

    with st.sidebar:
        menu_fabric = option_menu(
            None, 
            Section_Fabric, 
            icons = Section_Fabric_icons, 
            default_index = 0, 
            styles = Nav_styles
        )

    if menu_fabric == "1. Fabric OneLake" :
        st.markdown(Fabric_1_OneLake)
        
    if menu_fabric == "2. Data Engineering - Lakehouse" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "2.1 Create a Lakehouse", "2.2 Create Notebooks"], 
            icons = ["list", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )
      
        if selected_lakehouse == "Introduction" :
            st.markdown(Fabric_2_Data_Engineering_Lakehouse)
        elif selected_lakehouse == "2.1 Create a Lakehouse" :
            st.markdown(Fabric_2_1_Create_a_Lakehouse)
        elif selected_lakehouse == "2.2 Create Notebooks" :

            st.write("Navigate in one of these sections:")
            selected_notebook = st.radio(
                "",
                ["Introduction", "Create tables", "Time travel", "Print and display", "Update a table", "Add columns", "Use SQL", "Data Wrangler", "Sempy", "Other functions & utilities"],
                label_visibility = "collapsed",
                horizontal = True
            )
            
            if selected_notebook == "Introduction" :
                st.markdown(Fabric_2_2_Create_Notebooks)
            elif selected_notebook == "Create tables" :
                st.markdown(Fabric_2_2_1_Create_tables)
                
                #code_python = """
                #def hello():
                #    print("Hello, Streamlit!")
                #"""
                #st.code(code_python, language = "python")
                #code_sql = """
                #SELECT * FROM database.schema.table_name
                #WHERE name = "Samuele"
                #"""
                #st.code(code_sql, language = "sql")
                #code_dax = """
                #CALCULATE(
                #    SUM(table[column]),
                #    table_dim[column_dim] IN {"casa", "chiesa"}
                #)
                #"""
                #st.code(code_dax, language = "dax")
            #    st.markdown(Fabric_2_1_Create_a_Lakehouse)
            #elif selected_notebook == "2.2 Create Notebooks" :
            #    st.markdown(Fabric_2_2_Create_Notebooks)


# ---------------------------------------------------------------------------------------------------
########### Qlik ############
elif selected == "Qlik to Power BI (WIP)":

    # Title and logo
    col_1, col_2, col_3 = st.columns(3)
    with col_2:
        st.image(Image.open(r'images/Qlik_to_PBI_2.png'), width = 450)
        
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
