def modify_file_content(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as file:
            file.write(modified_content)

        print(f"Success! The modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don't have access to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

filename = input("Enter the filename to read: ")
modify_file_content(filename)


processed_content = content.upper()

with open("output.txt", "w") as file:
    file.write(processed_content)
    file.write(f"\nWORD COUNT: {word_count}\n")

print("Processing complete! The output has been saved to output.txt.")
