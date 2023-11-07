
def print_menu():
    print("""
        Welcome to Dining Experience
        
        Menu:
        1. Mozzarella Sticks   $ 6.99
        2. Grilled Chicken     $14.99
        3. Spaghetti Carbonara $12.99
        4. Grilled Salmon      $16.99
        5. Tiramisu            $ 6.99
        
    """)

meals = {1:{"name":"Mozzarella Sticks","price":6.99},
         2: {"name": "Grilled Chicken", "price": 14.99},
         3: {"name": "Spaghetti Carbonara", "price": 12.99},
         4: {"name": "Grilled Salmon", "price": 16.99},
         5: {"name": "Tiramisu", "price": 6.99},
         }

condition = "M"
order = {}
while condition.upper() != "N":
    if condition.upper() == "M":
        print_menu()
        condition = ""
    print("Please enter the number of the meal:")
    meal = input("Meal: ")
    while not meal.isdigit() or  not 1<= int(meal) <= 5:
        print("Please, enter a valid option")
        meal = input("Meal: ")
    amount = input("Amount: ")
    while not amount.isdigit() or  not 0< int(amount) <= 100:
        print("Please, enter a valid Amount")
        amount = input("Amount: ")
    if meal not in order:
        order[int(meal)] = int(amount)
    else:
        order[int(meal)] += int(amount)
    condition = input("Do you want another meal?(Y:Yes - N:No - M: Display the Menu):")

price = 5.0
discount = 0.0
special_offer = 0
if 5 <= sum(order.keys()) < 10:
    discount = 0.1
elif 10 <= sum(order.keys()):
    discount = 0.2

for item in order:
