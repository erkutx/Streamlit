import streamlit as st # pip install streamlit
import plotly.grapgh_objects as go # pipi install plotly 


# ---------------- Settings -----------------

incomes = ["Salary", "Blog" , "Other Income" ]
expenses = ["Rent","Utilities","Groceries","Car","Other Exxpenses", "Savings"]
currency = "USD"
page_title = 'Income  and Expense Tracker'
page_icon = ":money with wings:"
layout = 'centered'

# ---------------------

st.set_page_config (page_title-page_title,page_icon-page_icon, layout=layout) 

st.title(page_title + " " page_icon)









