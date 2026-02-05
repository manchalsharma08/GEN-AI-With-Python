# Addition 
a = 10
b = 20
c = a + b
print(c)

# Type of Data Show
a = "my name manchal"
print(a)

b=a
print(b)

b= 3
print(b)

# string

line = "manchal's son is yadvik"
z = line
print(z)

# for Function

name = "AI"
for i in range(3):
 print(name)


# write a Table of 2
print("## 01")
for i in range(1,11):
  print("2x",i,"=",2*i)

print("## 02")
print("## Takeing input from User")

Table = int(input("Enter Number: "))
for i in range(1,11):
  print(Table,"x",i,"=",Table*i)

print("## 03")
print("## While loop Function for Table Write")

i = 1
while i <= 10:
  print("2x",i,"=",2*i)
  i += 1

def table_of_2():
    for i in range(1, 11):
        print("2 x", i, "=", 2 * i)

print("## 04")
print("## Function [def] Defination with for looping ")
def table_of_2():
    for i in range(1,11):
       print("2x",i,"=",2*i)

table_of_2()

print("## 04.01")
print("## Function [def] Defination with for looping ")
def table_of_2(n):
    for i in range(1,11):
       print(n,"x",i,"=",n*i)

table_of_2(4)


print("## Create A file and something write on it")
print("01 type")

f= open("text.txt", "w")
f.write("Hello World")
f.closed

print("===================")
print("02 type" \
"\n====================")

with open("mytext.txt", "w") as f:
   f.write("MAnchal")

print("03 type" \
" \nOnly Create file not write any thing"
"\n====================")

open("hello.txt", "w").close()

print("04 type" \
" \n Append data (don’t delete old content)"
"\n====================")

with open("text.txt", "a") as f:
 f.write("\n My world is My feamily"
         "\n hi hello1")

print("05 type" \
" \nOnly Create file not write any thing"
"\n====================")

open("hello.py", "w").close()



print("================")
print(" Check file location ")
import os
print(os.getcwd())



with open("E:\GenAI\GEN-AI-With-Python\Practice\Day02_0402026\world.py", "w") as f:
    f.write('with open("write.txt", "w") as f:\n')
    f.write('    f.write("hum")')


