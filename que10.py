# Read the address from the user
address = input("Enter your full address: ")

# Split the address by commas (assuming the user uses commas to separate parts of the address)
address_parts = address.split(',')

# Display the address on multiple lines
print("\nYour address in multiple lines:")
for part in address_parts:
    print(part.strip())

