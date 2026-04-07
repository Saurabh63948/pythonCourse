# snack = ["samosa", "cookies"]

# user_demand = input("Enter your snack: ").lower()

# if user_demand in snack:
#     print("It's confirmed, the order is placed.")
# else:
#     print("Snack is not available.! sorry we only serve only samosa and cookies")


# You are building a small billing system for a grocery shop.
# def grocery_shop():
#     total = 0
#     items_dict = {}  # store item and price

#     while True:
#         item = input("Enter item name (type 'done' to stop): ")
#         if item == "done" or item == "stop":
#             break
#         price = float(input("Enter the price of item: "))
#         items_dict[item] = price
#         total += price
#     print("\n--- BILL SUMMARY ---")
#     for item, price in items_dict.values():
#         print(f"{item}: {price}")
#     print(f"\nTotal before discount: {total}")
#     if total > 1000:
#         discount = total * 0.10
#         total -= discount
#         print(f"Discount applied: {discount}")
#     print(f"Final amount: {total}")
# grocery_shop()
