# 1000
# import sys
#
# for s in sys.stdin:
#
#   a, b = map(int,s.split())
#
#   print(a+b)

# 8806
# a, b = map(int, input().split())
# print(a+b)


# 8809
# a,b = map(int,input().split())
# print(a-b)

# 8808
# a = int(input())
# b = int(input())
# print(a-b)

# 8810
# a,b,c = map(int, input().split())
# print(a+b-c)

# 8811
# a,b =  map(int, input().split())
# print(a*b)

# 8812
# a, b = map(int, input().split())
# p = 2*(a+b)
# s = a *b
# print(p,s)

# 8814
# a = int(input())
# p = 4 * a
# s = pow(a,2)
# print(p,s)

# 8817
# n = int(input())
# # count = 20 * (21 ** (n-1))
# # print(count)

# 9575
# a = float(input())
# x = "{:.4f}".format(3.14 * a ** 2)
# print(x)

# 9576
# a = float(input())
# x = "{:.3f}".format(3.14 * a * 2)
# print(x)

# 9900
# n = int(input())
# print(n)

# 9901
# n = int(input())
# print(n-1)

# 9902
# n = int(input())
# c = n // 2
# print(c)

# 9903
# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     if n % 2 != 0:
#         print((n // 2)+1)

# 9904
# n = int(input())
# if n % 2 == 0:
#     print(n // 2)
# else:
#     if n % 2 != 0:
#         print((n // 2))

# 9905
# n = int(input())
# if n % 2 == 0:
#      print((n // 2)-1)
# else:
#      if n % 2 != 0:
#         print((n // 2))


# 9906
# a,b = map(int, input().split())
# if a or b < o:
#     print(abs(a-b)+1)
# else:
#     print(a-b)


# Region 3
# a = str(input("Sozler daxil edin "))
# b = a.split()
# c = []
# for words in  b:
#     if words not in c:
#         c.append(words)

# print(c)

# Region 1
# num = int(input("Enter number "))
# factorial = 1
# if num == 0:
#     print("factorial is 1 for 0")
# elif num < 0:
#     print("factorial does not exit negative numbers")
# else:
#     for i in range(1, num+1):
#         factorial *= i
#     print(factorial)


# Region 2
# word_list = str(input("Sozleri daxil edin "))
# b = word_list.split()

# palindrome = []
# non_polindrome = []

# for words in b:
#     if words == words[::-1]:
#         palindrome.append(words)
#     else:
#         non_polindrome.append(words)

# print(palindrome)
# print(non_polindrome)


# Region 4
# number = int(input("ededi daxil edin "))

# num = []

# i = 1

# for i in range(1, number+1):
#     if number % i == 0:
#         num.append(i)
# print(num)



# 1605
# number = int(input("Enter a number: "))
#
# if number < 2:
#     print(f"{number} is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")




