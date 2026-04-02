def read_config(filename):
    try:
        with open(filename,'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
            print(f"File not found: {filename}")

filename = input("Enter file name: ")
read_config(filename)