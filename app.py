try:
    import streamlit as st  # type: ignore[import-not-found]
except ModuleNotFoundError:
    st = None

menu = {"Pizza": 120, "Burger": 80, "Salad": 40, "Coffee": 25}

if st is None:
    print("Streamlit is missing. Install it with: python -m pip install streamlit")
else:
    st.title("WELCOME TO OUR RESTAURANT")
    st.subheader("Here is our menu")
    for item, price in menu.items():
        st.write(f"{item}: {price}")
      