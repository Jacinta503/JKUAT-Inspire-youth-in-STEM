def my_function ():
    print("hello from function")
my_function

def greetings (user_name):
    return " Hello" +  user_name
print(greetings("Francisca"))

def greetings(user_name):
    return(f"Hello {user_name}")

print(greetings("Francisca"))

# Calculate area of a circle
import math
def circle_area(radius):
    return math.pi *radius ** 2 

print(circle_area(5))

#not using math module
def circle_area(radius):
    return 3.142 * radius ** 2
