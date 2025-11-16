import csv
from Bank import Bank, Customer
from datetime import datetime
import json

def export_customer_to_csv(bank):
    # Ensure 'bank' has customers
    if not hasattr(bank, "customers") or not bank.customers:
        print("No customers to export.")
        return

    with open("customers.csv", "w", newline="") as csvfile:
        # Define CSV headers
        fieldnames = [
            "first_name", "middle_name", "last_name", "customer_id", "account_no",
            "email", "phone_no", "aadhaar_no", "pan_no", "balance",
            "active", "dob", "address"
        ]
        Wariter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        Wariter.writeheader()
        for customer in bank.customers:
            Wariter.writerow({
                "first_name": customer.first_name,
                "middle_name": customer.middle_name,
                "last_name": customer.last_name,
                "customer_id":customer.customer_id,
                "account_no":customer.account_no,
                "email": customer.email,
                "phone_no": customer.phone_no,
                "aadhaar_no": customer.aadhaar_no,
                "pan_no": customer.pan_no,
                "balance": customer.balance,
                "active": customer.active,
                "dob": customer.dob.strftime("%d/%m%Y"),
                "address": customer.address,
            })


if __name__ == "__main__":
    bank = Bank() # Create an instance of Bank
    export_customer_to_csv(bank)