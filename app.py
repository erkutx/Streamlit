import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
import calendar # pythpn core 
from datetime import datetime # from python core 


# ---------------- Settings -----------------

incomes = ["Salary", "Blog" , "Other Income" ]
expenses = ["Rent","Utilities","Groceries","Car","Other Exxpenses", "Savings"]
currency = "USD"
page_title = 'Income  and Expense Tracker'
page_icon = ":money_with_wings:"
layout = 'centered'

# ---------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(page_title + " " + page_icon)


# ---------- DROPDOWN VALUES FOR SELECTION ------------

years = [datetime.today().year , datetime.today().year + 1]]
months = list(calendar.month_name[1:])

# ---------- INPUTs & SAVEs ------------







