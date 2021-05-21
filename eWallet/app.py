from models import *
from datetime import datetime

db.connect()

def signup():
	username = input("Create username: ")
	password = input("Create password: ")

	exists = len(User.select().where(User.username == username))

	if exists == 0:
		User.create(username=username, password=password)
		print("Signed up successfully!")
	else:
		print("Username already Exists! Use another username.")


def login():
	username = input("Enter username: ")
	password = input("Enter password: ")

	user = User.select().where(User.username == username)

	if len(user):
		user = user[0]

		if user.password == password:
			print("\nLogin successfull!")
			return user
		else:
			print("Invalid password!")
	else:
		return None


def create_wallet(user):
	name = input("Enter Wallet Name: ")
	bal = float(input("Enter starting balance: "))
	wallet = Wallet.create(name=name, balance=bal, owner=user, last_transaction=datetime.now())
	print("Wallet created successfully!")


def check_balance(user):
	wallets = user.wallets

	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)


def add_transaction(user):
	wallets = user.wallets

	for wallet in wallets:
		print(wallet.id, wallet.name, wallet.balance)

	ch = int(input("Choose a Wallet ID: "))

	wallet = Wallet.get(Wallet.id == ch)
	is_expense = int(input("\nChoose Type of Transaction:\n 0. Income\n 1. Expense\n-->"))

	if not is_expense:
		from_person = input("Enter that person name: ")
	else:
		 from_person = "None"

	trans_name = input("Enter the name: ")
	amount = float(input("Enter the amount: "))
	comment = input("Enter the description: ")

	if not is_expense:
		wallet.balance +=amount
	else:
		if amount > wallet.balance:
			print("Balance not sufficient!")
			return 1
		else:
			wallet.balance -= amount

	wallet.save()

	Transaction.create(owner=user,
		wallet=wallet,
		name=trans_name,
		amount= amount,
		timestamp = datetime.now(),
		comment = comment,
		is_expense = bool(is_expense),
		from_person = from_person)


def see_transaction(user):
	trans = user.expenses

	for txn in trans:
		if txn.is_expense:
			print(txn.wallet, txn.name, f"-{txn.amount}", txn.timestamp)
		else:
			print(txn.wallet, txn.name, f"+{txn.amount}", txn.timestamp)
