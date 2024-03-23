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
with st.expander("Commnent"):
  comment = st.text_area("",placeholder="Enter a comment here...")

  

"---"
submitted = st.form_submit_button("Save Data")
if submitted:
  period = str(st.session_steal["year"]) + "_" + (st.session_steal["month"])
  incomes = {income: st.session_state[income] for income in incomes}
  expenses = {expense: st.session_state[expense] for expense in expenses}
  
# TODO:insert values into database 
  st.write(f"incomes: {incomes}")
  st.write(f"expenses: {expenses}")
  st.success("Data saved!")

  # ----------- PLOT PERIODS -------------


#if selected == "Data Visualization":
  st.header("Data Visualization")
  with st.form("saved_periods"):
    # TODO: Get periods from db
    period = st.selectbox("Select Period" , ["2022_March"])
    submitted = st.form_submit_button("Plot Period")
    if submitted:
      # TODO:Get Data from database
      comment = "Some comment"
      incomes = {'Salary': 1500, 'Blog': 50, 'Other Income': 10}
      expenses = {'Rent': 600, 'Utilities': 200,'Groceries': 300,  'Car': 100, 'Other Expenses': 50, 'Saving': 10}



      #Create metrics
      total_income = sum(incomes.values())
      total_expense = sum(expenses())
      remaining_budget = total_income - total_expense
      col1,col2,col3 = st.columns(3)
      col1.metric("Total Income", f"{total_income} {currency}")
      col2.metric("Total Expense", f"{total_expense} {currency}")
      col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
      st.text(f"Comment: {comment}")

   




