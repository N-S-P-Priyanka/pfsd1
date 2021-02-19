class BankAccount:
 def __init__(a,acc_no,acc_holder,acc_type,ph_no):
   a.acc_no=acc_no
   a.acc_holder=acc_holder
   a.acc_type=acc_type
   a.ph_no=ph_no
class MobileBankAccount(BankAccount):
 def __init__(m,acc_no,acc_holder,acc_type,ph_no,MobAcc_no):
   super().__init__(acc_no,acc_holder,acc_type,ph_no)
   m.MobAcc_no=MobAcc_no
 def display_B():
   print("MobileBankAccount number : ",MobAcc_no)
class InternetBankAccount(MobileBankAccount):
 def __init__(i,acc_no,acc_holder,acc_type,ph_no,MobAcc_no,balance):
   super().__init__(acc_no,acc_holder,acc_type,ph_no,MobAcc_no)
   i. balance = balance
 def display_C():
   print("Balance InternetBankAccount : ",balance)
if __name__=='__main__':
 obj=InternetBankAccount(1234567890,'Priyanka','Savings',9999999999,650000,25000)
 print("Account Details")
 print("Account Number : ",obj.acc_no)
 print("holder Name: ",obj.acc_holder)
 print("Type :",obj.acc_type)
 print("Phone no. : ",obj.ph_no)
 print("MobileBank number : ",obj.MobAcc_no)
 print("Balance  : ",obj.balance)