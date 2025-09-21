import mylib

input_num = int(input("How many turns you want to run : "))

for i in range(1, input_num + 1):  
    print(mylib.myfunc("x", i))     