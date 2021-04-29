BUY = "buy"
FILL = "fill"
TAKE = "take"
EXIT = "exit"
REMAINING = "remaining"

unit_supplies = {"water": "ml", "milk": "ml", "coffee beans": "grams"}


class CoffeeMachine:
    enough_resources = True
    coffees = {"espresso": {"water": 250, "milk": 0, "coffee beans": 16, "money": 4},
               "latte": {"water": 350, "milk": 75, "coffee beans": 20, "money": 7},
               "cappuccino": {"water": 200, "milk": 100, "coffee beans": 12, "money": 6}}

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk\n" \
               f"{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money"

    def take_money(self):
        taking_money = self.money
        self.money = 0
        return taking_money

    def naming_coffee(self, type_of_coffee):
        if type_of_coffee == "1":
            return "espresso"
        elif type_of_coffee == "2":
            return "latte"
        elif type_of_coffee == "3":
            return "cappuccino"
        else:
            return None

    def check_resources(self, name_of_coffee):
        self.enough_resources = True
        if self.water < self.coffees[name_of_coffee]["water"]:
            print("Sorry, not enough water!")
            self.enough_resources &= False
        if self.milk < self.coffees[name_of_coffee]["milk"]:
            self.enough_resources &= False
            print("Sorry, not enough milk!")
        if self.coffee_beans < self.coffees[name_of_coffee]["coffee beans"]:
            self.enough_resources &= False
            print("Sorry, not enough coffee beans!")
        if self.cups == 0:
            self.enough_resources &= False
            print("Sorry, not enough disposable cups!")

    def make_coffee(self, type_of_coffee):
        name_of_coffee = self.naming_coffee(type_of_coffee)
        if name_of_coffee is not None:
            self.check_resources(name_of_coffee)
            if self.enough_resources:
                print("I have enough resources, making you a coffee!")
                self.water -= self.coffees[name_of_coffee]["water"]
                self.milk -= self.coffees[name_of_coffee]["milk"]
                self.coffee_beans -= self.coffees[name_of_coffee]["coffee beans"]
                self.cups -= 1
                self.money += self.coffees[name_of_coffee]["money"]

    def fill_water(self, water):
        self.water += water

    def fill_milk(self, milk):
        self.milk += milk

    def fill_coffee_beans(self, coffee_beans):
        self.coffee_beans += coffee_beans

    def fill_cups(self, cups):
        self.cups += cups


def coffee_machine(action):
    """Reads one option from the standard input"""
    if action == BUY:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        answer = input()
        if answer != "back":
            machine.make_coffee(answer)
    elif action == FILL:
        print("\nWrite how many ml of water do you want to add:")
        machine.fill_water(int(input()))
        print("Write how many ml of milk do you want to add:")
        machine.fill_milk(int(input()))
        print("Write how many grams of coffee beans do you want to add:")
        machine.fill_coffee_beans(int(input()))
        print("Write how many disposable cups of coffee do you want to add:")
        machine.fill_cups(int(input()))
    elif action == TAKE:
        print(f"\nI gave you ${machine.take_money()}")
    elif action == REMAINING:
        print(machine)


# Starting the program
machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    print("\nWrite action (buy, fill, take, remaining, exit):")
    chosen_action = input()
    if chosen_action == EXIT:
        break
    else:
        coffee_machine(chosen_action)
