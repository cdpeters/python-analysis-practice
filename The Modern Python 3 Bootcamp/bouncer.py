# ask for age. 18-20 wristband, 21+ normal entry and can drink, younger than
# 18 cannot enter
# age = input('How old are you: ')
# if age:
#     age = int(age)
#     if age >= 18 and age < 21:
#         print('You can enter but you need a wristband!')
#     elif age >= 21:
#         print('You can enter and can drink!')
#     else:
#         print('You cannot enter!')
# else:
#     print('Please enter an age!')

# here is the same code except the conditionals are shortened and rearranged.
# First conditional checks if under 21 so the next conditional does not need to
# check this again, instead it only checks to see if age is under 18.
age = input('How old are you: ')
if age:
    age = int(age)
    if age >= 21:
        print('You can enter and can drink!')
    elif age >= 18:
        print('You can enter but you need a wristband!')
    else:
        print('You cannot enter!')
else:
    print('Please enter an age!')