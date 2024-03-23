import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit


# ---------------- Settings -----------------

incomes = ["Salary", "Blog" , "Other Income" ]
expenses = ["Rent","Utilities","Groceries","Car","Other Exxpenses", "Savings"]
currency = "USD"
page_title = 'Income  and Expense Tracker'
page_icon = ":money with wings:"
layout = 'centered'

# ---------------------

st.set_page_config (page_titl=page_title,page_icon=page_icon, layout=layout) 

st.title(page_title + " " + page_icon)








