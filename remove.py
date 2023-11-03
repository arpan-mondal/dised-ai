# Function to remove a user's AI service listing
def remove_user_ai_service(user_address, api_name):
    if active_user in user_owned_services and api_name in user_owned_services[active_user]:
        del user_owned_services[active_user][api_name]
        print(f"Removed AI service: {api_name} from your listings.")
    else:
        print("AI service not found in your listings.")

# Function to display a summary of the user's activities
def view_user_summary(user_address):
    print(f"Summary of activities for {user_address}:")
    print(f"Owned AI Services:")
    if user_address in user_owned_services:
        for api_name, price in user_owned_services[user_address].items():
            print(f"{api_name}: {price} ALGO")
    print(f"Balance: {check_balance(user_address)} microALGO")
    print("Transaction History:")
    for transaction in transaction_history:
        if transaction['sender'] == user_address or transaction['recipient'] == user_address:
            print(f"{transaction['sender']} -> {transaction['recipient']} ({transaction['amount']} ALGO)")

# Updated user interface with AI service removal and summary view
def user_interactions_updated_with_removal():
    while True:
        if active_user:
            print(f"Logged in as: {active_user}")
        else:
            print("Not logged in")

        print("1. Browse AI services")
        print("2. Purchase AI services")
        print("3. List AI services")
        print("4. Check owned AI services")
        print("5. Check balance")
        print("6. View transaction history")
        print("7. List your AI services")
        print("8. Remove your AI service")
        print("9. View user summary")
        print("10. View all AI services in the marketplace")
        print("11. Login")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_ai_catalog()
        elif choice == "2":
            if active_user:
                api_name = input("Enter the name of the AI API you want to purchase: ")
                purchase_and_track_api(user_address, api_name, ai_api_catalog.get(api_name, 0))
            else:
                print("You need to log in to make a purchase.")
        elif choice == "3":
            if active_user:
                api_name = input("Enter the name of the AI API to list: ")
                price = int(input("Enter the price in ALGO: "))
                list_ai_service(api_name, price)
            else:
                print("You need to log in to list an AI service.")
        elif choice == "4":
            if active_user:
                check_user_owned_services(user_address)
            else:
                print("You need to log in to check owned services.")
        elif choice == "5":
            if active_user:
                check_balance(user_address)
            else:
                print("You need to log in to check your balance.")
        elif choice == "6":
            if active_user:
                view_transaction_history(user_address)
            else:
                print("You need to log in to view your transaction history.")
        elif choice == "7":
            if active_user:
                print(f"User-owned AI services for {active_user}:")
                if active_user in user_owned_services:
                    for api_name, price in user_owned_services[active_user].items():
                        print(f"{api_name}: {price} ALGO")
                else:
                    print("You have no AI services listed.")
            else:
                print("You need to log in to list your AI services.")
        elif choice == "8":
            if active_user:
                api_name = input("Enter the name of the AI API you want to remove: ")
                remove_user_ai_service(user_address, api_name)
            else:
                print("You need to log in to remove your AI services.")
        elif choice == "9":
            if active_user:
                view_user_summary(user_address)
            else:
                print("You need to log in to view your summary.")
        elif choice == "10":
            view_all_ai_services()
        elif choice == "11":
            if not active_user:
                login_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Simulate user interactions with AI service removal and summary view
user_interactions_updated_with_removal()
