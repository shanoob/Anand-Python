class bankaccount:
 def __init__(name):
 	print name
 	name.balance=0
 def deposit(name,amount):
   name.balance=name.balance+amount
   print name,name.balance
 def withdraw(name,amount):
   name.balance=name.balance-amount
   print name.balance

shanu=bankaccount()
nettu=bankaccount()
nettu.deposit(2500)
shanu.deposit(1000)
nettu.withdraw(500)
shanu.withdraw(300)
