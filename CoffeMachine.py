class CoffeeMachine:
    menu = {'espresso':
                {'Milk': 0,
                 'Water': 50,
                 'Coffee': 18,
                 'Price': 1.5},
            'latte':
                {'Milk': 150,
                 'Water': 200,
                 'Coffee': 24,
                 'Price': 2.5},
            'cappuccino':
                {'Milk': 100,
                 'Water': 250,
                 'Coffee': 24,
                 'Price': 3}}

    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.penny = 0
        self.nickel = 0
        self.dime = 0
        self.quarter = 0
        self.start_machine()

    def start_machine(self):
        while True:
            answer = self.initial_ask()
            self.check_resources(answer)

    def initial_ask(self):
        answer = ''
        while answer not in ('espresso', 'latte', 'cappuccino'):
            answer = input("What coffee do you want? (espresso/latte/cappuccino)\n").lower()
        return answer

    def check_resources(self, coffee):
        if (self.water - self.menu[coffee]['Water'] >= 0 and
                self.milk - self.menu[coffee]['Milk'] >= 0 and
                self.coffee - self.menu[coffee]['Coffee'] >= 0):
            self.take_coins(coffee)
        else:
            print('We are sorry but there is not enough resources at the moment')

    def make_coffee(self, coffee):
        self.water -= self.menu[coffee]['Water']
        self.milk -= self.menu[coffee]['Milk']
        self.coffee -= self.menu[coffee]['Coffee']
        print('\nBzzz, bzzz, bzzz\nEnjoy your coffee\n')

    def give_change(self, change, coffee):
        qua_need = change // 0.25
        if qua_need < self.quarter:
            self.quarter -= qua_need
            change -= qua_need * 0.25
            print('Got back ' + str(qua_need) + ' quarter/s')
        else:
            change -= self.quarter * 0.25
            print('Got back ' + str(self.quarter) + ' quarter/s')
            self.quarter = 0
        change = round(change, 2)

        dime_need = change // 0.1
        if dime_need < self.dime:
            self.dime -= dime_need
            change -= dime_need * 0.1
            print('Got back ' + str(dime_need) + ' dime/s')
        else:
            change -= self.dime * 0.1
            print('Got back ' + str(self.dime) + ' dime/s')
            self.dime = 0
        change = round(change, 2)

        nickel_need = change // 0.05
        if nickel_need < self.nickel:
            self.nickel -= nickel_need
            change -= nickel_need * 0.05
            print('Got back ' + str(nickel_need) + ' nickel/s')
        else:
            change -= self.nickel * 0.05
            print('Got back ' + str(self.nickel) + ' nickel/s')
            self.nickel = 0
        change = round(change, 2)

        penny_need = change // 0.01
        if penny_need < self.penny:
            self.penny -= penny_need
            change -= penny_need * 0.01
            print('Got back ' + str(penny_need) + ' penny/s')
        else:
            change -= self.penny * 0.01
            print('Got back ' + str(self.penny) + ' penny/s')
            self.penny = 0
        change = round(change, 2)

        if change == 0:
            self.make_coffee(coffee)

    def take_coins(self, coffee):
        price = self.menu[coffee]['Price']
        print('Order have been accept.\nPlease toss + ' + str(price) + '$')
        try:
            penny = int(input('How many pennies you give?\t'))
            nickel = int(input('How many nickels you give?\t'))
            dime = int(input('How many dimes you give?\t'))
            quarter = int(input('How many quarters you give?\t'))
        except:
            print('Incorrect data input')
            return
        self.penny += penny
        self.nickel += nickel
        self.dime += dime
        self.quarter += quarter

        if penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25 == price:
            self.make_coffee(coffee)
        elif penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25 < price:
            print('You got not enough money')
            return
        else:
            change = (penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25) - price
            self.give_change(round(change, 2), coffee)


