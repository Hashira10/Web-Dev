# -----------------------------------------------Task A

# a = int(input())
# b = map(int, input().split(maxsplit=a))
# numbers = []
# for i in b:
#     numbers.append(i)
# print(*numbers[::2])


# -----------------------------------------------Task B 

# a = int(input())
# b = map(int, input().split(maxsplit=a))
# numbers = []
# for i in b:
#     if i%2==0:
#         print(i, end=" ")


# -----------------------------------------------Task C 

# a = int(input())
# b = map(int, input().split(maxsplit=a))
# cnt = 0
# numbers = []
# for i in b:
#     if i > 0:
#         cnt+=1

# print(cnt)


# -----------------------------------------------Task D 


# a = int(input())
# b = map(int, input().split(maxsplit=a))
# numbers = []
# cnt = 0
# for i in b:
#     numbers.append(i)
# for i in range(1,a):
#     if numbers[i] > numbers[i-1]:
#         cnt += 1
# print(cnt)


# -----------------------------------------------Task E 

# a = int(input())
# b = map(int, input().split(maxsplit=a))
# numbers = []
# ok = False
# for i in b:
#     numbers.append(i)
# for i in range(0,a-1):
#     if (numbers[i] >= 0 and numbers[i+1] >= 0) or (numbers[i] < 0 and numbers[i+1] < 0):
#         print("YES")
#         ok = True
#         break
# if ok == False:
#     print("NO")

# -----------------------------------------------Task F 

# a = int(input())
# b = map(int, input().split(maxsplit=a))
# numbers = []
# cnt = 0
# for i in b:
#     numbers.append(i)
# for i in range(1,a-1):
#     if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
#         cnt+=1
# print(cnt)


# -----------------------------------------------Task G

a = int(input())
b = map(int, input().split(maxsplit=a))
numbers = []
cnt = 0
for i in b:
    numbers.append(i)
for i in range(0,a//2):
    cnt = numbers[i]
    numbers[i] = numbers[a-1-i]
    numbers[a-1-i] = cnt
print(*numbers)