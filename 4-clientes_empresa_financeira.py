## First lvl

class Client:
    def __init__(self, id_number, name, age, year_salary, date_of_birth, creation_date):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.year_salary = year_salary
        self.date_of_birth = date_of_birth
        self.creation_date = creation_date
        #document

    def info_client(self):
        print(f'ID: {self.id_number}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Year salary: $ {self.year_salary:.2f}')
        print(f'Date of birth: {self.date_of_birth}')
        print(f'Creation date: {self.creation_date}\n')

## Second lvl

class Account:
    def __init__(self, client: Client, balance: float):
        self.client = client
        self.balance = balance
        # account_number
        # password
        # creation_date

class CheckingAccount(Account):
    def __init__(self, client: Client, balance: float):
        super().__init__(client, balance)
        self.type = 'checking'

    def show_account(self):
        self.client.info_client()
        print(f'Account type: {self.type}\n')
        print(f'[ID: {self.client.id_number}] {self.type} account balance: $ {self.balance:.2f}\n')

class SavingsAccount(Account):
    def __init__(self, client: Client, balance: float):
        super().__init__(client, balance)
        self.type = 'savings'

    def show_account(self):
        self.client.info_client()
        print(f'Account type: {self.type}\n')
        print(f'[ID: {self.client.id_number}] {self.type} account balance: $ {self.balance:.2f}\n')

## Third lvl

class SpecialAccount(CheckingAccount):
    def __init__(self, client: Client, balance: float, discount: int, membership: str):
        super().__init__(client, balance)
        self.discount = discount
        self.membership = membership

    def show_info(self):
        self.show_account()
        print(f'[ID: {self.client.id_number}] has {self.membership} membership.')
        print(f'[ID: {self.client.id_number}] has {self.discount}% discount on all products.')

##### Creating Client Class(es)

client_1 = Client(0, 'Leonardo Coutinho dos Santos', 28, 18573.00, '08-05-1997', '12-12-2007')
client_2 = Client(1, 'Garcia Martin Marquez', 52, 32444.78, '12-12-1974','24-07-2014' )

print('------> Client 1: \n')
client_1.info_client()

print('------> Client 2: \n')
client_2.info_client()

##### Creating client_1 checking & Savings Account's Class(es)

checking_account_1 = CheckingAccount(client_1, 1200)
savings_account_1 = SavingsAccount(client_1, 10000)

##### Creating client_2 checking & Savings Account's Class(es)

checking_account_2 = CheckingAccount(client_2, 2400)
savings_account_2 = SavingsAccount(client_2, 6000)

print('------> client_1 checking: \n')
checking_account_1.show_account()

print('------> client_1 savings: \n')
savings_account_1.show_account()

print('------> client_2 checking: \n')
checking_account_2.show_account()

print('------> client_2 savings: \n')
savings_account_2.show_account()

##### Creating client_1 ClientGold Class

client_platinum_1 = SpecialAccount(client_1, checking_account_1.balance, 25, 'platinum')

print('------> client_1 client PLATINUM account: \n')
client_platinum_1.show_info()
