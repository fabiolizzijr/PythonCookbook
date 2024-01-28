# Example of string functions
# Using .lower(), .uppercase(), .replace(),
# .find(), .join(), .split(), .isdigit()

banner = "FreeFloat FTP server"

# Use of upper() to make it upper case
print(banner.upper())

# Use of lower() to make it lower case
print(banner.lower())

# Replace a text for other, oldTxt, newTxt
print(banner.replace("FreeFloat", "Ability"))

# Find to encounter first occurrence of a given str
print(banner.find('FTP'))

# Join the iterable/collection this way: separator.join(iterable)
print('*'.join(banner))

# Remove whitespace from the beginning
print(banner.strip())

# Split hte iterable, creating a list using the separator in .split(separator)
print(banner.split(" "))

# Return True if all characters are digits
digits = "1234"
print(digits.isdigit())
print(banner.isdigit())
