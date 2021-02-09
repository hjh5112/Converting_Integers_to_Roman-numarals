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

# if i <= 3:
#     print("I"*i)
# elif i == 4:
#     print("IV")
# elif i == 5:
#     print("V")
# elif 5 < i < 9:
#     print("V"+"I"*(i-5))
# elif i == 9:
#     print("IX")
# else:
#     print("X")

##### Now, expand it to 1000

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
    # 50 = L
    # 100 = C
    # 500 = D
    # 1000 = M

def convt_int_to_romannum(x):
    
    if x < 1000:
        # seperate input integer by place value
        i = x // 100 # hundreds
        j = (x - i*100) // 10 # tens
        k = x - i*100 - j*10 # units

        print(i, j, k, sep="")

        i_fctn(i) # convert function of hundreds
        j_fctn(j) # convert function of tens
        k_fctn(k) # convert function of units
    else:
        print(x)
        print("M")

# convert function of units
def k_fctn(k):
    if k < 4:
        print("I"*k)
    elif k == 4:
        print("IV")
    elif k == 5:
        print("V")
    elif k == 9:
        print("IX")
    else:
        print("V"+"I"*(k-5))

# convert function of tens
def j_fctn(j):
    if j < 4:
        print("X"*j, end = "")
    elif j == 4:
        print("XL", end = "")
    elif j == 5:
        print("L", end = "")
    elif j == 9:
        print("XC", end = "")
    else:
        print("L"+"X"*(j-5), end = "")

# convert function of hundreds
def i_fctn(i):
    if i < 4:
        print("C"*i, end = "")
    elif i == 4:
        print("CD", end = "")
    elif i == 5:
        print("D", end = "")
    elif i == 9:
        print("CM", end = "")
    else:
        print("D"+"C"*(i-5), end = "")

convt_int_to_romannum(85)