class Chai:
     origin ="India"

print(Chai.origin)     

Chai.is_hot =True

print(Chai.is_hot)

#creating object from class chai

masala =Chai()

print(masala.origin)
print(masala.is_hot)

masala.is_hot =False

print(f"Class : {Chai.is_hot}")
print(f"Masala : {masala.is_hot}")
masala.flavor ="Masala"

print(masala.flavor)