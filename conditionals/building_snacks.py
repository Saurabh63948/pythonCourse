snack = ["samosa", "cookies"]

user_demand = input("Enter your snack: ").lower()

if user_demand in snack:
    print("It's confirmed, the order is placed.")
else:
    print("Snack is not available.! sorry we only serve only samosa and cookies")