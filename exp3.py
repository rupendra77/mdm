import math

message = input("Enter the message: ")
total_length = len(message)
counts = {}

# Count character frequencies
for character in message:
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1

print("\n--- Character Analysis ---")
print("Character counts:", counts)
print("Number of unique characters:", len(counts))

entropy = 0
print(f"\nMessage: {message}")
print("\nInformation per character:")

# Calculate and display metrics
for character, count in counts.items():
    probability = count / total_length
    information = -math.log2(probability)
    
    # Visualizing metrics per character
    print(f"'{character}' -> Probability: {probability:.2f} | Information: {information:.2f} bits")
    
    # Accruing entropy formula: H(X) = -sum(P(x) * log2(P(x)))
    entropy += probability * information

print("\n--- Total Source Metric ---")
print(f"Average Entropy: {entropy:.2f} bits per character")
