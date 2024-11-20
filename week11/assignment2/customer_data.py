import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

class CustomerManager:
    def __init__(self, filepath):
        self.customers = []
        self.load_data(filepath)
    
    def load_data(self, filepath):
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['PurchaseAmount'] = float(row['PurchaseAmount'])
                self.customers.append(row)
    
    def filter_high_spenders(self, threshold):
        high_spenders = [cust for cust in self.customers if cust['PurchaseAmount'] > threshold]
        return high_spenders
    
    def calculate_average_purchase(self):
        total_amount = sum(cust['PurchaseAmount'] for cust in self.customers)
        return total_amount / len(self.customers) if self.customers else 0
    
    def find_inactive_customers(self, months=6):
        cutoff_date = datetime.now() - relativedelta(months=months)
        inactive_customers = [
            cust for cust in self.customers
            if datetime.strptime(cust['PurchaseDate'], '%Y-%m-%d') < cutoff_date
        ]
        return inactive_customers
    
    def save_filtered_data(self, high_spenders, inactive_customers, filename='filtered_customer_data_2.csv'):
        fields = ['CustomerID', 'Name', 'Email', 'PurchaseAmount', 'PurchaseDate']
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(high_spenders)
            writer.writerows(inactive_customers)

# Usage example (assuming the file path and other details are correct):
cm = CustomerManager("week11/assignment2/Costum_data.csv")
high_spenders = cm.filter_high_spenders(500)
average_purchase = cm.calculate_average_purchase()
inactive_customers = cm.find_inactive_customers()
cm.save_filtered_data(high_spenders, inactive_customers)


counter = 0
for spender in high_spenders:
    if counter == 10:
        break
    print(spender, "\n")
    counter += 1


print(f"The average_purchase amount is : {average_purchase}")


counter = 0
for spender in high_spenders:
    if counter == 10:
        break
    print(f"{spender['Name']}'s last purchase was made on {spender['PurchaseDate']}", "\n")
    counter += 1
    
