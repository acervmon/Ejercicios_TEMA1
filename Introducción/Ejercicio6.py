cadena = "zereP nauJ,01"

# Split the string into name and grade
name, grade = cadena[::-1].split(',')

# Format the string
formatted_string = f"{name[::-1]} ha sacado un Nota de {grade[::-1]}."

# Print the formatted string
print(formatted_string)
