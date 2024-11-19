import csv
from datetime import datetime, timedelta

class CustomerManager:
    def __init__(self, filename):
        self.filename = filename
        self.customers = []
        self.load_data()

    def load_data(self):
        """Load data from the CSV file into a list of dictionaries."""
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

    def display_high_value_customers(self, threshold=500):
        """Display customers who made purchases above the given threshold."""
        high_value_customers = [c for c in self.customers if c['PurchaseAmount'] > threshold]
        for customer in high_value_customers:
            print(f"{customer['Name']} (${customer['PurchaseAmount']:.2f})")

    def calculate_average_purchase(self):
        """Calculate and display the average purchase amount."""
        if not self.customers:
            print("No customer data available.")
            return
        total = sum(c['PurchaseAmount'] for c in self.customers)
        average = total / len(self.customers)
        print(f"Average Purchase Amount: ${average:.2f}")
        return average

    def find_inactive_customers(self, months=6):
        """List customers who have not made a purchase in the last X months."""
        cutoff_date = datetime.now() - timedelta(days=months*30)
        inactive_customers = [c for c in self.customers if c['PurchaseDate'] < cutoff_date]
        for customer in inactive_customers:
            print(f"{customer['Name']} (Last Purchase: {customer['PurchaseDate'].date()})")
        return inactive_customers

    def save_filtered_data(self, output_file, threshold=500, months=6):
        """Save filtered data into a new CSV file."""
        cutoff_date = datetime.now() - timedelta(days=months * 30)

        # Filter customers who are both high-value and inactive
        filtered_customers = [
            c for c in self.customers
            if c['PurchaseAmount'] > threshold and c['PurchaseDate'] < cutoff_date
        ]

        # Save to output CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['CustomerID', 'Name', 'Email', 'PurchaseAmount', 'PurchaseDate']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer in filtered_customers:
                writer.writerow({
                    'CustomerID': customer['CustomerID'],
                    'Name': customer['Name'],
                    'Email': customer['Email'],
                    'PurchaseAmount': customer['PurchaseAmount'],
                    'PurchaseDate': customer['PurchaseDate'].date()
                })
        print(f"Filtered data saved to {output_file}")



# Main Program Execution
if __name__ == "__main__":
    manager = CustomerManager('week11/assignment2/Costum_data.csv')

    print("Customers with purchases above $500:")
    manager.display_high_value_customers()

    print("\nAverage Purchase Amount:")
    manager.calculate_average_purchase()

    print("\nCustomers inactive for 6+ months:")
    manager.find_inactive_customers()

    # Save filtered data to a new CSV
    manager.save_filtered_data('week11/assignment2/output/filtered_customer_data.csv')
