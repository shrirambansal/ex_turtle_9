"""
Write a program to check whether an years is leap year or not.
"""
year = int(input("Enter the Year : "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
else :
    print("Not Leap Year")
