import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

# Initialize the class
class CustomerManager:
    def __init__(self, filepath):
        self.customers = []
        self.load_data(filepath)

    # Define function to load the dataset from the file
    def load_data(self, filepath):
        try:
            with open(filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try: 
                        # Validate and convert PurchaseAmount
                        row['PurchaseAmount'] = float(row['PurchaseAmount'])
                        if row['PurchaseAmount'] < 0:
                            raise ValueError("Puchase Amount should be positive.")

                        # Validate and convert PurchaseDate
                        try: 
                            row['PurchaseDate'] = datetime.strptime(row['PurchaseDate'], '%Y-%m-%d')
                        except ValueError: 
                            raise ValueError(f"Invalid date format: {row['PurchaseDate']}")

                        # Validate Email
                        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', row['Email']):
                            raise ValueError(f"Invalid email format: {row['Email']}")

                        self.customers.append(row)

                    except Exception as e:
                        print(f"Error processing row: {row}. Error: {e}")

        except Exception as e:
            print(f"Error loading file: {e}")

    # Define function to display customers who purchase above the threshold
    def display_high_spenders(self, threshold=500):
        high_spenders = [cust for cust in self.customers if cust['PurchaseAmount'] > threshold]
        for customer in high_spenders:
            print(f"{customer['Name']} (${customer['PurchaseAmount']:.2f})")

    # Define function to calculate and display average purchase amount
    def calculate_average_purchase(self):
        total = sum(cust['PurchaseAmount'] for cust in self.customers)
        average = total / len(self.customers) if self.customers else 0
        print(f"${average:.2f}")
        return average

    # Define function to filter inactive customers
    def find_inactive_customers(self, months=6):
        cutoff_date = datetime.now() - relativedelta(months=months)
        inactive_customers = [
            cust for cust in self.customers 
            if cust['PurchaseDate'] < cutoff_date
        ]
        inactive_customers.sort(key=lambda x: x['PurchaseDate'])

        for cust in inactive_customers:
            print(f"{cust['Name']} (Last Purchase: {cust['PurchaseDate'].date()})")
        return inactive_customers

    # Define function to save filtered data
    def save_filtered_data(self, output_file, threshold=500, months=6):

        # Set cutoff_date as 6 months from current datetime
        cutoff_date = datetime.now() - relativedelta(months=months)

        # Filter customers who purchased more than $500 and and inactive for 6+ months
        filtered_customers = [
            cust for cust in self.customers
            if cust['PurchaseAmount'] > threshold and cust['PurchaseDate'] < cutoff_date
        ]

        # Save to output CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            fields = ['CustomerID', 'Name', 'Email', 'PurchaseAmount', 'PurchaseDate']
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for cust in filtered_customers:
                writer.writerow({
                    'CustomerID': cust['CustomerID'],
                    'Name': cust['Name'],
                    'Email': cust['Email'],
                    'PurchaseAmount': cust['PurchaseAmount'],
                    'PurchaseDate': cust['PurchaseDate'].date()
                })
        print(f"Suceessful! Results are saved to {output_file}")

# Execute functions in Main Program
if __name__ == "__main__":
    cm = CustomerManager('week11/assignment2/Costum_data.csv')

    print("Customers who made purchases above $500:")
    high_spenders = cm.display_high_spenders(500)

    print("\nThe average_purchase amount is:")
    average_purchase = cm.calculate_average_purchase()

    print("\nCustomers who has not made purchase within the last 6 months:")
    inactive_customers = cm.find_inactive_customers(6)

    # Save filtered data to a new CSV
    cm.save_filtered_data('week11/assignment2/output/filtered_customer_data.csv', 500, 6)
