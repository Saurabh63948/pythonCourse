class Chai:
    tempareture ="hot"
    strength ="strong"


cutting =Chai()
print(cutting.tempareture)

cutting.tempareture ="Mild"
cutting.cup ="small"
print("after changing the tempareture")
print(cutting.cup)
print(f"directly look into the class",Chai.tempareture)

del cutting.tempareture
del cutting.cup
print(cutting.tempareture)
print(cutting.cup)
