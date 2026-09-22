import sys
if len(sys.argv) < 2 or 'z' not in sys.argv[1]:
    print("none")
else:
    txts = sys.argv[1]
    find_z = ""
    for txt in txts:
        if 'z' in txt:
            find_z = find_z + 'z'
    print(find_z)
    
