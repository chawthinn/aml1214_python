from objects import Product

def display_products(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print(str(i+1) + ". " + product.name)
    print()

def display_product(product):
    print("PRODUCT DATA")
    print("Name:\t\t\t{:s}".format(product.name))
    print("Price:\t\t\t${:.2f}".format(product.price))
    print("Discount percent:\t{:d}%".format(product.discountPercent))
    print("Discount amount:\t${:.2f}".format(product.getDiscountAmount()))
    print("Discounted price:\t${:.2f}".format(product.getDiscountedPrice()))
    print()

def main():
    print("Welcome to the Product Viewer Program!")
    print()

    # assign a tuple of Product objects
    products = (
            Product("Stanley 13 Ounce Wood Hammer", 12.99,   62),
            Product('National Hardware 3/4" Wire Nails', 5.06, 30),
            Product("Economy Duct Tape, 60 yds, Silver", 7.24, 15))
    display_products(products) # call display_products method and pass the products tuple

    while True: 
        number = int(input("Enter product number to view: "))
        print()

        selected_product = products[number-1]
        display_product(selected_product)

        choice = input("View another product? (y/n): ")
        print()
        if choice != "y": 
            print("Bye!")
            break

if __name__ == "__main__":
    main()