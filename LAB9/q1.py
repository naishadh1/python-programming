print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
str = ''
def upp_low(str):
    str = input("Enter a string")
    a=b=c=0
    for i in str:
        if i.isupper()==True:
            a+=1
        
        else:
            c+=1
    dict ={"Uppercase" : a , "Lowercase":c}
    print(dict)
upp_low(str)
