import csv
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Initialize the class
class CustomerManager:
    def __init__(self, filename):
        self.filename = filename
        self.customers = []
        self.load_data()

    # Define function to load the dataset from the file
    def load_data(self):
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert PurchaseAmount to float and PurchaseDate to a datetime object
                    row['PurchaseAmount'] = float(row['PurchaseAmount'])
                    row['PurchaseDate'] = datetime.strptime(row['PurchaseDate'], '%Y-%m-%d')
                    self.customers.append(row)
        except Exception as e:
            print(f"Error loading file: {e}")

    # Define function to display customers who purchase more than $500
    def display_high_spenders(self, threshold=500):
        high_spenders = [c for c in self.customers if c['PurchaseAmount'] > threshold]
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
        inactive_customers = [cust for cust in self.customers if cust['PurchaseDate'] < cutoff_date]
        for cust in inactive_customers:
            print(f"{cust['Name']} (Last Purchase: {cust['PurchaseDate'].date()})")
        return inactive_customers

    # Define function to save filtered data
    def save_filtered_data(self, output_file, threshold=500, months=6):

        # Set cutoff_date as 6 months from current datetime
        cutoff_date = datetime.now() - timedelta(days=months * 30)

        # Filter customers who purchased more than 500 and and inactive for 6+ months
        filtered_customers = [
            cust for cust in self.customers
            if cust['PurchaseAmount'] > threshold and cust['PurchaseDate'] < cutoff_date
        ]

        # Save to output CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['CustomerID', 'Name', 'Email', 'PurchaseAmount', 'PurchaseDate']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
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

# Main Program Execution
if __name__ == "__main__":
    cm = CustomerManager('week11/assignment2/Costum_data.csv')

    print("Customers who made purchases above $500:")
    cm.display_high_spenders(500)

    print("\nAverage Purchase Amount:")
    cm.calculate_average_purchase()

    print("\nCustomers who has not made purchase within the last 6 months:")
    cm.find_inactive_customers()

    # Save filtered data to a new CSV
    cm.save_filtered_data('week11/assignment2/output/filtered_customer_data.csv')
