#TASK 1=>
def read_print_file():
    filename = "sample.txt"

    try:
        with open(filename,'r') as file:
            print(f"--- Reading {filename} ---")

            for line in file:
                print(line,end='')
            print(line,end='')

    except FileNotFoundError:
        print("\n\n --- End of file ---")
        print(f"Error: The file '{filename}' was not found. ")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_print_file()

#TASH 2=>
def file_operations_demo():
    filename = "output.txt"

    try:
        print("--- Step 1: Writing to file ---")
        user_input = input("Enter text to write to the file: ")

        with open(filename, "w") as file:
            file.write(user_input + "\n")  # Adding \n to ensure next line starts on a new line
        print(f"Successfully wrote to '{filename}'.")


        print("\n--- Step 2: Appending to file ---")
        append_input = input("Enter additional text to append: ")

        with open(filename, "a") as file:
            file.write(append_input + "\n")
        print(f"Successfully appended to '{filename}'.")


        print("\n--- Step 3: Reading final content ---")

        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content Start ---")
            print(content.strip())
            print("--- File Content End ---")

    except IOError as e:
        print(f"An error occurred during file operations: {e}")



if __name__ == "__main__":
    file_operations_demo()