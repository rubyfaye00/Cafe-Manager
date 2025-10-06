cafeName = "Fresh Brew Crew"
taxRate = 0.1
discountRate = 0.1
discountCode = "STUDENT10"


itemNames = []
itemPrice = []
itemQuantities = []

_discountApplied = False

def showBanner():
    print("=" * 40)
    print(f"{cafeName} - Taxrate: {taxRate}")
    print("=" * 40)

def addItem(name: str, price: float, qty: int):
    itemNames.append(name)
    itemPrice.append(price)
    itemQuantities.append(qty)


def computeSubtotal():
    subtotal = 0
    for i in range(len(itemNames)):
        subtotal += itemPrice[i] * itemQuantities[i]
    
    return subtotal 


def viewCart():
    if not itemNames:
        print("Your cart is empty.")
        return
    
    print("---- Current Cart ----")

    subtotal = 0

    for i in range(len(itemNames)):
        item_total = itemPrice[i] * itemQuantities[i]
        print(f"Item Totals:{itemNames[i]} - ${itemPrice[i]:.2f} * {itemQuantities[i]}")    
    print(computeSubtotal())



def removeItem(index: int):
    if 1 <= index <= len(itemNames):
        removedName = itemNames.pop(index - 1)
        removedPrice = itemPrice.pop(index - 1)
        removedQuantity = itemQuantities.pop(index - 1)
        print(f"Removed: {removedName}, {removedPrice}, {removedQuantity}")
    else:
        print("Invalid item number")



def computeTax(subtotal, taxRate):
    return subtotal * taxRate


def applyDiscount(subtotal, code):
    if code == discountCode:
        print("Discount applied")
        return subtotal * discountRate
    else:
        print("No discount applied")
        return 0 


def checkout():
    if not itemNames:
        print("Cart is empty")
        return 
    _code = input("Enter discount code:\n>> ")
    subtotal = computeSubtotal()
    discount = applyDiscount(subtotal, _code)
    tax = computeTax(subtotal - discount, taxRate)
    total = subtotal - discount + tax


    print("---- RECEIPT ----")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: +${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Thank you for visiting {cafeName}!")
    print("------------------")



def mainMenu():
    showBanner()
    while True:
        print("---------------")
        print("1. Add Item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Checkout")
        print("5. Quit")
        print("---------------")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Item name: ").strip()
            price = float(input("Item price: "))
            qty = int(input("Quantity: "))
            if name and price > 0 and qty > 0:
                addItem(name, price, qty)
            else:
                print("Invalid entry, please try again")
        
        elif choice == "2":
            viewCart()

        elif choice == "3": 
            if not itemNames:
                print("Cart is empty")
            else:
                viewCart()
                try:
                    index = int(input("Enter item number to remove "))
                    removeItem(index)
                except ValueError:
                    print("Invalid input, please try again")

        elif choice == "4":
            checkout()

        elif choice == "5":
            print(f"Thank you for visiting {cafeName}!")

        else: 
            print("invalid choice, please select from the menu")

mainMenu()

            
                    
