content = ""
try:
    with open("sample.txt",'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")