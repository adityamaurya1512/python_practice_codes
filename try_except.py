try:
    file=open("a_file.txt")
except FileNotFoundError as error_message:
    file = open("a_file.txt","w")
    print(f"file not found error")
finally:
    print("your file is ready")