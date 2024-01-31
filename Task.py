# TASK 1
# a = list(input().split())

# a.sort(key = len)


# for word in a:
#     print(word)


# Task 3
# numbers = list(map(float, input("ededi daxil edin ").split()))

# product = 1

# for element in numbers:
#     product *= element

# print(product)


# Task 4
# a = list(map(int, input("Ededi daxil edin ").split()))

# b = list(map(int,input("Ededi daxil edin ").split()))

# for i in b:
#     a.append(i)
#     a.sort()

# print(a)


# EBOB TASK

# def abc():
#     b = input("eded daxil edin")
#
#     try:
#         b = float(b)
#         print("{}".format(round(b)))
#     except:
#         print("{} bu variable errordur".format(b))
#
#
# print(abc())


# luget = {
#     'meyve' : 'fruit' ,
#     'kitab' : 'book' ,
#     'komputer' : 'computer' ,
#     'masa' : 'desk' ,
#     'qelem' : 'pen' ,
# }
# deleted_word = input()
#
#
# if deleted_word in luget:
#         del luget[deleted_word]
# print(luget)


# Task1

# book = {"writer" : "Nizami Gencevi",
#         "poem" : "Yeddi Gozel",
#         "year" : 1147}


# another_book = {"writer" : "Nizami Gencevi",
#                 "poem" : "Leyli Mecnun",
#                 "year" : 1188}


# same_values_and_keys = {}

# for i in set(book) and  set(another_book):
#     if book[i] == another_book[i]:
#         same_values_and_keys[i] = (book[i])

# print(same_values_and_keys)


# Task3
# dict1 = {12, 13, 14, 24, 9, 27, 51}


# dict2= []

# for i in dict1:
#     if i % 3 == 0:
#         dict2.append(i)
# print(sorted(dict2))