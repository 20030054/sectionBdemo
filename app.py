import streamlit as st

def main():
    st.title("Simple Calculator Application")

    # Input fields for numbers
    num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

    # Dropdown to select operation
    operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

    # Calculate result based on operation
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
            st.success(f"The result of addition is: {result}")
        elif operation == "Subtract":
            result = num1 - num2
            st.success(f"The result of subtraction is: {result}")
        elif operation == "Multiply":
            result = num1 * num2
            st.success(f"The result of multiplication is: {result}")
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result of division is: {result}")
            else:
                st.error("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
