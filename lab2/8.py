class Bank:
    def __init__(self, balance: int):
        self.balance = balance

    def add_money(self, money: int):
        self.balance += money

    def withdraw_money(self, money: int):
        self.balance -= money

    def convert_to_usd(self):
        self.balance /= 463
    def convert_to_tenge(self):
        self.balance *= 463


operation = Bank(int(input('Enter your balance \n')))



app = True

while app:
    action = int(input('If you want add money click 1 \n'
                   'If you want withdraw money click 2 \n'
                   'If you want convert to Usd click 3 \n'
                   'If you want close click 0 \n'))
    if action == 1:
        operation.add_money(int(input('Add money \n')))
        print(operation.balance)
        print('\n')
    elif action == 2:
        operation.withdraw_money(int(input('Withdraw money \n')))
        print(operation.balance)
        print('\n')
    elif action == 3:
        operation.convert_to_usd()
        print(f'{round(operation.balance, 2)}$')
        operation.convert_to_tenge()
        print('\n')
    elif action == 0:
        app = False
    else:
        print('Problem 404. Check your internet connection! :( ')
        app = False

print('Good Bye!')



