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

# List
con = False
line = "======================"
n = int(input("ใส่จำนวนสินค้า = "))
List = []
for i in range(n):
  x = float(input("ราคา ="))
  List.append(x)

sum = 0
for x in List:
  sum += x
avg = sum / n

maxy = int(max(List))
minny = int(min(List))

if maxy == minny: 
  con = True

print(line)
print("avg = ", (avg))
if con:
  print("ราคาเท่ากัน =  ",min(List))
else:
  print("max =  ",max(List))
  print("min =  ",min(List))

print(line)


# IF_Meter
open, khmr, quer = False, False, False  #เปิดปิดเงื่อนไข

quet = input("A = ถามราคา, B = คำนวณค่ามีเตอร์ โปรดระบุ : ") # Create a Quest
if quet == 'A' : # if input 'A' quer = True
  quer = True
elif quet == 'B':
  khmr = True
else:
  print("คุณต้องใส่ A หรือ B")
#########################################
if quer :
  print("\n- ระยะทาง 1 กิโลเมตรแรก คิดค่าโดยสาร 35 บาท \n- ระยะทางกิโลเมตรที่ 1 - 10 กิโลเมตรละ 5.5 บาท \n- ระยะทางกิโลเมตรที่ 10-20 กิโลเมตรละ 6.50 บาท\n- ระยะทางกิโลเมตรที่ 20-40 กิโลเมตรละ 7.50 บาท\n- ระยะทางกิโลเมตรที่ 40-60 กิโลเมตรละ 8 บาท\n- ระยะทางกิโลเมตรที่ 60-80 กิโลเมตรละ 9 บาท\n- ระยะทางเกินกว่า 80 กิโลเมตรขึ้นไป กิโลเมตรละละ 10.50 บาท")
  quer = False
elif khmr :
  khm = int(input("ใส่ระยะทาง (กิโลเมตร) = "))
  khmr = False
  price = 0

  if khm == 0:
    open = True # 0 khm
  else:
    if khm == 1:
      price += 35
    else:
      if khm >= 2 and khm <= 10:
        price = khm * 5.5
      elif khm >= 11 and khm <= 20:
        price = khm * 6.50
      elif khm >= 21 and khm <= 40:
        price = khm * 7.50
      elif khm >= 41 and khm <= 60:
        price = khm * 8
      elif khm >= 61 and khm <= 80:
        price = khm * 9
      else:
        price = khm * 10.50
      price += 35 # 1khm = 35 bth
###############################################
  if open : # 0 khm
    price = price

  print("\nค่าโดยสารที่ต้องจ่าย : ",price," bth")