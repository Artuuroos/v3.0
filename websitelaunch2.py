import turtle
from turtle import color
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu



optionen2 = option_menu(menu_title=None,
                       options=["Home","Diagramm","Price","Notifi"],
                       icons=["house","graph-up","clock","alarm"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal",
                       )
if optionen2=="Home":
    st.write("Homepage")
    
else:
    if optionen2=="Diagramm":
        with st.sidebar:
            optionenside= option_menu(menu_title=None,
            options=["Liniendiagramm","Säulendiagramm"],
            icons=["graph-up","bar-chart-line"],
            menu_icon="",
            default_index=0,
            orientation="vertical",
        )
        if optionenside=="Liniendiagramm":
            st.write("Hier kommt ein Liniendiagramm hin")
            with st.form(key='form1'):
                submit_button = st.form_submit_button(label='Graph ansehen')
                if submit_button:
                    st.write("Knopf gedrückt")
                    
        else:
            
            st.write("Hier kommt ein Säulendiagramm hin")
            with st.form(key='form1'):
                submit_button1 = st.form_submit_button(label='Graph ansehen')
                if submit_button1:
                    st.write("Säulendiagramm angezeigt")  
                    
    if optionen2=="Price":
        st.write("Preisantizipation")
        
    if optionen2=="Notifi":
        st.markdown("Benachrichtigung")          
