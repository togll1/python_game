from math import *

def std_weight(height,gender):
    
    if gender == "man":
        stdwei = height * height * 22
    elif gender == "girl":
        stdwei = height * height * 21
    
    stdwei = round(stdwei,2)
    return stdwei

height = int(input("몸무게 : "))
gender = input("성별 : ")
weight = std_weight(height/100,gender)

print("키{}의 {}의 평균체중은{}kg 이다".format(height,gender,weight))