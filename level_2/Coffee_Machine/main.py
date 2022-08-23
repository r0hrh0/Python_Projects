def prompt():
    beverage = input("What would you like? (espresso/latte/cappuccino/report): ")
    return beverage


def price_list(selection):
    cost = 0
    if selection == "espresso":
        cost = 1.5
    elif selection == "latte":
        cost = 2.5
    elif selection == "cappuccino":
        cost = 3
    return cost


def report(ingredients, money):
    for item in ingredients:
        if item == "milk" or "water":
            print(f"{item}: {ingredients[item]} ml")
        elif item == "coffee":
            print(f"{item}: {ingredients[item]} gm")
    print(f"Money: ${money}")


def check_resource(selection, ingredients):
    if selection == "espresso":
        if ingredients["water"] < 50 or ingredients["coffee"] < 18:
            if ingredients["water"] < 50:
                print("Sorry, there is not enough water.")
                return False
            elif ingredients["coffee"] < 18:
                print("Sorry, there is not enough coffee.")
                return False
        elif ingredients["water"] >= 50 and ingredients["coffee"] >= 18:
            return True

    elif selection == "latte":
        if ingredients["water"] < 200 or ingredients["coffee"] < 24 or ingredients["milk"] < 150:
            if ingredients["water"] < 200:
                print("Sorry, there is not enough water.")
                return False
            elif ingredients["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                return False
            elif ingredients["milk"] < 150:
                print("Sorry, there is not enough milk.")
                return False
        elif ingredients["water"] >= 200 and ingredients["coffee"] >= 24 and ingredients["milk"] >= 150:
            return True

    elif selection == "cappuccino":
        if ingredients["water"] < 250 or ingredients["coffee"] < 24 or ingredients["milk"] < 100:
            if ingredients["water"] < 250:
                print("Sorry, there is not enough water.")
                return False
            elif ingredients["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                return False
            elif ingredients["milk"] < 100:
                print("Sorry, there is not enough milk.")
                return False
        elif ingredients["water"] >= 250 and ingredients["coffee"] >= 24 and ingredients["milk"] >= 100:
            return True


def process_coins(price, selection):

    cash = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    cash += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if cash < price:
        print("Sorry, money not sufficient. Money refunded.")
        return False
    elif cash == price:
        print(f"Here is your {selection}. Enjoy!")
        return True
    else:
        change = cash - price
        change = round(change, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {selection} ☕. Enjoy!")
        return True


def update_report(selection, ingredients):
    if selection == "espresso":
        ingredients["water"] -= 50
        ingredients["coffee"] -= 18

    elif selection == "latte":
        ingredients["water"] -= 200
        ingredients["coffee"] -= 24
        ingredients["milk"] -= 150

    elif selection == "cappuccino":
        ingredients["water"] -= 250
        ingredients["coffee"] -= 24
        ingredients["milk"] -= 100

    return ingredients


def coffee_machine():
    machine_on = True
    ingredients = {"water": 300, "milk": 200, "coffee": 100}
    money = 0
    while machine_on:
        selection = prompt()
        print(selection)
        if selection == "report":
            print(report(ingredients, money))
        else:
            if check_resource(selection, ingredients):
                price = price_list(selection)
                if process_coins(price, selection):
                    ingredients = update_report(selection, ingredients)
                    money += price

            else:
                machine_on = False


coffee_machine()
