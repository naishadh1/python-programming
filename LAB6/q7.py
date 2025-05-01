print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
tuple = (1, 2, 3, 4)
newtuple = ()


for i in range(len(tuple)):
    if i == 2:  
        continue
    newtuple += (tuple[i],)

print("Tuple after deletion:", newtuple)
