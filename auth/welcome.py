import random
import os

def generate_random_number():
    # Generate four random numbers between 0 and 255
    numbers = [str(random.randint(0, 255)) for _ in range(4)]

    # Generate a random number between 0 and 32 for the subnet mask
    subnet_mask = str(random.randint(0, 32))

    # Format the numbers with leading zeros and join them with dots
    ip_address = '.'.join([num.zfill(3) for num in numbers])

    # Format the IP address and subnet mask in the desired format
    result = f"{ip_address}/" + subnet_mask.zfill(2)

    return result

random_number = generate_random_number()

# Create the auth folder if it doesn't exist
folder_path = "auth"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Save the random number to a text file in the auth folder
filename = os.path.join(folder_path, "ip_address.txt")
with open(filename, 'w') as file:
    file.write(random_number)

print("IP Address:", random_number)
print("IP Address at: ", filename)