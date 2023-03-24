# Warmup-1

# def sleep_in(weekday, vacation):
#   if not weekday or vacation:
#     return True
#   else:
#     return False



# def diff21(n):
#   if n <= 21:
#     return 21 - n
#   else:
#     return (n - 21) * 2

# def near_hundred(n):
#   return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# def missing_char(str, n):
#   front = str[:n]
#   back = str[n+1:]
#   return front + back


# def monkey_trouble(a_smile, b_smile):
#   if a_smile and b_smile:
#     return True
#   if not a_smile and not b_smile:
#     return True
#   return False


# def pos_neg(a, b, negative):
#   if negative:
#     return (a < 0 and b < 0)
#   else:
#     return ((a < 0 and b > 0) or (a > 0 and b < 0))


# def front_back(str):
#   if len(str) <= 1:
#     return str
  
#   mid = str[1:len(str)-1] 
#   return str[len(str)-1] + mid + str[0]


# def sum_double(a, b):
#   sum = a + b

#   if a == b:
#     sum = sum * 2
#   return sum



# def makes10(a, b):
#   return (a == 10 or b == 10 or a+b == 10)




# def not_string(str):
#   if len(str) >= 3 and str[:3] == "not":
#     return str
#   return "not " + str



# def front3(str):
#   front_end = 3
#   if len(str) < front_end:
#     front_end = len(str)
#   front = str[:front_end]
#   return front + front + front





# Warmup2


# def string_times(str, n):
#   result = ""
#   for i in range(n): 
#     result = result + str
#   return result



# def string_splosion(str):
#     result = ""
#     for i in range(len(str)):
#         result = result + str[:i+1]
#     return result


# def array_front9(nums):
#     end = len(nums)
#     if end > 4:
#         end = 4
    
#     for i in range(end):
#         if nums[i] == 9:
#         return True
#     return False


# def front_times(str, n):
#     front_len = 3
#     if front_len > len(str):
#         front_len = len(str)
#     front = str[:front_len]
    
#     result = ""
#     for i in range(n):
#         result = result + front
#     return result


# def last2(str):
#   if len(str) < 2:
#     return 0
  
#   last2 = str[len(str)-2:]
#   count = 0
  
#   for i in range(len(str)-2):
#     sub = str[i:i+2]
#     if sub == last2:
#       count = count + 1

#   return count


# def array123(nums):
#   for i in range(len(nums)-2):
#     if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#       return True
#   return False


# def string_bits(str):
#   result = ""
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result


# def array_count9(nums):
#   count = 0
#   for num in nums:
#     if num == 9:
#       count = count + 1

#   return count

# def string_match(a, b):
#   shorter = min(len(a), len(b))
#   count = 0

#   for i in range(shorter-1):
#     a_sub = a[i:i+2]
#     b_sub = b[i:i+2]
#     if a_sub == b_sub:
#       count = count + 1

#   return count



# String1
# def hello_name(name):
#   result = "Hello " + name + "!"
#   return result

# def make_out_word(out, word):
#     result = out[:2] + word + out[2:]
#     return result


# def first_half(str):
#   result = str[:len(str)/2]
#   return result


# def non_start(a, b):
#   result = a[1:] + b[1:]
#   return resultv


# def make_abba(a, b):
#   result = a+b+b+a
#   return result


# def extra_end(str):
#   result = str[-2:] + str[-2:] + str[-2:]
#   return result


# def without_end(str):
#   result = str[1:-1]
#   return result


# def left2(str):
#   result = str[2:] + str[:2]
#   return result


# def make_tags(tag, word):
#   result = "<" + tag + ">" + word + "</" + tag + ">"
#   return result


# def first_two(str):
#   result = str[:2]
#   return result


# def combo_string(a, b):
#   if len(a) < len(b):
#     result = a+b+a
#   else:
#     result = b+a+b
#   return result

# List 1

# def first_last6(nums):
#   if nums[0] == 6 or nums[len(nums)-1] == 6:
#     return True
#   else:
#     return False


# def common_end(a, b):
#   if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
#     return True
#   else:
#     return False

# def reverse3(nums):
#   result = []
#   for i in range(0,len(nums)):
#     result.append(nums[len(nums)-1-i])
#   return result


# def middle_way(a, b):
#   result = []
#   result.append(a[1])
#   result.append(b[1])
#   return result


# def same_first_last(nums):
#   if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
#     return True
#   else:
#     return False


# def sum3(nums):
#   return nums[0]+nums[1] + nums[2]


# def max_end3(nums):
#   result = []
#   mx = nums[len(nums)-1]
#   if nums[0] > nums[len(nums)-1]:
#     mx = nums[0]
#   for i in range(0,3):
#     result.append(mx)
#   return result


# def make_ends(nums):
#   result = []
#   result.append(nums[0])
#   result.append(nums[len(nums)-1])
#   return result

# def make_pi():
#   result = [3, 1, 4]
#   return result


# def rotate_left3(nums):
#   result = [nums[1], nums[2], nums[0]]
#   return result


# def sum2(nums):
#   if len(nums)>1:
#     return nums[0]+nums[1]
#   elif len(nums) == 1:
#     return nums[0]
#   else:
#     return 0


# def has23(nums):
#   if 2 in nums or 3 in nums:
#     return True
#   else:
#     return False


# Logic 1

# def cigar_party(cigars, is_weekend):
#   if is_weekend == False and (cigars < 40 or cigars > 60):
#     return False
#   elif is_weekend == True and cigars < 40:
#     return False
#   else:
#     return True


# def caught_speeding(speed, is_birthday):
#   if is_birthday == False:
#     if speed <= 60:
#       return 0
#     elif speed >= 61 and speed <= 80:
#       return 1
#     else:
#       return 2
#   else:
#     if speed <= 65:
#       return 0
#     elif speed >= 66 and speed <= 85:
#       return 1
#     else:
#       return 2



# def love6(a, b):
#   if a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6:
#     return True
#   else:
#     return False




# def date_fashion(you, date):
#   if you <= 2 or date <= 2:
#     return 0
#   elif you >= 8 or date >= 8:
#     return 2
#   else:
#     return 1



# def sorta_sum(a, b):
#   if a+b >=10 and a+b <=19:
#     return 20
#   else:
#     return a+b



# def in1to10(n, outside_mode):
#   if n >=1 and n <=10 and outside_mode == False:
#     return True
#   if outside_mode == True and (n <= 1 or n >=10):
#     return True
#   else:
#     return False



# def squirrel_play(temp, is_summer):
#   if temp >= 60 and temp <=90 and is_summer == False:
#     return True
#   elif is_summer ==True and temp >= 60 and temp <=100:
#     return True
#   else:
#     return False


# def alarm_clock(day, vacation):
#   if vacation == True and (day == 6 or day == 0):
#     return "off"
#   elif vacation == True and day != 6 and day != 0:
#     return "10:00"
#   elif vacation == False and (day == 6 or day == 0):
#     return "10:00"
#   else:
#     return "7:00"


# def near_ten(num):
#   return (num + 2) % 10 <= 4




# Logic 2

# def make_bricks(small, big, goal):
#   return (goal%5)<=small and (goal-(big*5))<=small


# def fix_teen(n):
#     if (n >= 13 and n <=19):
#         if (n!= 15 and n != 16):
#             n = 0
#     return n
# def no_teen_sum(a, b, c):
#   return fix_teen(a)+fix_teen(b)+fix_teen(c)


# def make_chocolate(small, big, goal):
#   if small + big * 5 < goal or small < goal%5 : 
#     return -1
#   elif((big * 5) > goal):
#     return goal % 5
#   else:
#     return goal - big * 5

  

# def lone_sum(a, b, c):

#   if a != b and b != c and c != a:
#     return a + b + c

#   elif a == b == c:
#     return 0 

#   elif a == b:
#     return c
#   elif b == c:
#     return a
#   elif c == a:
#     return b



# def round_sum(a, b, c):
#   def round10(n):
#     return (n+5)/10*10 
    
#   return round10(a) + round10(b) + round10(c)


# def lucky_sum(a, b, c):
#   if a==13:
#     return 0
#   elif b==13:
#     return a
#   elif c==13:
#     return a+b
#   else:
#     return a+b+c


# def close_far(a, b, c):
#   return (abs(a - b) <= 1 or abs(a - c) <= 1) and abs(c - a) >= 2 <= abs(c - b) or abs(b - a) >= 2 <= abs(b - c)


# String 2

# def double_char(str):
#   result = ""
#   for i in range(0,len(str)):
#     result+=str[i]+str[i]
#   return result


# def count_code(str):
#   x=["co"+i+"e" for i in str.lower()]
#   count = 0
#   index = 0
#   for i in x:
#       if i in str[index:]:
#           index = str.find(i)+1
#           count+=1
#   return count


# def count_hi(str):
#   count = 0
#   for i in range(len(str)-1):
#       if str[i:i+2] == "hi":
#           count += 1
          
#   return count



# def end_other(a, b):
#   a = a.lower()
#   b = b.lower()
      
#   return a.endswith(b) or b.endswith(a)


# def cat_dog(str):
#   cat = 0
#   dog = 0
    
#   for i in range(len(str) - 2):
#       if str[i:i+3] == "cat":
#           cat += 1
#       elif str[i:i+3] == "dog":
#           dog += 1
                                
#   return cat == dog



# def xyz_there(str):
#   if str[:3] == "xyz":
#       return True
                  
#   for i in range(1, len(str) - 2):
#       if str[i-1] != "." and str[i:i+3] == "xyz":
#           return True
                                    
#   return False



# List 2

# def count_evens(nums):
#   cnt = 0
#   for i in nums:
#     if i%2 == 0:
#       cnt += 1
#   return cnt


# def sum13(nums):
#     sm = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 13:
#             i += 1
#         else:
#             sm += nums[i]
            
#         i += 1
        
#     return sm



# def big_diff(nums):
#     mn = nums[0]
#     mx = nums[0]
      
#     for i in range(1,len(nums)):
#         mn = min(mn, nums[i])
#         mx = max(mx, nums[i])
                    
#     return mx- mn



# def sum67(nums):
#     res = 0
#     a = False
      
#     for i in range(len(nums)):
#         if nums[i] == 6:
#             a = True
#         if not a:
#             res += nums[i]
#         if nums[i] == 7 and a:
#             a = False
            
#     return res


# def centered_average(nums):
#    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


# def has22(nums):
#   for i in range(len(nums)-1):
#     if nums[i] == 2 and nums[i+1] == 2:
#       return True
#   return False
