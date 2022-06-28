print("welcome to atm")
print("insert yout card")
lang=input("enter your language")
if lang=="english":
	bank=input("enter a account")
	if bank=="saving account":
		trans=input("enter a option")
		if trans=="withdraw":
			pin=int(input("enter your pin"))
			if pin==1234:
				amt=int(input("enter your amount"))
				a=50000
				if amt>=0 and amt<=50000:
					print("collect your cash and your current balance is",a-amt)
					b=input("enter your slip")
					if b=="yes":
						print("here is your slip")
					else:
						print("no slip save tree")
				else:
					print("insufficent balance")
			elif pin=="try again":
				print("reset your pin")
			else:
				print("incorrect pin")
		elif trans=="balance enquiry":
			print("enquiry")
			pin=int(input("enter your pin"))
			if pin==1234:
				a=50000
				if a==50000:
					print("your current balance is",a)
					b=input("enter your slip")
					if b=="yes":
						print("here is your slip")
		else:
			print("other balance")
			bank=input("enter a option")
	elif bank=="current account":
		trans=input("enter a option")
		if trans=="withdraw":
			pin=int(input("enter your pin"))
			if pin==1234:
				amt=int(input("enter your amount"))
				a=50000
				if amt>=0 and amt<=50000:
					print("collect your cash and your current balance is",a-amt)
					b=input("enter your slip")
					if b=="yes":
						print("here is your slip")
					else:
						print("no slip save tree")
				else:
					print("insufficent balance")
			elif pin=="try again":
				print("reset your pin")
			else:
				print("incorrect pin")
				
	else:
		print("error")
else:
	print("other language")