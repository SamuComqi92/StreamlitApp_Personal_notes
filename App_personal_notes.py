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
        st.markdown("""
        ### OneLake

        ***OneLake*** is a single, unified *data lake* for the whole organization.
        It hosts only **one copy of data** for the entire organization to use in multiple analytica engines.[^1]

        OneLake is built on top of the *Azure Data Lake Storage (ADLS) Gen 2* and can support any type of file (structured or unstructured).
        All items are stored in the **Delta Parquet format** (columnar).
        It is also possible to create *shortcuts* for copying data from different locations (data stays in the original source).

        it is possible to use different *engines* to connect to data, using different languages (e.g. T-SQL, Python) and tools/services (e.g. Pipelines, Notebooks):
        
        - **T-SQL** (Warehousing)
        - **Spark** (Synapse Data Engineering & Data Science)
        - **Analysis Services** (for Power BI)
        - **KQL** (real-time analytics).

        Moreover, Microsoft Fabric can be integrated with **Git (Azure DevOps)** to manage Deployment Pipelines and *versioning*.
        Finally, it is possible to use ***Microsoft Purview*** to have details on Fabric Workspaces and data.
        In Fabric, it is possible to use ***Data Activator*** to set up alerts (e.g. from Power BI reports).

        Each process in Fabric (e.g. refreshes, notebooks, pipelines) can be monitored in the ***Monitoring Hub***.
        There is also an app called *Microsoft Fabric Capacity Metrics* ([link to the app](https://appsource.microsoft.com/en-us/product/power-bi/pbi_pcmm.microsoftpremiumfabricpreviewreport?tab=Overview)) to monitor resources usage across the Tenant (only for Admins).
        
        [^1]: OneLake is similar to an *Azure Data Lake Storage*.
        """)
        
    if menu_fabric == "2. Data Engineering - Lakehouse" :
        st.markdown("""
        ### Data Engineering - Lakehouse

        **Data engineering** in Microsoft Fabric enables users to design, build, and maitain infrastructures and systems that enable thier organizations to collect, store, process, and analyze large volumes of data.

        A ***Lakehouse*** is a storage (based on the Microsoft Fabric *OneLake*) for files and tables. When a Lakehouse is created, Fabric produces 3 items:

        - *Lakehouse*: **storage** of metadata, files, folders, and data.
        - *Semantic model*: automatic **data model** that can be used in Power BI for reporting.
        - *SQL Endpoint*: **read-only**, to connect to the Lakehouse and query its data using *T-SQL*.

        Data can be added to the Lakehouse (i.e. ingestion) in 4 ways:

        1. Simple *Upload* (manual upload).
        2. Using *Dataflows*, for additional data transformations (with Power Query Online - see next).
        3. Using *Notebooks* (in an *Apache Soark pool*); notebooks can be used to manipulated table using SQL.
        4. Through *Pipelines* (using the **Copy activity** in *Data Factory*).
        """)


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
