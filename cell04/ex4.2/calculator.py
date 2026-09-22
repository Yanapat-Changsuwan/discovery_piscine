inp1 = int(input("Give me the first number: "))
inp2 = int(input("Give me the second number: "))
print("Thank you!")
print(f"{inp1} + {inp2} = {inp1 + inp2}")
print(f"{inp1} - {inp2} = {inp1 - inp2}")
if inp1 % inp2 == 0:
    print(f"{inp1} / {inp2} = {inp1 // inp2}")
else:
    print(f"{inp1} / {inp2} = {inp1 / inp2}")
print(f"{inp1} * {inp2} = {inp1 * inp2}")