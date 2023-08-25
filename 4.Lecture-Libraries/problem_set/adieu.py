import inflect

p = inflect.engine()

lis=[]
while True:
    try:
        lis.append(input("Name: "))
    except EOFError:
        mylist = p.join(lis)
        print("Adieu, adieu, to " + mylist)
        break
