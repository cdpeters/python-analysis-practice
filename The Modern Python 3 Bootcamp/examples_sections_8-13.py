#===========================================
# Section 8: Boolean and Conditional Logic
#===========================================

# video 61 Getting User Input

# data = input("What's your favorite color?\n")
# print("You said " + data)

#-----------------------------------------------------------------------------

# video 62 Conditionals

# name = input('enter a name: ')
# if name == "Arya Stark":
#     print("Valar Morghulis")
# elif name == "Jon Snow":
#     print("You know nothing")
# else:
#     print("Carry on")

#-----------------------------------------------------------------------------

#================================
# Section 10: Looping in Python
#================================

# video 83 The Basics of For Loops

# for char in "hello":
#     print(char)

#-----------------------------------------------------------------------------

# video 84 Exploring Ranges in Depth

# range(5) will use a default start of 0 and go to 4 (5-1)
# for num in range(5):
#     print(num)

# range1 = range(1,10,2)
# range2 = range(0,10,2)
# range3 = range(1,9,2)
# range4 = range(0,9,2)
# number_sets = [range1, range2, range3, range4]

# for number_set in number_sets:
#     for number in number_set:
#         print(number)
#     print()

# for num in range(10,1,-3):
#     print(num)

# can display ranges easier (without the need for printing in a loop) using
# list()

# r = range(1,15,4)
# print(list(r))

#-----------------------------------------------------------------------------

# video 86 EXERCISE: Screaming Repeating

# repeats = int(input("How many times do I have to tell you? "))

# for num in range(repeats):
#     print("CLEAN UP YOUR ROOM!")

#-----------------------------------------------------------------------------

# video 87 EXERCISE: Unlucky Numbers

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# another way
# state = None

# for num in range(1,21):
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")

#-----------------------------------------------------------------------------

# video 89 EXERCISE: Emoji Art
# for num in range(1,11):
#     print("\U0001f600"*num)

# num = 1
# while num < 11:
#     print("\U0001f600"*num)
#     num +=1

#-----------------------------------------------------------------------------

# video 90 EXERCISE: Stop Copying Me

# user_input = input("Hey how's it going? ")

# while user_input != "stop copying me":
#     print(user_input)
#     user_input = input()
# print("UGH FINE YOU WIN")

#-----------------------------------------------------------------------------

#====================
# Section 12: Lists
#====================

# video 102 Iterating Over Lists
# numbers = [1,2,4,5]

# # can use "in" to loop over a list where number is an individual item in the
# # list
# for number in numbers:
#     print(number)

#-----------------------------------------------------------------------------






