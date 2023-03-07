import os

# Get a list of all files in the current directory
files = os.listdir()

# Ask the user what type of renaming they want to do
renaming_type = input("What type of renaming do you want to do? Choose one of the following:\n"
                      "1. All caps\n"
                      "2. All lowercase\n"
                      "3. Capitalize first letter of every word\n"
                      "4. Replace _ for - or space\n"
                      "5. Replace - for _ or space\n"
                      "6. Replace spaces for _ or -\n"
                      "7. Text in camelCase\n"
                      "Enter the number of your choice: ")

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
            new_file_name = file.replace("_", "-").replace(" ", "-")
        elif renaming_type == "5":
            new_file_name = file.replace("-", "_").replace(" ", "_")
        elif renaming_type == "6":
            new_file_name = file.replace(" ", "-").replace("_", "-")
        elif renaming_type == "7":
            words = file.split(" ")
            new_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
            new_file_name = "".join(new_words)
        
        # Rename the file
        os.rename(file, new_file_name)
