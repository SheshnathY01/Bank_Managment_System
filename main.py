from Bank import Bank
from Customer import Customer
from validation import *
# from datetime import datetime
import re
from pprint import pprint
import json
from export import export_customer_to_csv
from pymongo import MongoClient


cbi = Bank("Central_Bank_of_India", "cbi",{"street": "Andheri", "city": "Mumbai", "pin_code": "400093", "country": "India"},["1202040232"], "dadar", "SBIN0001234", "sbi@gmail.com", "0987654321")


sheshnath = cbi.create_customer(

    first_name="Shesh",
    middle_name="Nandlal",
    last_name="Yadav",
    customer_id="CUST001",
    dob="22/04/2005",
    account_no=Bank.generate_acc_no(),
    email="shes@gmail.com",
    address={"street": "Andheri", "city": "Mumbai", "pin_code": "400093", "country": "India"},
    phone="+918879159241",
    aadhaar_no="2345 6789 0123",
    pan_no="ABCDE1234F",
    balance=5000
)

# print(vedant.get_details())
# vedant.deposit(2000)
# vedant.withdraw(500)
# print("Balance:", vedant.get_balance())
# vedant.close_account()

# print(sbi.customers)
# print(sbi)
# vedant.edit_details(middle_name = "Daddy")
# print(vedant.get_details())

# print(vedant.valid_dob("31/03/2004"))
# vedant.edit_details(email=  "vedantdulam@gmail.com")
# print(vedant.get_details())
# # print(vedant.vaild_phone_no("+918169sd5410"))
# print(vedant.vaild_aadhaar_no("2345 6789 1234"))
# print(vedant.valid_pan_no("ABCDE1234A"))


# print("Customer details:", vedant.get_details())
# print("All customers:", sbi.get_all_customer())
# print("Total balance in bank:", sbi.get_total_balance())


# vedant = Customer(
#     first_name="Vedant",
#     middle_name="Umesh",
#     last_name="Dulam",
#     customer_id="CUST001",
#     dob="31/03/2004",
#     account_no=Bank.generate_acc_no(),
#     email="vedu@gmail.com",
#     address={"street": "ghatkopar", "city": "Mumbai", "pin_code": "400083", "country": "India"},
#     phone="+919876543210",
#     aadhaar_no="2345 6789 1234",
#     pan_no="ABCDE1234F",
#     balance=5000
# )

# pprint(sheshnath.get_details())

pprint("Customer created successfully!")
export_customer_to_csv

# Connect to local MongoDB server

client = MongoClient("mongodb://localhost:27017/")





# pprint("✅ Customer created successfully!")
































































































































# from Bank import Bank
# from Customer import Customer
# from validation import *
# import re
# from pprint import pprint
# import json

# cbi = Bank(
#     "Central Bank of India",
#     "CBI",
#     "Andheri, Mumbai",
#     ["1531561362"],
#     "Andheri Branch",
#     "CBIN0001234",
#     "cbi@gmail.com",
#     "400002345"
# )

# sheshnath = cbi.create_customer(
#     first_name="Shes",
#     middle_name="Nandlal",
#     last_name="Yadav",
#     customer_id="CUST005",
#     dob="22/04/2005",
#     account_no="1531561362",
#     email="yadavsheshnath@gmail.com",
#     phone="+918879159241",
#     address="Shree Sai Ganesh, Room No-106, R-11, Poonam Nagar, Andheri (East), Mumbai - 400093",
#     aadhaar_no="394905900590",
#     pan_no="ABCDE1234F",
#     balance=7000
# )

# print(sheshnath.get_details())
# sheshnath.deposit(2000)
# sheshnath.withdraw(500)
# print("Balance:", sheshnath.get_balance())
# sheshnath.close_account()


# # b = Bank()
# # b.add_customer("Sheshnath", "123456789012")
# # b.add_customer("Aashis", "123456789013")

# # print(is_valid_first("Sheshnath"))
# # print(is_valid_middle("Nandlal"))
# # print(is_valid_last("Yadav"))
# # print(is_valid_customer("Aashis"))
# # print(is_valid_Dob("22/040/2205"))
# # print(is_valid_account("12345679"))
# # print(is_valid_email("yadavsheshnat@gmail.com"))
# # print(is_valid_phone("+918879159241"))
# # print(is_valid_aadhaar("3639154234"))
# # print(is_valid_pan("XY12455"))
# # print(is_valid_balance(10000))



# # sheshnath.edit_details(middle_name="Daddy")
# # print(sheshnath.get_details())

# # print("All customers:", cbi.get_all_customer())
# # print("Total balance in bank:", cbi.get_total_balance())
