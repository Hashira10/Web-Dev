# Write a function

# def is_leap(a):
#     leap = False
#     if (a % 4 == 0 and a%100 != 0) or (a%400 == 0):
#         leap = True
#     else:
#         leap = False 
    
#     return leap
    
# year = int(input())
# print(is_leap(year))


# Print function

# def print_func(n):
#     ans = ""
#     for i in range(1,n+1):
#         ans+=str(i)
#     print(ans)
# n = int(input())
# print_func(n)

# List Comprehensions

# def permutations(x,y,z,n):
#     ans = []
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if(i+j+k)!=n:
#                     ans.append([i,j,k])

#     print(ans)
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# permutations(x,y,z,n)


# Find the Runner-Up Score!

# def maxnum(n,arr):
#     l = []
#     for i in arr:
#         l.append(i)
#     l.sort()
#     l.reverse()
#     for i in range(1,n):
#         if l[i]!=l[0]:
#             print(l[i])
#             break
    
    
# n = int(input())
# arr = map(int, input().split())
# maxnum(n,arr)


# Nested Lists

# def my_func(l,st):
#     ans = []
#     l.sort()
#     min = 0
#     for i in range (1,len(l)):
#         if l[i] != l[0]:
#             min = l[i]
#             break
#     for i in range(0,len(st)):
#         if st[i][1] == min:
#             ans.append(st[i][0])
#     ans.sort()
#     for i in range(0,len(ans)):
#         print(ans[i])


# l = []
# st = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append(score)
#     st.append([name,score])

# my_func(l,st)


# Arithmetic Operators

# def my_func(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)

# a = int(input())
# b = int(input())
# my_func(a,b)


# Python If-Else


# n = int(input())
# if n % 2 != 0:
#     print("Weird")
# elif n%2 == 0 and n in range(2,6):
#     print("Not Weird")
# elif n%2 == 0 and n in range(6,21):
#     print("Weird")
# else:
#     print("Not Weird")


# Loops

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0,n):
#         print(i*i)


# Division
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a//b)
#     print(a/b)