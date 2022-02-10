'''
1.What are User Defined Exception:
    Programmers may name their own exceptions by creating a new exception class. Exceptions need to
    be derived from the Exception class, either directly or indirectly. Although not mandatory, most of the exceptions are
    named as names that end in “Error” similar to the naming of the standard exceptions in python


'''

# Example:
#
# class BalanceCheckError(Exception):
#     pass
#
# def checkBalance():
#     money=int(input("Enter The Money"))
#     withdraw=int(input("Enter money to withdraw"))
#     balance=money-withdraw
#     if(balance<2000):
#         print("Your Current Balance is=", money)
#         raise BalanceCheckError("As per the Minimum Balance Policy, Balance must be at least 2000 "
#                                 "This Transaction Could Not Be Proceeded")
#     print("Your Withdrawal Of ",withdraw,"Completed Successfully.........")
#     print("Your Current balance is =",balance)
#
# try:
#     checkBalance()
#
# except BalanceCheckError as  be:
#     print(be)
#
# finally:
#     print("program terminates normally")


# class MinimumDepositError(Exception):
#     pass
# class MinimumBalanceError(Exception):
#     pass
# def Bank_ATM(balance,choice,amount):
#     if(balance<500):
#         raise ValueError(“As per the Minimum Balance Policy, Balance must be at least 500”)
#     if(choice == 1 and amount<2000):
#         raise MinimumDepositError(“The Minimum amount of Deposit should be 2000.”)
#     elif(choice == 1):
#         balance+=amount
#         print(“Updated Balance Amount:  “+str(balance))
#
#     if(choice == 2 and balance-amount<500):
#         raise MinimumBalanceError(“You cannot withdraw this amount due to Minimum Balance Policy”)
#     elif(choice ==2):
#         balance-=amount
#         print(“Updated Balance Amount:  “+str(balance))



# total_amount = 10000
# withdraw = int(input("enter the amount to withdraw: "))
# try:
#     bal = total_amount - withdraw
#     if bal <= 2000:
#         e = Exception()
#         raise e
# except Exception as e:
#     print("low minimum balance")
# else:
#     print("please collect your cash")
# finally:
#     print("program terminates normally")


# class BankException(Exception):
#
#     def __init__(self,bal, message="Balance is not sufficient"):
#         self.bal = bal
#         self.message = message
#         super().__init__(self.message)
#
#
# balance = 5000
# withDrawAmount = int(input("Enter the amount to withdrawn: "))
#
# try:
#     if withDrawAmount > balance:
#         raise BankException(withDrawAmount)
#     else:
#         print("Updated balance is: ", balance - withDrawAmount)
# except BankException as e:
#     print(e)
# except Exception as e:
#     raise


class UnderageException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class OverageException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

a = int(input("enter the age: "))
try:
    if a < 18:
        e = UnderageException("you are under age to apply for DL")
        raise e

    elif a > 60:
        e = OverageException("you are over age to apply for DL")
        raise e

except UnderageException as e:
    print(e)
except OverageException as e:
    print(e)
else:
    print("you are eligible to apply for DL")
finally:
    print("Thank you")

