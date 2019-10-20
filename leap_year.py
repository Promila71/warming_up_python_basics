year = input("enter the year: ")
year=int(year)

if year % 100!=0 and year % 4 ==0:
    print ("yes")
elif year % 400 == 0 and year % 100 == 0 :
    print("yes")
else:
    print("No")