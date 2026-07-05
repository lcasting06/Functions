def circleArea(radius):
    pi = 3.1416
    area = pi * (radius ** 2)
    return area

def totalDue(money, tax):
    total = money + (money * tax)
    return total

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

radius = float(input("Enter the radius: "))
print("%.2f" % circleArea(radius))

money = float(input("Enter the amount of money: "))
taxPercent = float(input("Enter the tax rate (%): "))
taxRate = taxPercent / 100
print("%.2f" % totalDue(money, taxRate))

fahrenheit = float(input("Enter the Fahrenheit temperature: "))
print("%.6g" % fahrenheitToCelsius(fahrenheit))
