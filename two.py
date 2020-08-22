#Code for Loop for

for i in range(5):
    inputname = input("Name = ")
    inputprice = float(input("Price = "))
    if inputprice >= 1000:
      discount = inputprice*(12/100)
      total = inputprice - discount
    else:
      total = inputprice

    print("=============================")
    print("ชื่อสินค้า : ",inputname)
    print("คุณได้รับส่วนลดจำนวน : ",discount)
    print("ราคาสุทธิ : ",total)
    print("=============================")

#Code for Loop While
import random

loop = 1
con_open = False
while loop < 6:
  inputname = input("Name = ")
  inputprice = float(input("Price = "))
  if inputprice >= 1000:
    con_open = True
    discount = inputprice*(12/100)
    total = inputprice - discount
  else:
    con_open = False
    total = inputprice

  if not con_open:
    bonus = random.randint(1,2)

  if con_open == True :
    print("=============================")
    print("ชื่อสินค้า : ",inputname)
    print("คุณได้รับส่วนลดจำนวน : ",discount)
    print("ราคาสุทธิ : ",total)
    print("=============================")
  else:
    print("=============================")
    print("ชื่อสินค้า : ",inputname)
    print("ราคาสุทธิ : ",total)
    if bonus == 1:
      bonus = "ขนม"
    else:
      bonus = "ปีป"
    print("คุณได้รับ : ",bonus)

    print("=============================")
  loop += 1


#Code for loop while and import
import random
import time

cat_label = {}
dis_H = (30/100)
dis_G = (20/100)
dis_O = (10/100)
breakprice = 0
wait_total = 3
con_open = False

while True:
  inputname = input("Name = ")
  inputprice = float(input("Price = "))
  inputcat = input("Catagory = ")

  if inputcat == "H":
    cat_label = "สินค้ายอดฮิต"
    con_open = True
    discount = inputprice * dis_H
    total = inputprice - discount
    if inputprice == breakprice:
      break
  elif inputcat == "G":
    cat_label = "สินค้าขายดี"
    con_open = True
    discount = inputprice * dis_G
    total = inputprice - discount
    if inputprice == breakprice:
      break
  elif inputcat == "O":
    cat_label = "สืนค้าโอท๊อป"
    con_open = True
    discount = inputprice * dis_O
    total = inputprice - discount
    if inputprice == breakprice:
      break
  else:
    con_open = False
    total = inputprice
    cat_label = "สืนค้าไม่ได้บรรจุในประเภท"
    if inputprice == breakprice:
      break

  if con_open:
    ran = random.randint(1,100)
    bonus = ran / 100

  if con_open:
    print("กรุณารอ ",wait_total," วินาที")
    time.sleep(wait_total)
    print("=============================")
    print("ชื่อสินค้า : ",inputname)
    print("ชนิดสินค้า : ",cat_label)
    print("คุณได้รับส่วนลดจำนวน : ",discount)
    print("ราคาสุทธิ : ",total)
    print("เลขเครื่องราง : ",bonus)
    print("=============================")
  else:
    print("=============================")
    print("ชื่อสินค้า : ",inputname)
    print("ชนิดสินค้า : ",cat_label)
    print("ราคาสุทธิ : ",total)


    print("=============================")

