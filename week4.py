# This program reads a file, changes the text to UPPERCASE,
# and saves it in a new file. It also handles errors.

def main():
    # Ask the user for the file name
    filename = input("Enter the name of the file you want to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Change the text to uppercase
        modified_content = content.upper()

        # Create a new file name
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        # Let the user know the process is complete
        print(f"Done! The modified text is saved in '{new_filename}'.")

    except FileNotFoundError:
        # If the file is not found, show this message
        print("Error: The file was not found. Please check the name and try again.")

    except Exception as e:
        # If another error happens, show this message
        print("Something went wrong:", e)

# Start the program
main()
