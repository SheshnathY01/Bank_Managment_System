import Bank
from datetime import datetime
import re
from validation import Validator



class Customer:

    def __init__(self, first_name, middle_name, last_name, customer_id, dob, account_no, email, phone, address, aadhaar_no, pan_no, balance=0):

        if not Validator.valid_first_name(first_name):
            raise ValueError("Invalid first name. Only alphabets allowed.")
        if not Validator.valid_middle_name(middle_name):
            raise ValueError("Invalid middle name. Only alphabets allowed.")
        if not Validator.valid_last_name(last_name):
            raise ValueError("Invalid last name. Only alphabets allowed.")
        if not Validator.valid_dob(dob):
            raise ValueError("Invalid date of birth (must be past date, format DD/MM/YYYY).")
        if not Validator.valid_account_no(account_no):
            raise ValueError("Account number must be 10-16 digits.")
        if not Validator.valid_email(email):
            raise ValueError("Invalid email format.")
        if not Validator.valid_phone_no(phone):
            raise ValueError("Invalid phone number.")
        if not Validator.valid_aadhaar_no(aadhaar_no):
            raise ValueError("Invalid Aadhaar number .")
        if not Validator.valid_pan_no(pan_no):
            raise ValueError("Invalid PAN number .")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
         

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.customer_id = customer_id     
        self.dob = datetime.strptime(dob, "%d/%m/%Y")
        self.account_no = account_no   
        self.email = email
        self.phone = phone
        self.address = address                   
        self.aadhaar_no = aadhaar_no
        self.pan_no = pan_no
        self.balance = balance
        self.active = True

 
                    
    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def get_details(self):
        return {
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "customer_id": self.customer_id,
            "account_no": self.account_no,
            "email": self.email,
            "phone": self.phone,
            "balance": self.balance,
            "active": self.active
            
        }

    def edit_details(self, first_name=None, middle_name=None, last_name=None,dob=None, email=None, phone=None, address=None, balance=None):
        if first_name:
            self.first_name = first_name
        if middle_name:
            self.middle_name = middle_name
        if last_name:
            self.last_name = last_name
        if dob:
            self.dob = datetime.strptime(dob, "%d/%m/%Y")
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        if balance is not None:
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.full_name} deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{self.full_name} withdrew {amount}. Balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def close_account(self):
        if not self.active:
            print("Account already closed.")
            return
        self.active = False
        self.balance = 0
        print(f"{self.full_name}'s account has been closed.")

    
    # def valid_email_id(self, email):
    #     email_regex = re.compile(r"(^[a-zA-Z_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    #     match = email_regex.search(email)
    #     if match:
    #         return True
    #     return False
    
    # def vaild_phone_no(self, phone):
    #     phone_regex = re.compile(r"^\+?91\s?\d{10}$")
    #     match = phone_regex.search(phone)
    #     if match:
    #         return True
    #     return False
    
    # def vaild_aadhaar_no(self, aadhaar_no):
    #     aadhaar_no_regex = re.compile(r"^[2-9][0-9]{3}\s[0-9]{4}\s[0-9]{4}$")
    #     match = aadhaar_no_regex.search(aadhaar_no)
    #     if match:
    #         return True
    #     return False 
    
    # def valid_pan_no(self, pan_no):
    #     pan_no_regex = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    #     match = pan_no_regex.search(pan_no)
    #     if match:
    #         return True
    #     return False

    # def valid_first_name(self, first_name):
    #     first_name_regex = re.compile(r"^[A-Za-z]$")
    #     match = first_name_regex.search(first_name)
    #     if match:
    #         return True
    #     return False
    
    # def valid_middle_name(self, middle_name):
    #     middle_name_regex = re.compile(r"^[A-Za-z]$")
    #     match = middle_name_regex.search(middle_name)
    #     if match:
    #         return True
    #     return False
    
    # def valid_last_name(self, last_name):
    #     last_name_regex = re.compile(r"^[A-Za-z]$")
    #     match = last_name_regex.search(last_name)
    #     if match:
    #         return True
    #     return False

    # def valid_dob(self, dob):
    #     dob_regex = re.compile(r"^(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[0-2])[/-](19|20)\d\d$")
    #     match = dob_regex.search(dob)
    #     if match:
    #         return True
    #     return False
    
    




# sbi = Bank.Bank("state_bank_of_india", "sbi",
#            ["1202040232"], "dadar",
#            "SBIN0001234", "sbi@gmail.com", "0987654321")


# vedant = sbi.create_customer(
#     first_name="Vedu",
#     middle_name="Umesh",
#     last_name="Dulam",
#     customer_id="CUST001",
#     dob="31/03/2004",
#     account_no="1234567890",
#     email="vedu@gmail.com",
#     phone="9865369291",
#     aadhaar_no="123456789012",
#     pan_no="ABCDE1234F",
#     balance=2000
# )

# print.deposit(2000)
# # # # vedant.edit_details(middle_name="om")
# # # print(vedant.get_details())
        
# # print(vedant.get_details())



