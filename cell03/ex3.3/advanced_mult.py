inp = 0
while inp < 11:
    print(f"Table de {inp}:", end=" ")
    i = 0
    while i < 11:
        print(f"{inp * i}", end=" ")
        i += 1
    print()
    inp += 1