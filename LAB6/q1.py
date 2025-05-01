print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
list = ["trisha" ,"maya", ("jai" ,"veeru"),"jaya"]
a = len(list)
c=0
d=0
for i in list:
    if isinstance(i,tuple):
        c+=len(i)
    else:
        d+=1
print(f"The number of boys are {c}")
print(f"The number of girls are {d}")