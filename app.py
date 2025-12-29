import streamlit as st

def calculator (n1, n2, operation):
    if operation == "Add":
        return n1 + n2
    elif operation == "Subtract":
        return n1 - n2
    elif operation == "Multiply":
        return n1 * n2
    elif operation == "Divide":
        if n2 == 0:
            return None
        return n1 / n2


st.title("Simple calculator V4")

number1 = st.number_input("Enter First number", value = 0.0)
number2 = st.number_input("Enter Second number", value = 0.0)

operation = st.selectbox(
    "Choose operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button ("Calculate"):
    result = calculator(number1, number2, operation)

    if result is None and operation == "Divide":
        st.error("Cannot divide by zero")
    else:
        st.success(f"Result: {result}")
