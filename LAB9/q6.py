print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
print("Name: Naishadhsinh Kumpavat")
print("Roll No: 24BEE112")
def generate_tuples(n):
    return [(x, x**2, x**3) for x in range(1, n + 1)]


end_value = int(input("Enter the ending value: "))
result = generate_tuples(end_value)
print(result)


    