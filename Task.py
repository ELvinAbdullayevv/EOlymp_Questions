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

# import sys
#
# notebook1 = {"Created": "Vince Gilligan",
#               "Series name": "Breaking bad",
#               "Genre": "Crime drama",
#               "Episodes": "62",
#               "Release": "20 January 2008",
#               "Seasons": 5}
#
# notebook2 = {"Created": "Jantje Friese",
#               "Series name": "Dark",
#               "Genre": "Science fiction",
#               "Episodes": "26",
#               "Release": "01 December 2017",
#               "Seasons": 3}
#
# notebook3 = {"Created": "Robert Kirkman",
#               "Series name": "The Walking Dead",
#               "Genre": "Horror",
#               "Episodes": "153",
#               "Release": "31 October 2010",
#               "Seasons": 10}
#
# notebooks = [notebook1, notebook2, notebook3]
#
# def find_creator_and_series_name():
#     if len(sys.argv) > 2:  # You need to check if there are at least 2 command-line arguments
#         director = sys.argv[1]
#         movie_name = sys.argv[2]
#
#         for notebook in notebooks:
#             for key, value in notebook.items():
#                 if value == director or value == movie_name:
#                     print(f"{key}: {value}")
#
# find_creator_and_series_name()



# Task1
number1 = input()
number2 = input()
calculation = input()


def calculator(func):
    def calc_progress(a, b):
        a = int(a)
        b = int(b)
        if a == 0 or b == 0:
            print("The result equal to 0")
            return
        else:
            print("Calculating...")
            return func(a, b)

    return calc_progress


@calculator
def plus(a, b):
    print(a + b)


@calculator
def multiply(a, b):
    print(a * b)


@calculator
def division(a, b):
    print(a / b)


@calculator
def minus(a, b):
    print(a - b)


match calculation:
    case "+":
        plus(number1, number2)
    case "-":
        minus(number1, number2)
    case "/":
        division(number1, number2)
    case "*":
        multiply(number1, number2)





# Task2
import sys

inputs = []
if len(sys.argv) > 1:
    a = sys.argv[1]
    if a == "add":
        title1 = input("Enter Series Name: ")
        title2 = input("Enter director name: ")
        title3 = input("Enter series of episodes: ")
        title4 = input("Enter genre: ")
        b = [title1, title2, title3, title4]
        inputs.append(b)
        print(*inputs)


    else:
        print("please write add")

try:
    with open("C:/Users/user/Desktop/python/newtext.txt", "a") as file:
        for item in inputs:
            file.write(str(item) + "\n")
except Exception:
    print("An error occurred while writing to the file:", )