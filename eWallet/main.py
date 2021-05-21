from app import *

while True:
	print("----------------eWallet Management System-------------")
	print("------------------Project by Abhishek.k---------------")
	print("------------e-mail me at: abhisheku3u@gmail.com-------")
	print("---------------Contact for publishing-----------------")
	
	print("-"*20)
	print("Welcome to Fintrack", "-"*20, sep="\n")

	print("What would you like to do:\n\
		1. Login\n\
		2. Signup\n\
		3. Exit")

	choice = input("\n--> ")

	if choice == "1":
		user = login()

		while user is not None:
			print("Choose Operations:\n\
		1. Create Wallet\n\
		2. Add Transaction\n\
		3. Check Balance\n\
		4. See Transaction")

			ch = input("\n--> ")

			if ch == "1":
				create_wallet(user)
			elif ch == "2":
				add_transaction(user)
			elif ch == "3":
				check_balance(user)
			elif ch == "4":
				see_transaction(user)
			else:
				break

		else:
			print("Credentials do not match. or Create a New Account.\n")

	elif choice == "2":
		signup()
	else:
		break
