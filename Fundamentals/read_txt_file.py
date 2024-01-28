# Open and read txt file example
# opening filename "Text_Example" in "r" read mode
file = open("Text_Example.txt", "r")
first_line = file.readline()
all_text = file.read()
print()
print(first_line, end="") # Get rid of the extra \n of readline()
print("----------------------------------------")
print(all_text)
file.close()

print("*************************************************")
print("*************************************************")
# Now reading WITH
# With will handle the close ALWAYS, "rt" for read text mode
with open("Text_Example.txt", "rt") as f:
    # Using a for loop to read each line
    for line in f:
        print(line, end='') # Get rid of extra \n from print
