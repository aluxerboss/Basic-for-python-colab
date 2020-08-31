
# Code for Healthy
height = float(input("Enter  hight in m."))
weight = float(input("Enter  weight in m."))
bmi = weight / ((height/100)**2)
print("BMI =  {0} ".format(bmi), end='')

if ( bmi < 16):
  print (" saverely underweight ")
elif ( bmi >= 16 and bmi <18.5 ):
  print("underweight")
elif ( bmi >= 18.5 and bmi <25 ):
  print("Healthy")
elif ( bmi >= 25 and bmi <30 ):
  print("overweight")
elif ( bmi >= 30):
  print("sevrely overweight")


#Code for Sum number
numA = (float(input("Enter Number 1 :")))
numB = (float(input("Enter Number 2 :")))
numC = (float(input("Enter Number 3 :")))
sum = (numA + numB) + numC
print("ผมรวม = {0}".format(sum), end='' )


#Code for 2.Sum number
def summy(num1,num2,num3):
  numA = float(input(num1))
  numB = float(input(num2))
  numC = float(input(num3))
  sum = (numA + numB) + numC
  print("ผมรวม = {0}".format(sum), end='' )
summy("Number 1 :", "Number 2 :" , "Number 3 :")