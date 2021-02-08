# main.py


### I am going to be coding that converts integers to Roman numarals in Python.

##### First, 1~10

    # 1 = I
    # 2 = II
    # 3 = III
    # 4 = IV
    # 5 = V
    # 6 = VI
    # 7 = VII
    # 8 = VIII
    # 9 = IX
    # 10 = X

i = int(input("Number: "))

if i <= 3:
    print("I"*i)
elif i == 4:
    print("IV")
elif i == 5:
    print("V")
elif 5 < i < 9:
    print("V"+"I"*(i-5))
elif i == 9:
    print("IX")
else:
    print("X")


### How can I make a function for this...?
# def convt_int_romannum(i):
#     i = int(input("Number: "))

#     if i == 1:
#         print("I")