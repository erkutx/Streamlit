import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
import calendar # pythpn core 
from datetime import datetime # from python core 


# ---------------- Settings -----------------

incomes = ["Salary", "Blog" , "Other Income" ]
expenses = ["Rent","Utilities","Groceries","Car","Other Expenses", "Savings"]
currency = "USD"
page_title = 'Income  and Expense Tracker'
page_icon = ":money_with_wings:"
layout = 'centered'

# ---------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(page_title + " " + page_icon)


# ---------- DROPDOWN VALUES FOR SELECTION ------------

years = [datetime.today().year , datetime.today().year + 1]
months = list(calendar.month_name[1:])



# ---------- INPUT & SAVE PERIOD ------------


st.header(f"Data Entry in {currency}")
with st.form("entry_form",clear_on_submit = True):
  col1, col2 = st.columns(2)
  col1.selectbox("Select Month:", months , key = "month")
  col2.selectbox("Select Year:", years, key="year")


"---"

with st.expander("Income"):
  for income in incomes:
    st.number_input(f"{income}:", min_value=0, format= "%i",step =10, key=income)

with st.expander("Expenses"):
  for expense in expenses:
    st.number_input(f"{expense}:", min_value=0, format="%i",step=10, key=expense) 






