try:
    firstN=int(input("Write the first number: "))
    secondN=int(input("Write the second number: "))
except:
    print("both numbers need to be int")
else:
    if firstN<=secondN:
        if firstN==secondN:
            print("both numbers are equals")
        else:
            nonList=[]
            for i in range(firstN,secondN+1):
                if i%2!=0:
                    nonList.append(i)
            print(nonList)
    else:
        print("the first number has to be less than the second number")
