# def min_num(a,b,c,d):
#     min = a 
#     if min > b:
#         min = b 
#     if min > c:
#         min = c 
#     if min > d:
#         min = d 
    
#     print(min)
        
# a,b,c,d = map(int,input().split())
# min_num(a,b,c,d)


# Task B

# def my_pow(a,b):
#     pow = 1
#     while b != 0:
#         pow*=a
#         b-=1
#     print(pow)
# a, b = input().split()
# my_pow(float(a),int(b))


# Task c

def xor(x, y):
    ok = False
    if (x == 1 and y == 0) or (x == 0 and y == 1):
        print(1)
        ok = True
    if ok == False:
        print(0)
a,b = map(int, input().split())
xor(a,b)