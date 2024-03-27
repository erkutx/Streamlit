import streamlit as st
import plotly.graph_objects as go
import calendar
from datetime import datetime

# ---------------- Settings -----------------

incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Savings"]
currency = "USD"
page_title = 'Income and Expense Tracker'
page_icon = ":money_with_wings:"
layout = 'centered'

# ---------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.title(page_title + " " + page_icon)

# ---------- DROPDOWN VALUES FOR SELECTION ------------

years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# ---------- INPUT & SAVE PERIOD ------------

st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    selected_month = col1.selectbox("Select Month:", months, key="month")
    selected_year = col2.selectbox("Select Year:", years, key="year")

    "---"

    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)

    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        comment = st.text_area("", placeholder="Enter a comment here...")

    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"]) + "_" + (st.session_state["month"])
        income_values = {income: st.session_state[income] for income in incomes}
        expense_values = {expense: st.session_state[expense] for expense in expenses}

        # TODO: Insert values into the database
        st.write(f"incomes: {income_values}")
        st.write(f"expenses: {expense_values}")
        st.success("Data saved!")

        # ----------- PLOT PERIODS -------------

        st.header("Data Visualization")
        with st.form("saved_periods"):
            # TODO: Get periods from db
            selected_period = st.selectbox("Select Period", ["2022_March"])
            submitted = st.form_submit_button("Plot Period")
            if submitted:
                # TODO: Get Data from database
                comment = "Some comment"
                incomes = {'Salary': 1500, 'Blog': 50, 'Other Income': 10}
                expenses = {'Rent': 600, 'Utilities': 200, 'Groceries': 300, 'Car': 100, 'Other Expenses': 50, 'Savings': 10}

                # Create metrics
                total_income = sum(incomes.values())
                total_expense = sum(expenses.values())
                remaining_budget = total_income - total_expense
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Income", f"{total_income} {currency}")
                col2.metric("Total Expense", f"{total_expense} {currency}")
                col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
                st.text(f"Comment: {comment}")

                # Create sankey chart
                label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
                source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
                target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
                value = list(incomes.values()) + list(expenses.values())

                # Data to dict, dict to sankey
                link = dict(source=source, target=target, value=value)
                node = dict(label=label, pad=30, thickness=30, color="#E694FF")
                data = go.Sankey(link=link, node=node)
                # Plot it!
                fig = go.Figure(data)
                fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
                st.plotly_chart(fig, use_container_width=True)
