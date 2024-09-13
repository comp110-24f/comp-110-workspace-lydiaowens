age: int = 10
age = age + 1
print(age)

x: int = 1
x = x + 1
print(x)

name: str = input("What is your name?")
if len(name) > 6:
    print("Do you have a nickname?")
elif name == "Alyssa":
    print("You must love Comp 110!")
else:
    print("Nice to meet you," + name)
