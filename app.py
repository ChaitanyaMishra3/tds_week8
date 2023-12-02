import streamlit as st

def find_greatest_number(a, b, c):
    if (a > b and a > c):
        return f'{a} is greatest'
    elif (b > c and b > a):
        return f'{b} is greatest'
    else:
        return f'{c} is greatest'

def main():
    st.title("Greatest Number Finder")

    # Input fields in the UI
    a = st.number_input("Enter first number:")
    b = st.number_input("Enter second number:")
    c = st.number_input("Enter third number:")

    # Button to trigger the calculation
    if st.button("Find Greatest Number"):
        result = find_greatest_number(a, b, c)
        st.success(result)

if __name__ == "__main__":
    main()
