import streamlit as st

st.set_page_config(
page_title="Food Corner Restaurant",
page_icon="🍽️",
layout="wide"
)

st.title("🍽️ Food Corner Restaurant")
st.markdown("### Delicious Food, Happy Moments ❤️")
st.write("Welcome! Choose your favourite food and enjoy!")

st.divider()

# Restaurant menu

menu = {
"Pizza": {
"price": 120,
"image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500"
},
"Burger": {
"price": 80,
"image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500"
},
"Salad": {
"price": 40,
"image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=500"
},
"Coffee": {
"price": 25,
"image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500"
}
}

st.header("🍴 Our Menu")

col1, col2 = st.columns(2)

selected_items = {}

for index, (item, details) in enumerate(menu.items()):
    with (col1 if index % 2 == 0 else col2):
        st.image(details["image"], use_container_width=True)
        st.subheader(item)
        st.write(f"Price: ₹{details['price']}")

        quantity = st.number_input(
            f"Select quantity of {item}",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key=item
        )

        selected_items[item] = quantity
        st.divider()

st.header("🧾 Your Bill")

total = 0

for item, quantity in selected_items.items():
    if quantity > 0:
        amount = menu[item]["price"] * quantity
        total += amount
        st.write(f"{item} × {quantity} = ₹{amount}")

st.subheader(f"Total Amount: ₹{total}")

if st.button("🛒 Place Order", type="primary"):
    if total > 0:
        st.balloons()
        st.success(f"Thank you! Your order total is ₹{total}.")
    else:
        st.warning("Please select at least one food item.")