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
Main_topics = ["Microsoft Fabric", 'Qlik to Power BI', 'DP 2023 course notes', "Python notes"]
Main_icons = ['house', 'clipboard-data', 'graph-up-arrow', 'award', 'code-square']
Section_Fabric = ["1. Fabric OneLake", "2. Data Engineering - Lakehouse", "3. Data Engineering - Data Factory: Pipelines", "4. Data Engineering - Data Factory: Dataflows", "5. Data Warehouse", "6. Data Science", "7. Real-Time Analytics", "8. Data Activator", "9. Administration aspects of Microsoft Fabric"]
Section_Fabric_icons = ['caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill']
Section_Qlik = ["1. Connections and Sources", "2. Semantic model", "3. Visualizations and report layout", "4. Measures and Expressions", "5. Advanced functionalities"]
Section_Qlik_icons = ['caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill']
Section_DP203 = ["1. Introduction", "2. ADLS Gen2 & Big Data processing stages", "3. Azure Synapse Analytics", "4. Lakehouse", "5. Apache Spark", "6. Relational Data Warehouse", "7. Pipelines", "8. Hybrid Transactional/Analytical Processing", "9. Data Streaming", "10. Azure Databricks (base)"]
Section_DP203_icons = ['caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill', 'caret-right-fill']


# --------------------------------------------------------------------------------------------------------------------------------------------
# Page settings
st.set_page_config(layout = "wide")

# Sidebar width
st.markdown( """<style>section[data-testid = "stSidebar"] {width: 510px !important;}</style>""", unsafe_allow_html = True )

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
            gap: 7px;
        }
    </style>
""")

# Section navigation style
Nav_styles = {
    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "3px", "--hover-color": "#c7c5c5"},
    "nav-link-selected": {"background-color": "#239583"},
}


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Text loader
# Fabric
Fabric_0_Introduction = load_text("Text/Fabric/Fabric_0_Introduction.txt")
Fabric_1_OneLake = load_text("Text/Fabric/Fabric_1_OneLake.txt")
Fabric_2_Data_Engineering_Lakehouse = load_text("Text/Fabric/Fabric_2_Data_Engineering_Lakehouse.txt")
Fabric_2_1_Create_a_Lakehouse = load_text("Text/Fabric/Fabric_2.1_Create_a_Lakehouse.txt")
Fabric_2_2_Create_Notebooks = load_text("Text/Fabric/Fabric_2.2_Create_Notebooks.txt")
Fabric_2_2_1_Create_tables = load_text("Text/Fabric/Fabric_2.2.1_Create_tables.txt")
Fabric_2_2_2_Time_travel = load_text("Text/Fabric/Fabric_2.2.2_Time_travel.txt")
Fabric_2_2_3_Print_display = load_text("Text/Fabric/Fabric_2.2.3_Print_display.txt")
Fabric_2_2_4_Update_table = load_text("Text/Fabric/Fabric_2.2.4_Update_table.txt")
Fabric_2_2_5_Add_columns = load_text("Text/Fabric/Fabric_2.2.5_Add columns.txt")
Fabric_2_2_6_Use_SQL = load_text("Text/Fabric/Fabric_2.2.6_Use_SQL.txt")
Fabric_2_2_7_Data_Wrangler = load_text("Text/Fabric/Fabric_2.2.7_Data_Wrangler.txt")
Fabric_2_2_8_Sempy = load_text("Text/Fabric/Fabric_2.2.8_Sempy.txt")
Fabric_2_2_9_Other_functions = load_text("Text/Fabric/Fabric_2.2.9_Other_functions.txt")
Fabric_2_3_SQL_Endpoint = load_text("Text/Fabric/Fabric_2.3_SQL_Endpoint.txt")
Fabric_2_4_Create_report = load_text("Text/Fabric/Fabric_2.4_Create_report.txt")
Fabric_3_Data_Engineering_DataFactory_Pipelines = load_text("Text/Fabric/Fabric_3_Data_Engineering_DataFactory_Pipelines.txt")
Fabric_3_1_Create_pipeline = load_text("Text/Fabric/Fabric_3.1_Create_pipeline.txt")
Fabric_3_2_pipeline_notebook = load_text("Text/Fabric/Fabric_3.2_pipeline_notebook.txt")
Fabric_3_3_Delete_data = load_text("Text/Fabric/Fabric_3.3_Delete_data.txt")

# Qlik to Power BI
Qlik2PBI_0_Introduction = load_text("Text/Qlik2PBI/Qlik2PBI_0_Introduction.txt")
Qlik2PBI_1_Connection_sources = load_text("Text/Qlik2PBI/Qlik2PBI_1_Connection_sources.txt")
Qlik2PBI_1_PowerQuery_dataflows_Fabric = load_text("Text/Qlik2PBI/Qlik2PBI_1_PowerQuery_dataflows_Fabric.txt")
Qlik2PBI_2_Semantic_model = load_text("Text/Qlik2PBI/Qlik2PBI_2_Semantic_model.txt")
Qlik2PBI_3_Visuals = load_text("Text/Qlik2PBI/Qlik2PBI_3_Visuals.txt")

# DP-203 exam notes
DP203_0_Introduction = load_text("Text/DP_203/DP203_0_Introduction.txt")
DP203_1_Introduction = load_text("Text/DP_203/DP203_1_Introduction.txt")
DP203_2_ADLS_BigData = load_text("Text/DP_203/DP203_2_ADLS_BigData.txt")
DP203_3_Synapse = load_text("Text/DP_203/DP203_3_Synapse.txt")
DP203_4_Create_Lakehouse = load_text("Text/DP_203/DP203_4_Create_Lakehouse.txt")
DP203_5_Apache_Spark = load_text("Text/DP_203/DP203_5_Apache_Spark.txt")
DP203_6_Warehouse = load_text("Text/DP_203/DP203_6_Warehouse.txt")

# Python notes
Python_0_Introduction = load_text("Text/Python/Python_0_Introduction.txt")


# --------------------------------------------------------------------------------------------------------------------------------------------
# Menu laterale
with st.sidebar:
    st.markdown("# My Digital Notebook")
    main_selected = st.selectbox(
        "Choose a topic",
        Main_topics,
        index = None,
        placeholder = "Choose a topic...",
        label_visibility = "collapsed"
    )
    
    if main_selected != None :
        st.markdown("*Clear selection to go back to the Landing page*")
        st.write("")


########### Landing page ############
if main_selected == None :#"Landing page" :
    st.markdown("""
    # **Welcome to My Digital Notebook!**
    
    I designed this space to collect *my notes* on different topics, from programming to machine learning and systems dedicated to data management, manipulation and visualization.
    
    I have collected a lot of notes over the last 2-3 years and decided to collect them here in an orderly manner.
    Obviously, it will take some time to write everything down and what I include will be subject to future changes and additions, based on my explorations and testing.

    >***Important**: some notes are detailed, while others are just a simple list or few sentences.*
    
    The web page is public so anyone can have access.
    
    Enjoy 😃
    """
    )

    st.divider()

    # Fabric introduction
    st.image(Image.open(r'images/Logo_Fabric_2.png'), width = 150)
    st.markdown(Fabric_0_Introduction)

    st.write("")
    st.write("")
    
    # Qlik to Power BI introduction
    st.image(Image.open(r'images/Qlik_to_PBI.png'), width = 150)
    st.markdown(Qlik2PBI_0_Introduction)

    st.write("")
    st.write("")
    
    # DP-203 exam notes
    st.image(Image.open(r'images/DP_203_notes.png'), width = 150)
    st.markdown(DP203_0_Introduction)

    st.write("")
    st.write("")
    
    # DP-203 exam notes
    st.image(Image.open(r'images/Python_notes.png'), width = 150)
    st.markdown(Python_0_Introduction)

# --------------------------------------------------------------------------------------------------------
########### Microsoft Fabric ############
elif main_selected == "Microsoft Fabric" :

    # Title and logo
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(Image.open(r'images/Logo_Fabric.png'), width = 480)

    with st.sidebar:
        st.write("")
        st.markdown("**Navigation**")
        menu_fabric = option_menu(
            None, 
            Section_Fabric, 
            icons = Section_Fabric_icons, 
            default_index = 0, 
            styles = Nav_styles
        )

    ##### 1. Onelake
    if menu_fabric == "1. Fabric OneLake" :
        st.divider()
        st.markdown(Fabric_1_OneLake)

    ##### 2. Data Engineering - Lakehouse
    elif menu_fabric == "2. Data Engineering - Lakehouse" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "2.1 Create a Lakehouse", "2.2 Create Notebooks", "2.3 SQL Endpoint", "2.4 Create a report"], 
            icons = ["list", "file-earmark", "file-earmark", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )

        if selected_lakehouse != "2.2 Create Notebooks":
            st.divider()
            
        if selected_lakehouse == "Introduction" :
            st.markdown(Fabric_2_Data_Engineering_Lakehouse)
        elif selected_lakehouse == "2.1 Create a Lakehouse" :
            st.markdown(Fabric_2_1_Create_a_Lakehouse)
        elif selected_lakehouse == "2.2 Create Notebooks" :

            st.write("Navigate in one of these sections:")
            selected_notebook = st.radio(
                "",
                ["Introduction", "Create tables", "Time travel", "Print and display", "Update a table", "Add columns", "Use SQL", "Data Wrangler", "Sempy", "Other functions"],
                label_visibility = "collapsed",
                horizontal = True
            )

            st.divider()
            
            if selected_notebook == "Introduction" :
                st.markdown(Fabric_2_2_Create_Notebooks)
            elif selected_notebook == "Create tables" :
                st.markdown(Fabric_2_2_1_Create_tables)
            elif selected_notebook == "Time travel" :
                st.markdown(Fabric_2_2_2_Time_travel)
            elif selected_notebook == "Print and display" :
                st.markdown(Fabric_2_2_3_Print_display)
            elif selected_notebook == "Update a table" :
                st.markdown(Fabric_2_2_4_Update_table)
            elif selected_notebook == "Add columns" :
                st.markdown(Fabric_2_2_5_Add_columns)
            elif selected_notebook == "Use SQL" :
                st.markdown(Fabric_2_2_6_Use_SQL)
            elif selected_notebook == "Data Wrangler" :
                st.markdown(Fabric_2_2_7_Data_Wrangler)
            elif selected_notebook == "Sempy" :
                st.markdown(Fabric_2_2_8_Sempy)
            elif selected_notebook == "Other functions" :
                st.markdown(Fabric_2_2_9_Other_functions)

        elif selected_lakehouse == "2.3 SQL Endpoint":
            st.markdown(Fabric_2_3_SQL_Endpoint)

        elif selected_lakehouse == "2.4 Create a report" :
            st.markdown(Fabric_2_4_Create_report)


    ##### 3. Data Engineering - Data Factory - Pipelines
    elif menu_fabric == "3. Data Engineering - Data Factory: Pipelines" :

        st.write("Navigate in one of these pages:")
        selected_pipeline = option_menu(
            None,
            ["Introduction", "3.1 Create a pipeline", "3.2 Pipeline to Notebook", "3.3 Delete Data Activity"], 
            icons = ["list", "file-earmark", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )

        if selected_pipeline == "Introduction" :
            st.markdown(Fabric_3_Data_Engineering_DataFactory_Pipelines)
        elif selected_pipeline == "3.1 Create a pipeline" :
            st.markdown(Fabric_3_1_Create_pipeline)
        elif selected_pipeline == "3.2 Pipeline to Notebook" :
            st.markdown(Fabric_3_2_pipeline_notebook)
        elif selected_pipeline == "3.3 Delete Data Activity" :
            st.markdown(Fabric_3_3_Delete_data)
    
    ##### 4. Data Engineering - Data Factory - Dataflows
    elif menu_fabric == "4. Data Engineering - Data Factory: Dataflows" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "4.1 Create a dataflow", "4.2 Publication and usage of a dataflow"], 
            icons = ["list", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


    ##### 5. Data Warehouse
    elif menu_fabric == "5. Data Warehouse" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "5.1 Create a Warehouse", "5.2 Create a data model", "Connection to SSMS", "5.4 Security"], 
            icons = ["list", "file-earmark", "file-earmark", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


    ##### 6. Data Science
    elif menu_fabric == "6. Data Science" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "6.1 Create a data science model inside a Notebook", "6.2 Validation and metrics"], 
            icons = ["list", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


    ##### 7. Real-Time Analytics
    elif menu_fabric == "7. Real-Time Analytics" :
        st.markdown("***Notes on Real-Time Analytics: missing***")


    ##### 8. Data Activator
    elif menu_fabric == "8. Data Activator" :
        st.markdown("***Notes on Data Activator: missing***")


    ##### 9. Administration aspects of Microsoft Fabric
    elif menu_fabric == "9. Administration aspects of Microsoft Fabric" :
        
        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Introduction", "9.1 Licensing and Pricing"], 
            icons = ["list", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


# =============================================================================================================================================================================
########### Qlik ############
elif main_selected == "Qlik to Power BI":

    # Title and logo
    col_1, col_2, col_3 = st.columns(3)
    with col_2:
        st.image(Image.open(r'images/Qlik_to_PBI_2.png'), width = 410)

    with st.sidebar:
        st.write("")
        st.markdown("**Navigation**")
        menu_qlik = option_menu(
            None, 
            Section_Qlik, 
            icons = Section_Qlik_icons, 
            default_index = 0, 
            styles = Nav_styles
        )

    ##### 1. Connections and Sources
    if menu_qlik == "1. Connections and Sources" :
        
        st.write("Navigate in one of these pages:")
        selected_qlik = option_menu(
            None,
            ["Quick comparison", "Power Query vs. T-SQL and Microsoft Fabric Notebooks"], 
            icons = ["file-earmark", "file-earmark", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )

        if selected_qlik == "Quick comparison" :
            st.markdown(Qlik2PBI_1_Connection_sources)
        elif selected_qlik == "Power Query vs. T-SQL and Microsoft Fabric Notebooks" :
            st.markdown(Qlik2PBI_1_PowerQuery_dataflows_Fabric)
                
    ##### 2. Semantic model
    elif menu_qlik == "2. Semantic model" :
        st.markdown(Qlik2PBI_2_Semantic_model)

    ##### 3. Visualizations and report layout
    elif menu_qlik == "3. Visualizations and report layout" :
        st.markdown(Qlik2PBI_3_Visuals)


    ##### 4. Measures and Expressions
    elif menu_qlik == "4. Measures and Expressions" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Analogies between Qlik and DAX", "Examples"], 
            icons = ["file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


    ##### 5. Advanced functionalities
    elif menu_qlik == "5. Advanced functionalities" :

        st.write("Navigate in one of these pages:")
        selected_lakehouse = option_menu(
            None,
            ["Section Access and OLS", "Object conditional visiblity", "Dynamic naming", "Custom ordering", "Page conditional visibility"], 
            icons = ["file-earmark", "file-earmark", "file-earmark", "file-earmark", "file-earmark"], 
            default_index = 0,
            orientation = "horizontal",
            styles = {
                "nav-link": {"font-size": "12px", "text-align": "center", "margin": "0px", "--hover-color": "#dbdbdb"},
                "nav-link-selected": {"background-color": "#479e92"},
            }
        )


# =============================================================================================================================================================================
########### DP 203 ############
elif main_selected == "DP 2023 course notes":

    # Title and logo
    col_1, col_2, col_3 = st.columns(3)
    with col_2:
        st.image(Image.open(r'images/DP_203_notes_2.png'), width = 410)

    with st.sidebar:
        st.write("")
        st.markdown("**Navigation**")
        menu_dp_203 = option_menu(
            None, 
            Section_DP203, 
            icons = Section_DP203_icons, 
            default_index = 0, 
            styles = Nav_styles
        )

    ##### 1. Introduction
    if menu_dp_203 == "1. Introduction" :
        st.markdown(DP203_1_Introduction)
    elif menu_dp_203 == "2. ADLS Gen2 & Big Data processing stages" :
        st.markdown(DP203_2_ADLS_BigData)
    elif menu_dp_203 == "3. Azure Synapse Analytics" :
        st.markdown(DP203_3_Synapse)
    elif menu_dp_203 == "4. Lakehouse" :
        st.markdown(DP203_4_Create_Lakehouse)
    elif menu_dp_203 == "5. Apache Spark" :
        st.markdown(DP203_5_Apache_Spark)
    elif menu_dp_203 == "6. Relational Data Warehouse" :
        st.markdown(DP203_6_Warehouse)
        

########### Microsoft Fabric ############
elif main_selected == "Python notes" :
    # Title and logo
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(Image.open(r'images/Logo_Python.png'), width = 480)

    with st.sidebar:
        st.write("")
        st.markdown("**Navigation**")
        menu_python = option_menu(
            None, 
            Section_Fabric, 
            icons = Section_Fabric_icons, 
            default_index = 0, 
            styles = Nav_styles
        )

    
# ================================================================================================================================================================
# ================================================================================================================================================================
# Footer (le funzioni utilizzate sono in functions.py)
if __name__ == "__main__":
    myargs = [ "Made in ", footer.image_render('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4', width = px(25), height = px(25)), 
        " by ", footer.link_render("https://www.linkedin.com/in/samuele-campitiello-ph-d-913b90104/", "Samuele Campitiello") ]
    footer.footer(*myargs)
