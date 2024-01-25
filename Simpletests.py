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


# 8681
# def product_num(a):
#     b=1
#     for i in str(a):
#         digit =int(i)
#         if digit !=0:


#             b *= digit
#     print(b)

# a = input()

# product_num(a)

# 8679
# size = int(input())
# arr = map(int, input().split())

# c = []
# def min_custom(arr):

#     for num in arr:
#         if num % 3 == 0:
#             c.append(num // 3)


#         else:
#             c.append(num)
#     print(*c)


# min_custom(arr)

# 8689
# def f_x(a):
#     c = 1+a+a**2
#     return c

# a = int(input())
# print(f_x(a))


# 8690

# def calculation(x, y, z):
#     f = x*y*z + x + y**2 + z**3
#     return f

# a, b, c = map(int, input().split())
# print(calculation(a,b,c))


# 2
# def digit(a):
#     b = str(a)
#     return len(b)

# a = int(input())
# print(digit(a))


# 1601
# def ebob(x, y):
#     while y:
#         x , y = y, x % y
#     return x
# a,b = map(int, input().split())
# print(ebob(a,b))


# 1603
# def calculation(x):
#     c = 0
#     while x > 0:
#         digit = int(x % 10)
#         c += digit
#         x = x // 10
#     return c

# a = abs(int(input()))
# print(calculation(a))

# 1658
# def factoriyal(x):
#     if x > 0:
#         return x * factoriyal(x-1)
#     if x == 0:
#         return 1
#     else:
#         False

# a = int(input())
# print(factoriyal(a))


# 3258
# def Fibonacci(n):


#     if n == 0:
#         return 0

#     elif n == 1 or n == 2:
#         return 1

#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# input_fibanocci = int(input())
# print(Fibonacci(input_fibanocci))


# 8609

# def rekursiya(n):
#     if n == 0:
#         return 0

#     elif n > 0:
#         return rekursiya(n-1) + n

#     else:
#         False

# number = int(input())
# print(rekursiya(number))


# a = abs(int(input()))
#
# c = a % 10
# d = a // 100
# if c > d:
#     print(c)
# else:
#     print(d)

# 494
# a = input().upper()

# Vowel_letters = ["A", "E", "I", "O", "U", "Y"]
# count = 0

# for i in a:
#     if i in Vowel_letters:
#         count += 1

# print(count)


# 138
# number = int(input())
# denomination =[500,200,100,50,20,10]
# count = 0
# for i in denomination:

#     c= number//i
#     number = number%i
#     count+=c

# print(count)


# 7831
# def variables(x):

#     max_element = max(x)
#     sum = 0
#     for i in x:
#         if i != max_element:
#             sum += i
#     print(sum)
# a = int(input())
# b = list(map(int,input().split()))
# variables(b)


# 8631
# a = str(input())
# count = 0

# for i in a:
#     c = max(a)
#     if i == c:
#         count += 1
# print(count)


# 5089
# n = int(input())

# c = []
# for i in range(n):
#     word = input()
#     c.append(word)

# a = sorted(c)

# for word in a:
#     print(word)

