# basic-renamer
A basic code in Python that allows the user to choose from different file renaming options.

In this code, we first ask the user what type of renaming they want to do by presenting a menu of choices using the input() function. Based on the user's choice, we set the new_file_name variable to the appropriate renamed file name.

For option 1, we use the upper() function to make the file name all caps. For option 2, we use the lower() function to make the file name all lowercase. For option 3, we use the title() function to capitalize the first letter of every word. For options 4-6, we use the replace() function to replace the appropriate characters with the specified replacements.

For option 7, we first split the file name into words using the split() function. We then create a new list called new_words that contains the first word in lowercase (since it shouldn't be capitalized) and the remaining words capitalized using a list comprehension. Finally, we join the words together into a single string using the join() function, and set new_file_name to the resulting camelCase file name.

After getting the new file name, we use the os.rename() function to rename the file.

-ChatGPT

*Project done with the help of ChatGPT
