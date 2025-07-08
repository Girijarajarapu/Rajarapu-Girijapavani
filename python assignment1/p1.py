year=int(input("enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year}is leap year")
        else:
            print("it is not leap year",year)
    else:
        print("it is leap year",year)
else:
    print("it is not leap year")



first=int(input("enter the 1st digit number:"))
second=int(input("enter the 2st digit number:"))
third=int(input("enter the 3st digit number:"))
if first==2*second and first==third/2:

    print("yes you have done it")
else:
    print("please try next time")



height = float(input("Enter height of one wall (in meters): "))
width = float(input("Enter width of one wall (in meters): "))
cost_per_sq_meter = float(input("Enter cost of painting per square meter: "))

area_one_wall = height * width
total_area = 4 * area_one_wall

total_cost = total_area * cost_per_sq_meter
 
print(f"\nTotal area to paint: {total_area:.2f} square meters")
print(f"Total cost of painting: ₹{total_cost:.2f}")



p1=float(input("enter the product1:"))
p2=float(input("enter the produc2:"))
p3=float(input("enter the product3:"))
p4=float(input("enter the product4:"))
p5=float(input("enter the product5:"))
total=p1+p2+p3+p4+p5
gst=total*0.18
billtotal=total+gst
print("the total bill ",total)
print("the gst is",gst)
print("the totalbill is:",billtotal)


import math


radius_cm = 20
length_cm = 50
breadth_cm = 40
cost_per_meter = 35
rounds = 5

radius_m = radius_cm / 100
length_m = length_cm / 100
breadth_m = breadth_cm / 100


half_circle = math.pi * radius_m


rectangle_sides = 2 * breadth_m


diameter_m = 2 * radius_m


perimeter_one_round = half_circle + rectangle_sides + diameter_m


total_length = perimeter_one_round * rounds


total_cost = total_length * cost_per_meter

print(f"Total length of fencing (in meters): {total_length:.2f} m")
print(f"Total cost of fencing: ₹{total_cost:.2f}")
