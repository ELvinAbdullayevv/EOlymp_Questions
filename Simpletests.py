# TEST 2
# a = int(input("Eded daxil edin "))
# print(len(str(a))

# ProjectEuler.net
# b  = 2 ** 1000
# count = 0
# while b > 1:
#     a = b%10
#     count += a
#     b = b // 10
# print(count)


# 903
# a =abs(int(input()))

# b = a % 10
# c = (a // 10) % 10
# d = a // 100
#
# if b == d:
#     print("=")
# else:
#     print(max(b,d))

# 905
# a,b,c = map(int, input().split())
# if a == b == c:
#     print("1")
# elif a == b or a == c or b == c:
#     print("2")
# else:
#     print("3")

# 906
# a = int(input())
# b = a % 10
# c = (a // 10) % 10
# d = a // 100
# product = b * c * d
# print(product)

# 909
# a = str(input())
# res = len(a.split())
# print(str(res))

# 915
# a,b,c = map(int,input().split())
# if a**2 + c**2 == b**2 or a**2 + b**2  == c**2 or b**2 +c**2 == a**2:
#     print("YES")
# else:
#     print("NO")

# 923
# season = int(input())
# if season >= 3 and season <= 5:
#     print("Spring")
# elif season >= 6 and season <= 8:
#     print("Summer")
# elif season >= 9 and season <= 11:
#     print("Autumn")
# else:
#     print("Winter")

# 931
# a = int(input())
# digit = 0
# product = 1
# while a > 0:
#     b = a % 10
#     product *= b
#     digit += b
#     a = a // 10
# print('{:.3f}'.format((product / digit)))

# # 932
# import math
#
# s, a = map(float,input().split())
#
# d = a*a + 8*s;
#
# h = (-a + math.sqrt(d)) / 2;
# print("%.2f" %h)

# 909
# a = str(input())
# res = len(a.split())
# print(str(res))

# a = str(input())

# words = a.split()
# count = 0
# for word in words:
#     count += 1
# print(count)

# 901
# a = input("listi daxil edin")
# b = ("*", "-", "+")

# count = 0
# for i in a[1::1]:
#     if i in b:
#       count +=1

# print(count)


# 8320
# centence = str(input())
# a = centence.title()
# print(a)


# 8569
# centence = input()
# a = len(centence)
# print(centence)
# print(a)

# 8319
# a ,c, b, = input().split(" ")
# a = int(a)
# b = int(b)


# if c == ('+'):
#         print(a+b)
# elif c == ('-'):
#         print(a-b)
# elif c == ('*'):
#         print(a*b)
# elif c == ("/"):
#         print(a // b)


# 920
# def number(x,y,z):
#     decimal_num = min(max(x,y), max(y,z), x+y+z)
#     return "{:.2f}".format(decimal_num)

# x,y,z = map(float,input().split())
# print(number(x,y,z))




