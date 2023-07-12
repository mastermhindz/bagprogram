if __name__ == '__main__':
   bags = []


while True:
    print(" BG'S Store Management System ")
    print("1. check Bags")
    print("2. add Bag")
    print("3. Exit")
    
    choice = input("Enter your choice [1-3]: ")

    if choice == '1':
        if bags:
            print("Bags Available ")
            for bag in bags:
                print("Brand:", bag['brand'])
                print("Price:", bag['price'])
                print("Quantity:", bag['quantity'])
                print("-------------------")
        else:
            print("No bags available yet.")
    elif choice == '2':
        try:
            brand = input("Enter bag brand: ")
            price = float(input("Enter bag price: "))
            quantity = int(input("Enter quantity available: "))

            bag = {
                'brand': brand,
                'price': price,
                'quantity': quantity
            }
            bags+= 1

            print("Bag added successfully!")

        except :
            print("Invalid input. Please enter a valid price and quantity.")
    elif choice == '3':
        print("Thank you for using the Bag Store Management System!")
        break
    else:
        print("Invalid choice. Please try again.")