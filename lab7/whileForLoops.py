# ----------------------------------------Циклы: Задачи на цикл while
# ----------------------------------Task A 

# a = int(input())
# i = 1
# while i**2 <= a:
#     print(i**2)
#     i+=1

# ----------------------------------Task B 

# a = int(input())
# i = 2
# while a%i != 0:
#     i+=1
# print(i)

# ----------------------------------Task C 

# a = int(input())
# i = 0
# while 2**i <= a:
#     print(2**i, end = " ")
#     i+=1

# ----------------------------------Task D 

# a = int(input())
# while a!=0:
#     if a%2 == 0 or a == 1:
#         a = a//2
#     else:
#         print("NO")
#         break
# if(a == 0): 
#     print("YES")

# ----------------------------------Task E

# a = int(input())
# sum = 1
# b = 0
# while a > sum:
#     sum *= 2
#     b += 1
# print(b)



# ----------------------------------------------Циклы: Задачи на цикл for:

# ----------------------------------Task A 

# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if(i%2 == 0):
#         print(i, end = " ")

# ----------------------------------Task B 

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(a,b+1):
#     if i%d == c:
#         print(i, end = " ")

# ----------------------------------Task C

# import math

# a = int(input())
# b = int(input())

# for i in range(a,b+1):
#     if math.sqrt(i * 1.0) == int(math.sqrt(i)):
#         print(i)


# ----------------------------------Task D
# b = int(input())
# a = int(input())
# cnt = 0
# for i in str(b):
#     if i == str(a):
#         cnt+=1
# print(cnt)
# ----------------------------------Task E 

# b = int(input())
# cnt = 0
# for i in str(b):
#     cnt+=int(i)
# print(cnt)


# ----------------------------------Task F 

# b = int(input())
# while(b%10 == 0): b//=10
# while(b!=0):
#     print(b%10,end="")
#     b//=10


# ----------------------------------Task G

# b = int(input())
# for i in range(2, b+1):
#     if b%i==0:
#         print(i)
#         break

# ----------------------------------Task H

# b = int(input())
# for i in range(1, b+1):
#     if b%i==0:
#         print(i, end = " ")
        
# ----------------------------------Task I 

# import math

# cnt = 0
# b = int(input())
# for i in range(1, int(math.sqrt(b))):
#     if b%i==0:
#         cnt+=1
# cnt*=2
# if(math.sqrt(b) == int(math.sqrt(b))):
#     cnt+=1

# print(cnt)


# ----------------------------------Task J

# k = 0
# for i in range(0,100):
#     b = int(input())
#     k+=b 
# print(k)
# ----------------------------------Task K 
# a = int(input())
# k = 0
# for i in range(0,a):
#     b = int(input())
#     k+=b 
# print(k)
# ----------------------------------Task L

# binary = int(input())
# decimal, i = 0, 0
# while(binary != 0):
#     dec = binary % 10
#     decimal = decimal + dec * pow(2, i)
#     binary = binary//10
#     i += 1
# print(decimal)


# ----------------------------------Task M

a = int(input())
cnt = 0
for i in range(0,a):
    b = int(input())
    if b == 0:
        cnt+=1
print(cnt)