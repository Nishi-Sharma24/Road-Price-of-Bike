#Write a program to accept the cost price of a bike and display the road tax and road price to be paid according to the following criteria :
cp=int(input("Enter the cost price of bike:"))
if cp>100000:
       tax=15/100*cp
elif cp>50000 and cp<=100000:
    tax=10/100*cp
elif cp<=50000:
    tax=5/100*cp
road_price=tax+cp
print("The road price of bike is",road_price)
input()
