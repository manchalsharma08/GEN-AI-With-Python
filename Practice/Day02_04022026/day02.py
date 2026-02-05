x = 3
for i in range(1,11):
    print(x,"x",i,"=",x*i)

#========================================

# x = int(input("enter Number:"))
# for i in range(1,11):
#     print(x,"x",i,"=",x*i)

# #========================================

# i = 1
# x = int(input("enter Number:"))
# while i <= 10:
#     print(x,"x",i,"=",x*i)
#     i +=1

#==========================

f = open("test.txt", "w")

f.closed

#========================

f = open("test01.txt", "w")
f.write("hum aap ke hai kon")

f.closed

#===========================

# f = open("E:\GenAI\GEN-AI-With-Python\Practice\Day01_02022026\test03.txt", "w")
# f.write(" hum tumhare hai wo bhi")

# f.closed

# f = open("E:\\GenAI\\GEN-AI-With-Python\\Practice\\Day01_02022026\\test03.txt", "w")
# f.write("hum tumhare hai wo bhi")
# f.close()

# f = open("E:/GenAI/GEN-AI-With-Python/Practice/Day01_02022026/test03.txt", "w")
# f.write("hum tumhare hai wo bhi")
# f.close()

# with open(r"E:\GenAI\GEN-AI-With-Python\Practice\Day01_02022026\test03.txt", "w") as f:
#     f.write("hum tumhare hai wo bhi")

# with open(r"E:\GenAI\GEN-AI-With-Python\Practice\Day01_02022026\test04.txt", "w") as f:
#     f.write("Ye file dusre folder me bani hai")

import os

folder = r"E:\GenAI\GEN-AI-With-Python\Practice\Day01_02022026"
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, "test04.txt")

with open(file_path, "w") as f:
    f.write("Folder auto create ho gaya")




