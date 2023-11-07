"""Dining Experience Manager - Joby Farra."""


def print_menu():
    """ Module providing a function printing menu."""
    print("""
        Welcome to Dining Experience
        
        Menu:
        1. Mozzarella Sticks   $ 6.99
        2. Grilled Chicken     $14.99
        3. Spaghetti Carbonara $12.99
        4. Grilled Salmon      $16.99
        5. Tiramisu            $ 6.99
        
    """)


def display_order(order_detail, meals_dic):
    """Module providing a function printing order detail."""
    print("This is your order!")
    for k in order_detail:
        print(f"{meals_dic[k]['name']}  ${meals_dic[k]['PRICE']}  Amount:{order_detail[k]}")


meals = {1: {"name": "Mozzarella Sticks", "price": 6.99},
         2: {"name": "Grilled Chicken", "price": 14.99},
         3: {"name": "Spaghetti Carbonara", "price": 12.99},
         4: {"name": "Grilled Salmon", "price": 16.99},
         5: {"name": "Tiramisu", "price": 6.99},
         }

CONDITION = "M"
order = {}
while CONDITION.upper() != "N":
    if CONDITION.upper() == "M":
        print_menu()
        CONDITION = ""
    print("Please enter the number of the meal:")
    meal = input("Meal: ")
    while not meal.isdigit() or not 1 <= int(meal) <= 5:
        print("Please, enter a valid option")
        meal = input("Meal: ")
    amount = input("Amount: ")
    while not amount.isdigit() or 0 >= int(amount):
        print("Please, enter a valid Amount")
        amount = input("Amount: ")
    if meal not in order:
        order[int(meal)] = int(amount)
    else:
        order[int(meal)] += int(amount)
    condition = input("Do you want another meal?(N:No - M: Display the Menu):")
    if sum(order.values()) > 100:
        print("You attempt to order more than 100 meals. Restarting the order ....")
        order = {}

PRICE = 5.0
DISCOUNT = 0.0
SPECIAL_OFFER = 0
if 5 <= sum(order.keys()) < 10:
    DISCOUNT = 0.1
elif 10 <= sum(order.keys()):
    DISCOUNT = 0.2

for key, item in order.items():
    PRICE += meals[key]["price"] * item

if 50 < PRICE < 100:
    SPECIAL_OFFER += 10
elif PRICE > 100:
    SPECIAL_OFFER += 25

display_order(order, meals)
print(f"The total cost is: ${(PRICE - SPECIAL_OFFER) * (1 - DISCOUNT)}")
confirmation = input("Please enter OK to accept your order")
if confirmation.upper() == "OK":
    print(1)
else:
    print(-1)
