user_asked = input("Enter the cup size: ").lower()

if user_asked == "large":
    print("Chai price is: 20")
elif user_asked == "medium":
    print("Chai price is: 15")
elif user_asked == "small":
    print("Chai price is: 10")
else:
    print("Sorry, tea is not available in this size!")