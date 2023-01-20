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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def returnChange(total, price):
    if total < price:
        return -1
    else:
        return total - price


def takeCoin():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def checkResources(name):
    if MENU[name]["ingredients"]["water"] > resources["water"]+1:
        return "water"
    if name != 'espresso' and MENU[name]["ingredients"]["milk"] > resources["milk"]+1:
        return "milk"
    if MENU[name]["ingredients"]["coffee"] > resources["coffee"]+1:
        return "coffee"
    else:
        return 1


def reducer(name):
    if name != "espresso":
        resources["water"] -= MENU[name]["ingredients"]["water"]
        resources["milk"] -= MENU[name]["ingredients"]["milk"]
        resources["coffee"] -= MENU[name]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[name]["ingredients"]["water"]
        resources["coffee"] -= MENU[name]["ingredients"]["coffee"]


coffeeMachineStates = True
moneyCollected = 0

while coffeeMachineStates:
    userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if userInput == "report":
        for item, value in resources.items():
            print(f'{item} : {value}')
        print("Money : ", moneyCollected)
    elif userInput == "espresso" or userInput == "cappuccino" or userInput == "latte":
        if checkResources(userInput) != 1:
            print(f"Sorry there is not enough {checkResources(userInput)}")
        else:
            money = takeCoin()
            returnCoin = round(returnChange(money, MENU[userInput]["cost"]), 2)
            # print(f'{money} {MENU[userInput]["cost"]}')
            if returnCoin == -1:
                print("Sorry that not enough money, Money refunded.")
            else:
                moneyCollected += MENU[userInput]["cost"]
                reducer(userInput)
                print(f"Here is ${returnCoin} in change")
                print(f"Here is your {userInput} Enjoy!")
                # for item, value in resources.items():
                #    print(f'{item} : {value}')
                # print("Money: ", moneyCollected)
    elif userInput == "off":
        coffeeMachineStates = False

# todo 1. to return the amount of resources present in the mashine including money
# todo 2. ask user what would he like to have
# todo 2. check if the machine have enough amount of ingrdians and user have ented all money needed
# todo 3. ask the amount of coins inserted and refund the rest according to the coffee offered
# todo 4. make coffee and print the here your coffee and enjoy
