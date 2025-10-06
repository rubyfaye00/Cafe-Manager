cafe_name = "Fresh Brew Crew"
tax_rate = 0.083
discount_rate = 0.10 
discount_code = "STUDENT10"


item_names = ["Latte", "Mocha", "Tea"]
item_price = [4.25, 4.25, 3.50]
item_quantities= [1, 1, 1]

discount_applied = False


def show_banner():
    print("=" * 40)
    print(f"{cafe_name} - Tax Rate: {tax_rate}")
    print("=" * 40)
 
def add_item(name: str, price: float, quantity: int): 
    item_names.append(name)
    item_price.append(price)
    item_quantities.append(quantity)
    print(f"Added: {name} x {quantity} @ ${price:.2f}")

def view_cart():
    if not item_names:
        print("Your cart is empty.") 
        return 
    
    subtotal = 0 
    
    print("---- Current Cart ----")
    
    for i in range(len(item_names)):
        subtotal += item_price[i] * item_quantities[i]
        # print(f"{i+1}) {item_names[i]} ${item_price[i]:.2f} x{item_quantities[i]} = ${line_total:.2f}")
    
    print(f"Subtotal: {subtotal}")

def remove_item(index: int):
    if 1 <= index <= len(item_names):
        removed_name = item_names.pop(index - 1)
        removed_price = item_price.pop(index - 1)
        removed_quantity = item_quantities.pop(index - 1)
        print(f"Removed: {removed_name}, {removed_quantity}, {removed_price}")
    else: 
        print("Invalid item number")

#def compute_subtotal():
#    return sum(item_price[i] * item_quantities[i] for i in range(len(item_names)))
# make your own loop!

def compute_tax(subtotal, tax_rate):
    return subtotal * tax_rate

'''
def apply_discount(subtotal, code):
    global discount_applied 
    if code == discount_code and not discount_applied:
        discount_applied = True 
        return subtotal * discount_rate
    
        

    userCode = input("EnterCode: ")
    if( userCode == "STUDENT10"):
        return subtotal * discount_rate 
    
    
    return 0.0
'''
def checkout():
    if not item_names:
        print("Cart is empty.")
        return 
    
    subtotal = compute_subtotal()
    print(f"Cart subtotal: ${subtotal:.2f}")
    code = input("Enter discount code (or press Enter): ").strip()
    discount = apply_discount(subtotal, code)
    tax = compute_tax(subtotal - discount, tax_rate)
    total = subtotal - discount + tax 

# research rounding to 2 decimal places
    print("---- RECEIPT ----")
    
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print(f"Thank you for visiting {cafe_name}!")

def main_menu():
    while True:
        print("----------------")
        print("1. Add item.")
        print("2. View cart.")
        print("3. Remove item.")
        print("4. Checkout.")
        print("5. Quit.")
        print("----------------")

        choice = input("Choose: ").strip()
        
        if choice == "1":
            name = input("Item name: ").strip()
            price = float(input("Item price: "))
            quantity = int(input("Quantity: "))
            if name and price > 0 and quantity > 0:
                add_item(name, price, quantity)
            else: 
                print("Invalid entry, please try again.")
        
        elif choice == "2":
            view_cart()
        
        elif choice == "3":
            if not item_names:
                print("Cart is empty.")
            else: 
                view_cart()
                try: 
                    index = int(input("Enter item number to remove: "))
                    remove_item(index)
                except ValueError:
                    print("Invalid input, please enter a number")
        
        elif choice == "4":
            checkout()
        
        elif choice == "5": 
            print(f"Thank you for visiting {cafe_name}!")
            break 
        
        else:
            print("Invalid choice, please select from the menu.")


def main():
    show_banner()
    main_menu()

main()


        
            




    
    
 