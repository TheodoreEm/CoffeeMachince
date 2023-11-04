
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# TODO: 1. FIRST QUESTION
#
# first_question=input("Prompt user by asking “What would you like? (espresso/latte/cappuccino):” ").lower()
#
#
# money= quarters_deposit * 0.25 + dimes_deposit * 0.1 + nickles_deposit * 0.05 + pennies_deposit * 0.01
# water = resources["water"]
# milk = resources["milk"]
# coffee = resources["coffee"]
#
# print(MENU["espresso"]["ingredients"]["water"])
#
# es_water = MENU["espresso"]["ingredients"]["water"]
# es_coffee = MENU["espresso"]["ingredients"]["coffee"]
# es_cost = MENU["espresso"]["cost"]
#
# latte_water = MENU["latte"]["ingredients"]["water"]
# latte_coffee = MENU["latte"]["ingredients"]["coffee"]
# latte_milk = MENU["latte"]["ingredients"]["milk"]
# latte_cost = MENU["latte"]["cost"]
#
# cup_water = MENU["cappuccino"]["ingredients"]["water"]
# cup_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
# cup_milk = MENU["cappuccino"]["ingredients"]["milk"]
# cup_cost = MENU["cappuccino"]["cost"]
#
# while first_question!= "off":
#       if first_question=="report":
#          print(f"The current resource values: \nWater: {water}ml\nMilk: {milk}ml\nWater: {coffee}g\nMoney: ${money}")
#       elif first_question=="espresso":
#           if es_water > water or es_coffee >coffee or es_cost> money:
#               print("")
