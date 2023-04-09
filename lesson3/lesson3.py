fizz=int(input("1 number= "))
buzz=int(input("2 number= "))
x=int(input("3 number= "))

for i in range (1, x+1,1):
    if (not i%fizz and not i%buzz):
        print ("FB", end=" ")
    elif (not i%fizz):
        print ("F", end=" ")
    elif (not i%buzz):
        print ("B", end=" ")
    else:
        print (i, end=" ")