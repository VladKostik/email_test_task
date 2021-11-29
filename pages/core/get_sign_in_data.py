with open('../pages/core/data', 'r') as file:
    lines = file.readlines()
    email = lines[0]
    password = lines[1]
    for line in lines:
        print(line)

file.close()
