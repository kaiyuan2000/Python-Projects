from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
c_maker = CoffeeMaker()
m_machine = MoneyMachine()

is_open = True
while is_open == True:
    print("Welcome to coffee machine! ")
    choice = input(f"What would you like? ({menu.get_items()}) ? ").lower()
    #need add while loop
    if choice == "off":
         is_open = False
    elif choice == "report":
         c_maker.report()
    else:
         drink = menu.find_drink(choice)
         if c_maker.is_resource_sufficient(drink) == True:
            if m_machine.make_payment(drink.cost) == True:
                c_maker.make_coffee(drink)

print("Machine closing. ")




