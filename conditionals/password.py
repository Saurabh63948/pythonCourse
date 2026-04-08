# Password length ≥ 8
# At least 1 uppercase letter (A–Z)
# At least 1 lowercase letter (a–z)
# At least 1 digit (0–9)
# At least 1 special character (like @ # $ % &)


def password_strength():
    isUpperCase = False
    isLowerCase = False
    isDigit = False
    isSpecialCharacter = False
    user_password=input("Enter your password")
    
    #loop
    for char in user_password:
        if char.isupper():
            isUpperCase=True
        elif char.islower():
            isLowerCase=True
        elif char.isdigit():
            isDigit=True
        elif char.isalnum():
            isSpecialCharacter=True       

    #check condtitons
    if(len(user_password) >= 8 and isUpperCase and isLowerCase and isDigit and isSpecialCharacter):print("Strong Password") 
    else:
        print("Week password") 

    if len(user_password) < 8:
            print("- Password length should be at least 8")
    if not isUpperCase:
            print("- Missing uppercase letter")
    if not isLowerCase:
            print("- Missing lowercase letter")
    if not isDigit:
            print("- Missing digit")
    if not isSpecialCharacter:
            print("- Missing special character")                

password_strength()            