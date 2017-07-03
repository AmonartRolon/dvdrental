
with open(input(), 'r') as f:
    o = open('output.txt', 'w')
    data = f.readlines()
    print(data)
    for line in data:
        o.write(line.replace('"', ''))
