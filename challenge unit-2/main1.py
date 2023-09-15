class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance +=amount
      print("Deposite:  {}.new balance:  {}".format(amount, self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print("withdrew  {}.New balance:  {}". format(amount, self.__account_balance))
    else:
      print("Invalid withdraw amount or insufficient balance.")
  def display_balance (self):
    print("Account balance for {}(Accpount #{}:  {}".format(
    self.__account_holder_name, self.__account_number,
    self.__account_balance))
    #create an instance of the BankAccount class
account = BankAccount(account_number="568709809",account_holder_name="Hema",initial_balance = 50000.0)
#Test deposit and withdraw functionality
account.display_balance()
account.deposit(5000.0)
account.withdraw(2000.0)
account.display_balance()
