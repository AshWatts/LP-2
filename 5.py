def pizza_chatbot():
    print("🍕 Welcome to PizzaBot!")
    
    menu = {
        '1': 'Margherita (₹199)',
        '2': 'Pepperoni (₹299)',
        '3': 'Veg Supreme (₹249)',
        '4': 'Check Order',
        '5': 'Checkout'
    }
    
    order = []
    total = 0
    
    while True:
        print("\nChoose an option:")
        for key, item in menu.items():
            print(f"{key}. {item}")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            order.append("Margherita")
            total += 199
            print("Added Margherita!")
        elif choice == '2':
            order.append("Pepperoni")
            total += 299
            print("Added Pepperoni!")
        elif choice == '3':
            order.append("Veg Supreme")
            total += 249
            print("Added Veg Supreme!")
        elif choice == '4':
            print("\nYour Order:")
            if order:
                for item in order:
                    print(f"- {item}")
            else:
                print("Your order is empty")
        elif choice == '5':
            if order:
                print("\nYour Final Order:")
                for item in order:
                    print(f"- {item}")
                print(f"\nTotal: ₹{total}")
                print("Thank you! Your pizzas will be ready in 30 minutes!")
            else:
                print("You didn't order anything!")
            break
        else:
            print("Please enter a number between 1-5")

# Start the chatbot
pizza_chatbot()