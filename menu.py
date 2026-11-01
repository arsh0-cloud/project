menu={
    "Pizza": 120,
    "Burger": 80,
    "Salad": 40,
    "Coffe": 25,
    }
print ("WELCOME TO THE PYTHON RESTAURANT")

print(" Here is our menu")
print("Pizza: 120")
print("Burger: 80")
print("Salad: 40")
print("Coffe: 25")

order_total = 0
#80+25  = 105
item_1 = input("Please enter the item you want to order: ").strip().lower()

if item_1 in menu:
    order_total += menu[item_1]
    print("Your item [item_1] has been added to your order.")
else:
    print("Sorry, we don't have that item on the menu.")
another_order = input("Would you like to order another item?(yes/no): ")
if another_order.lower() == "yes":
    item_2 = input("Please enter the item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2] #105+80
        print ("your item [item_2] has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu.")
    if item_2 in menu:
        print("Your total order amount is: ", order_total)
        print("Thank you for your order! Enjoy your meal!")
        if item_2 not in menu:
            print("sorry, we don't have that item on the menu.")
        else:
           print("Thank you for your order! Enjoy your meal!")

payment_method = input("Please enter your payment method (cash/card): ")
payment_method = payment_method.lower()
if payment_method == "cash":
    print("Please insert cash.")
elif payment_method == "card":  
    print("Please insert your card.")
if payment_method in ("cash", "card"):
    print("Your payment has been processed successfully.")
    
print ("Thank you for coming please visit again")
   

        