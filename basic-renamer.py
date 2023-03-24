import os

# Get a list of all files in the current directory
files = os.listdir()

# Ask the user what type of renaming they want to do
renaming_type = input("What type of renaming do you want to do? Choose one of the following:\n"
                      "1. All caps\n"
                      "2. All lowercase\n"
                      "3. Capitalize first letter of every word\n"
                      "4. Replace underscore for dash\n"
                      "5. Replace underscore for space\n"
                      "6. Replace dash for underscore\n"
                      "7. Replace dash for space\n"
                      "8. Replace space for underscore\n"
                      "9. Replace space for dash\n"
                      "10. Text in camelCase\n"
                      "11. Replace a portion of the file name\n"
                      "Enter the number of your choice: ")

# Ask the user for the old and new parts of the file name to replace
if renaming_type == "11":
    old_part = input("Enter the old part of the file name to replace: ")
    new_part = input("Enter the new part of the file name to replace it with: ")

# Loop through each file
for file in files:
    # If it's a file (not a directory)
    if os.path.isfile(file):
        # Get the new file name based on the user's choice
        if renaming_type == "1":
            new_file_name = file.upper()
        elif renaming_type == "2":
            new_file_name = file.lower()
        elif renaming_type == "3":
            new_file_name = file.title()
        elif renaming_type == "4":
            new_file_name = file.replace("_", "-")
        elif renaming_type == "5":
            new_file_name = file.replace("_", " ")
        elif renaming_type == "6":
            new_file_name = file.replace("-", "_")
        elif renaming_type == "7":
            new_file_name = file.replace("-", " ")
        elif renaming_type == "8":
            new_file_name = file.replace(" ", "_")
        elif renaming_type == "9":
            new_file_name = file.replace(" ", "-")
        elif renaming_type == "10":
            # Replace '_' and '-' with spaces before applying camelCase
            words = file.replace("_", " ").replace("-", " ").split(" ")
            new_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
            new_file_name = "".join(new_words)
        elif renaming_type == "11":
            new_file_name = file.replace(old_part, new_part)
        else:
            # If the user enters an invalid option, skip the file
            continue
        
        # Rename the file
        os.rename(file, new_file_name)
