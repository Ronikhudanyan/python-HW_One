#QUESTION 1
# def sum_to(num):
#   sum = 0
#   for i in range(num + 1):
#     sum += i
#   return sum
# print(sum_to(6))


#QUESTION 2
# def largest(ls):
#   largest = 0
#   for num in ls:
#     if num > largest:
#       largest = num
#   return largest

# print(largest([1,2,3,4,500]))



#QUESTION 3
# def occurances(string, substr):
#   count = string.count(substr)
#   return count

# print(occurances('fleep floop', 'e'))


#QUESTION 4
# def product(*args):
#   product = 1
#   for arg in args:
#     product *= arg
#   return product
# print(pcoduct((1,2,3))

# EXTRA HW 
#GET NAME 1
# name = input("Enter Name")
# print("Hello", name)

# REVERSE IT 2
# strang = "Roni Khudanyan"
# print(strang[::-1])

# SWAP EM 3
# a = 30
# b = 10

# temp = b
# b = a
# a = temp

# print("a is now ",  a,  ", and b is now ", b)


#MULTIPLY 4
# list1 = [2,10]
# list2 = [4,5,2,1]

# def multiplylist(mylist):
#   result = 1
#   for x in mylist:
#     result = result * x
#   return result

# print(multiplylist(list1))
# print(multiplylist(list2))

#FIZZBUZZ DIVISIBLE #5
# def checkdevis(i):
#   if i % 3 == 0 and i % 5 == 0:
#     print("fizzbuzz")
#   elif i % 3 == 0:
#     print("fizz")
#   elif i % 5 == 0:
#     print("buzz")
#   else:
#     print(i)
# # print(checkdevis(12))
# # print(checkdevis(50))
# print(checkdevis(15))

# FIND IN ARRAY AND PRINT TRUE
# myarr = ["roni", "billie", "paola", "waldo", "gabby", "kristi"]

# def whereswaldo(array, value):
#   count = array.count(value)
#   if count >= 1:
#     print(True)
#   elif count == 0:
#     print(False)

# print(whereswaldo(myarr, "waldo"))

#FIND DUPLICATES
# myarr = ["roni", "billie", "paola", "waldo", "gabby", "kristi"]
# myarr2 = ["roni", "roni", "billie", "paola", "waldo", "gabby", "kristi"]

# def isdupe(array):
#   if len(array) != len(set(array)):
#     return ("there are dupes!")
#   elif len(array) == len(set(array)):
#     return ("there are no dupes!")

# print(isdupe(myarr))
# print(isdupe(myarr2))

#CHECK FOR PALINDROME
# def ispalindrome(string):
#   if string == string[::-1]:
#     return "it is a palindrome!"
#   elif string != string[::-1]:
#     return "this is not a palindrome!"

# print(ispalindrome("racecar"))
# print(ispalindrome("roni"))