# the award to be won in the competition
import math
 
swimming  = int(input("Enter the time taking to swim : "))
cycling = int(input("Enter the time taking to cycle:"))
running = int(input("Enter the time to run: "))

# print the time for swimming, cycling snd running 
print ("\n The time taken to swim is : ", swimming )
print ("\n The time taken to cycle is : ", cycling)
print ( "\n The time taken to run is : ", running)

# print the total time for triathlon
total_time = swimming + cycling + running

# print the total time in minits 
print("\n The total time for triathlon is :", total_time )

# print the award receive for a specify time range 
if (total_time <100 ):
    print  ("\n Provincial Colours")
elif (total_time > 100 and total_time <= 105):
    print ("\n Provincial half colour")
elif (total_time >= 105 and total_time <=110):
    print ("\n Provincial Scroll")
else:
    print("\n No award")



print("Enter credit principal:")
p = float(input())
print("Enter count of periods:")
n = float(input())
print("Enter your credit interest:")
i = float(input()) / 100 * (1/12)
a = p * ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
print("Your payment = {}!".format(math.ceil(a)))