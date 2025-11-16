import re
from datetime import datetime

class Validator:

    @staticmethod
    def valid_email(email):
        email_regex = re.compile(r"(^[a-zA-Z_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        match = email_regex.search(email)
        if match:
            return True
        return False

    @staticmethod
    def valid_phone_no(phone):
        phone_regex = re.compile(r"^\+?91\s?\d{10}$")
        match = phone_regex.search(phone)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_aadhaar_no(aadhaar_no):
        aadhaar_no_regex = re.compile(r"^[2-9][0-9]{3}\s[0-9]{4}\s[0-9]{4}$")
        aadhaar_no = aadhaar_no.strip()
        match = aadhaar_no_regex.search(aadhaar_no)
        if match:
            return True
        return False

    @staticmethod
    def valid_pan_no(pan_no):
        pan_no_regex = re.compile(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
        match = pan_no_regex.search(pan_no)
        if match:
            return True
        return False

    @staticmethod
    def valid_first_name(first_name):
        first_name_regex = re.compile(r"^[A-Za-z]+$")
        match = first_name_regex.search(first_name)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_middle_name(middle_name):
        middle_name_regex = re.compile(r"^[A-Za-z]+$")
        match = middle_name_regex.search(middle_name)
        if match:
            return True
        return False

    @staticmethod
    def valid_last_name(last_name):
        last_name_regex = re.compile(r"^[A-Za-z]+$")
        match = last_name_regex.search(last_name)
        if match:
            return True
        return False

    @staticmethod
    def valid_dob(dob):
        try:
            dob_date = datetime.strptime(dob, "%d/%m/%Y")
            return dob_date < datetime.now()  
        except ValueError:
            return False


    @staticmethod
    def valid_account_no(account_no):
        account_no_regex = re.compile(r"^\d{10,16}$")
        match = account_no_regex.search(account_no)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_customer_id(customer_id):
        customer_id_regex = re.compile(r"^CUST\d{3}$")
        match = customer_id_regex.search(customer_id)
        if match:
            return True
        return False

    @staticmethod
    def valid_balance(balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            return True
        return False

    @staticmethod
    def valid_ifsc_code(ifsc_code):
        ifsc_code_regex = re.compile(r"^[A-Z]{4}0[A-Z0-9]{6}$")
        match = ifsc_code_regex.search(ifsc_code)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_pin_code(pin_code):
        pin_code_regex = re.compile(r"^\d{6}$")
        match = pin_code_regex.search(pin_code)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_bank_name(bank_name):
        bank_name_regex = re.compile(r"^[A-Za-z\s]+$")
        match = bank_name_regex.search(bank_name)
        if match:
            return True
        return False

    @staticmethod
    def valid_branch_name(branch_name):
        branch_name_regex = re.compile(r"^[A-Za-z\s]+$")
        match = branch_name_regex.search(branch_name)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_city(city):
        city_regex = re.compile(r"^[A-Za-z\s]+$")
        match = city_regex.search(city)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_country(country):
        country_regex = re.compile(r"^[A-Za-z\s]+$")
        match = country_regex.search(country)
        if match:
            return True
        return False
    
    @staticmethod
    def valid_street(street):
        street_regex = re.compile(r"^[A-Za-z0-9\s,.-]+$")
        match = street_regex.search(street)
        if match:
            return True
        return False

    @staticmethod
    def valid_address(address):

        required_fields = ["street", "city", "pin_code", "country"]
        for field in required_fields:
            if field not in address:
                return False
        if not Validator.valid_street(address["street"]):
            return False
        if not Validator.valid_city(address["city"]):
            return False
        if not Validator.valid_pin_code(address["pin_code"]):
            return False
        if not Validator.valid_country(address["country"]):
            return False
        return True
    
    



