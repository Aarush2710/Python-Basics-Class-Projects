a=int(input("enter the marks of english  "))
b=int(input("enter the marks of hindi  "))
c=int(input("enter the marks of marathi  "))
d=int(input("enter the marks of maths  "))
e=int(input("enter the marks of science "))
f=int(input("enter the marks of ss  "))
total=a+b+c+d+e+f
percentage=(total/180)*100
print(percentage)
if percentage<=100 and percentage>=81:
    print("A+ very good,Exllent!!!!")
elif  percentage<=80 and percentage>=61:
    print("B+ Good")
elif  percentage<=60 and percentage>=41:
    print("C Ok")
else:  
    print("F very very very very Bad,If i was the teacher I will fail you sorry you are failed, I do not need to fail you")