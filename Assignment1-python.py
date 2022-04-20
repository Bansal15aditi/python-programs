'''#1.print hello world in different lines.
a="hello"
b="world"
print("%s\n%s"%(a,b))
#2. print hello world in single line.
a="hello"
b="world"
print("%s %s"%(a,b))
#3. program to add two integer value.
a=int(input("enter number"))
b=int(input("enter number"))
print("sum=%d"%(a+b))
#4. program to subtract two integer value.
a=int(input("enter number"))
b=int(input("enter number"))
print("difference=%d"%(a-b))
#5. program to multiply two integers.
a=int(input("enter number"))
b=int(input("enter number"))
print("product=%d"%(a*b))
#6.program to calculate power.
a=int(input("enter number"))
b=int(input("enter number"))
print("power=%d"%(a**b))
#7.program to find area and perimeter(length and breadth input from user).
a=int(input("enter length"))
b=int(input("enter breadth"))
print("perimeter=%d"%(2*(a+b)))
print("area=%d"%(a*b))
#8.program to find area and circumference of circle.
r=float(input("enter radius"))
const=3.14
print("area = %f"%(const*r*r))
print("circumference =%f"%(2*const*r))
#9.program to find hypotenuse of right angle triangle.
b=int(input("enter base"))
p=int(input("enter height"))
h=(p**2+b**2)**(1/2)
print("hypotenuse=%d"%h)
#10.program to swap two numbers.
a=int(input("enter first value"))
b=int(input("enter second value"))
c=a
a=b
b=c
print("after swap=%d,%d"%(a,b))
#12. program to check triangle is isosceles,rightangled,scalene or invalid.
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if(a+b>c and b+c>a and c+a>b):
    if(a==b or b==c or c==a):
        print("isosceles triangle")
    elif((a*a+b*b==c*c) or (b*b+c*c==a*a) or (c*c+a*a==b*b)):
        print("right angle triangle")
    elif(a==b==c):
        print("eqilateral triangle")
    else:
        print("scalene triangle")
else:
    print("invalid triangle")
#13. program to find SI and amount.
p=float(input("enter principle"))
r=float(input("enter rate of interest"))
t=float(input("enter time"))
s=(p*r*t)/100
print("simple interest=%f"%(s))
a=s+p
print("amount=%f"%(a))
#14. program to find CI and amount.
p=float(input("enter principle"))
r=float(input("enter rate of interest"))
t=float(input("enter time"))
a=p+(1+r/100)**t
print("amount=%f"%a)
c=a-p
print("compound interest=%f"%c)'''
#15.
l=int(input("enter length of floor in cm"))
b=int(input("enter breadth of floor in cm"))
l1=int(input("enter length of tile in cm"))
b1=int(input("enter breadth of tile in cm"))
n=(l*b)//(l1*b1)
print("Number of tiles required=%d tiles"%n)
'''#16. program to input no. of overs of match,calculate total runs.
n=int(input("enter overs of match"))
n=((n-1)<<5)+n+36
print(n)
            # if else programs.
#1. check no. is even or odd.
n=int(input("enter number"))
if(n%2==0):
    print("even number")
else:
    print("odd number")
#2. program to subtract small no. from greater.
a=int(input("enter first number"))
b=int(input("enter second number"))
if(a>b):
    print("difference=%d"%(a-b))
else:
    print("difference=%d"%(b-a))
#3. find maximum between two numbers.
x=int(input("enter first no."))
y=int(input("enter second no."))
if(x>y):
    print("maximum=%d"%x)
else:
    print("maximum=%d"%y)
#4. find maximum between three numbers.
a=int(input("enter first no."))
b=int(input("enter second no."))
c=int(input("enter third no."))
if(a>b and a>c):
    print("maximum is a=%d"%a)
elif(b>a and b>c):
    print("maximum is b=%d"%b)
else:
    print("maximum is c=%d"%c)
#5. program to check number is +ve,-ve or 0.
n=int(input("enter number"))
if(n>0):
    print("positive number")
elif(n<0):
    print("negative number")
else:
    print("number is zero")
#6.program to check no. is divisible by 5 and 11 or not.
n=int(input("enter number"))
if(n%5==0 and n%11==0):
    print("divisible")
else:
    print("not divisible")
#7. check no. is even or odd.
n=int(input("enter number"))
if(n%2==0):
    print("even number")
else:
    print("odd number")
#8. check whether year is leap or not.
n=int(input("enter year"))
if(n%4==0):
    print("leap year")
else:
    print("not leap year")
#9. check whether character is alphabet or not.
ch=input()
if((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')):
    print("alphabet")
else:
    print("not alphabet")
#10. check alphabet is vowel or consonant.
ch=input()
if(ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U'or ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u'):
    print("vowel")
elif((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')):
    print("cosonants")
else:
    print("not alphabet")
#11. program to input week no. and print week day.
day=int(input("enter week number grom 1-7"))
if(day==1):
    print("monday")
elif(day==2):
    print("tuesday")
elif(day==3):
    print("wednesday")
elif(day==4):
    print("thursday")
elif(day==5):
    print("friday")
elif(day==6):
    print("saturday")
elif(day==7):
    print("sunday")
else:
    print("invalid day in week")
#12. program to input month number and print no. of days in that month.
m=int(input("enter month"))
y=int(input("enter year"))
if((m==2) and (y%4==0) or ((y%100==0) and (y%400==0))):
    print("no. of days is 29")
elif(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("no. of days is 31")
elif(m==2):
    print("no. of days is 28")
else:
    print("no. of days is 30")
#14. input angle and check triangle is valid or not.
a=int(input("enter angle of triangle"))
b=int(input("enter angle of triangle"))
c=int(input("enter angle of triangle"))
if(a>0 and b>0 and c>0 and a+b+c==180):
    print("triangle valid")
else:
    print("not valid")
#15. input sides and check triangle is valid or not.
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if(a+b>c or b+c>c or c+a>b):
    print("triangle valid")
else:
    print("not valid")
#16. program to check triangle is isosceles,eqilateral,scalene or invalid.
a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))
if(a+b>c and b+c>a and c+a>b):
    if(a==b or b==c or c==a):
        print("isosceles triangle")
    elif(a==b==c):
        print("eqilateral triangle")
    else:
        print("scalene triangle")
else:
    print("invalid triangle")
#17. program to find roots of quadratic equation.
a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
if(d>=0):
    print("real and distinct roots")
elif(d==0):
    print("real and equal roots")
else:
    print("imaginary roots")
#18.program to calculate profit and loss.
sp=int(input("enter sell price"))
cp=int(input("enter cost price"))
if(sp>cp):
    p=(sp-cp)/cp*100
    print("profit=%d"%p)
else:
    l=(cp-sp)/cp*100
    print("loss=%d"%l)
#19.program to input marks and calculate percentage and grade.
a=int(input("enter maths marks"))
b=int(input("enter physics marks"))
c=int(input("enter chemistry marks"))
d=int(input("enter english marks"))
e=int(input("enter computer marks"))
p=(a+b+c+d+e)/500*100
if(p>=90):
    print("grade A")
elif(p>=80):
    print("grade B")
elif(p>=70):
    print("grade C")
elif(p>=60):
    print("grade D")
elif(p>=40):
    print("grade E")
else:
    print("grade F")
#20. program to input basic salary and calculate gross salary.
ba=int(input("enter basic salary"))
if(ba<=10000):
    h=ba*20//100
    d=ba*80//100
    g=ba+h+d
elif(ba<=20000):
    h=ba*25/100
    d=ba*90//100
    g=ba+h+d
elif(ba>20000):
    h=ba*30//100
    d=ba*95//100
    g=ba+h+d
print("gross salary=%d"%g)
#21. input electricity units and calculate total electricity bill
u=int(input("enter unit"))
if(u<=50):
    b=u*0.50
elif(u<=150):
    b=50*0.50+(u-50)*0.75
elif(u<=250):
    b=50*0.50+100*0.75+(u-150)*1.20
else:
    b=50*0.50+100*0.75+100*1.20+(u-250)*1.50
b=b+b*20/100
print(b)
#22. a man has certain apples WAP that identifies the min. no. of apples.
a=int(input("enter number of apples"))
if(a%7==0 and a%6==1 and a%5==1 and a%4==1 and a%3==1 and a%2==1):
    print("valid apples")
else:
    print("invalid apples")
#23. program to find how many two wheeler and four wheeler need to manufacture.
v=int(input("enter number of vehicles"))
w=int(input("enter number of wheels"))
y=((w//2)-(v))
x=w//2-2*((w//2)-v)
print("tw=%d"%x)
print("fw=%d"%y)'''