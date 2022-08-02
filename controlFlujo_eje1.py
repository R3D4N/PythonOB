try:
    age=int(input("write your age: "))
except:
    print("You need to write a number.")
else:
    if age>=18:
        print("you are an adult.")
    else:
        print("you are not old enough.")
