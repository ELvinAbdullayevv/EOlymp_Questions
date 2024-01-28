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

def find_deviders(num):
    result = set()
    result.add(num)
    max_num = int(num / 2) + 1
    for i in range(1, max_num):
        if num % i == 0:
            result.add(i)

    return result


num1 = int(input("first number:"))
num2 = int(input("second number:"))

first_devidors = find_deviders(num1)
second_devidors = find_deviders(num2)
intersection = first_devidors & second_devidors
print(num1, "sayisinin bolenleri", first_devidors)
print(num2, "sayisinin bolenleri", second_devidors)
print("kesisen bolenleri", intersection)
print("EBOB: ", max(intersection))