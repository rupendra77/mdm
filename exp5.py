import numpy as np

# 1. Setup Standard (7,4) Matrices
G = np.array([[1,0,0,0,1,1,0],
              [0,1,0,0,0,1,1],
              [0,0,1,0,1,1,1],
              [0,0,0,1,1,0,1]])

H = np.array([[1,0,1,1,1,0,0],
              [1,1,1,0,0,1,0],
              [0,1,1,1,0,0,1]])

# 2. Get User Inputs
msg = np.array([int(b) for b in input("Enter 4-bit message (e.g. 1011): ")])
codeword = np.dot(msg, G) % 2

print("Generated Codeword:", "".join(map(str, codeword)))

received = np.array([int(b) for b in input("Enter 7-bit received codeword: ")])

# 3. Calculations
syndrome = np.dot(received, H.T) % 2

# Generate Error Vector Array by comparing expected vs received
error_vector = (received != codeword).astype(int)

# 4. Traverse through the array to find the error position
error_pos = -1

for i in range(len(error_vector)):
    if error_vector[i] == 1:
        error_pos = i + 1
        break  # Stop at the first error found

# 5. Display Results
print("\n--- Results ---")
print("Calculated Syndrome:", "".join(map(str, syndrome)))
print("Error Vector     :", "".join(map(str, error_vector)))

if np.all(syndrome == 0):
    print("Status           : Clean / No Errors.")
else:
    print(f"Status           : Error Detected at Position {error_pos}!")