from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_continue = True

while is_continue:
    option = menu.get_items()
    choice = input(f"Which coffee you want? ({option})")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_continue = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
