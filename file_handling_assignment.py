def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("1. Welcome to PLP Academy.\n")
            file.write("2. This is a python week 5 assignment.\n")
            file.write("3. It is about file handling in python.\n")
    except PermissionError:
        print("Permission denied to create the file.")
    finally:
        print("File creation completed.")

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents in my file:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    else:
        print("An error occurred while displaying the file.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("4. So far the python classes at PLP Academy are interesting!\n")
            file.write("5. I Love the PLP instructors' dedication.\n")
            file.write("6. I enjoy programming with python!\n")
    except PermissionError:
        print("Permission denied to append to the file.")
    finally:
        print("Appending completed.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()
    read_and_display()
