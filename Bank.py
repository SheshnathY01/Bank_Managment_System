from Customer import Customer   
from datetime import datetime
from validation import *
import random
import csv 
from pymongo import MongoClient                  

class Bank:

    def __init__(self, bank_name, initials, address, phone_nos, branch, ifsc_code, email, micr_code):
        
        self.bank_name = bank_name 
        self.initials = initials
        self.address = address 
        self.phone_nos = phone_nos
        self.branch = branch
        self.ifsc_code = ifsc_code
        self.email = email
        self.micr_code = micr_code
        self.customers = []

        # Mongo connection

        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["bank_db"]
        self.collection = self.db["customers"]

    def new_customer(self, name):
        customer = {"name": name}
        self.customers.append(customer)
        with open("customer.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["name"])
            writer.writeheader()
            writer.writerow(self.customers)

            self.collection.insert_one(customer)

    def __repr__(self):
        return f"{self.bank_name} ({self.ifsc_code})"
    
    @classmethod
    def generate_id(cls, length=8):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def generate_acc_no():
        length = random.randint(10, 16)  # random length between 10–16
        return ''.join(str(random.randint(0, 9)) for _ in range(length))
    
    def create_customer(self, first_name, middle_name, last_name, customer_id, dob,account_no, email, phone,address, aadhaar_no, pan_no, balance):
        if not all([first_name, last_name, customer_id, dob, account_no, email, phone, address, aadhaar_no, pan_no]):
         raise ValueError("All required fields must be provided")
    
        new_customer = Customer(
            first_name,
            middle_name,
            last_name,
            customer_id,
            dob,
            account_no,
            email,
            phone,
            address,    
            aadhaar_no,
            pan_no,
            balance
    )
        self.customers.append(new_customer)
        return new_customer

    def find_customer_by_id(self, customer_id):  
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise ValueError("Customer id not found")  

    def find_customer_by_account_no(self, account_no):
        for customer in self.customers:
            if customer.account_no == account_no:
                return customer
        raise ValueError("Customer Account no not found")        

    def filter_customer(self, first_name):
        return [customer for customer in self.customers if customer.first_name == first_name]
    
    def delete_customer(self, customer_id):
        self.customers = [customer for customer in self.customers if customer_id != customer_id]

    def get_all_customer(self):
        return self.customers
    
    def get_total_balance(self):
        total = 0
        for customer in self.customers:
            if customer.active:
                total += customer.balance
        return total
