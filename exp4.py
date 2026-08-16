import heapq
import math

class Node:
    def __init__(self, message, freq):
        self.message = message
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
   
def generate_codes(node, code="", codes={}):
    if node is None:
        return

    if node.message is not None:
        codes[node.message] = code

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes

n = int(input("Enter number of messages: "))

messages = []
frequencies = []

for i in range(n):
    msg = input("Enter message: ")
    freq = float(input("Enter probability: "))
    messages.append(msg)
    frequencies.append(freq)
   
heap = []

for msg, freq in zip(messages, frequencies):
    heapq.heappush(heap, Node(msg, freq))

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new = Node(None, left.freq + right.freq)
    new.left = left
    new.right = right

    heapq.heappush(heap, new)

root = heap[0]

codes = generate_codes(root)

print("\nHuffman Codes")
print("------------------------------------------")
print("Message\tProbability\tCode")

for msg, freq in zip(messages, frequencies):
    print(f"{msg}\t{freq}\t\t{codes[msg]}")

L = 0
for msg, freq in zip(messages, frequencies):
    L += freq * len(codes[msg])

H = 0
for freq in frequencies:
    H += -freq * math.log2(freq)

efficiency = (H / L) * 100
redundancy = 100 - efficiency

print("\n------------------------------------------")
print("Entropy (H) =", round(H, 4), "bits")
print("Average Code Length (L) =", round(L, 4), "bits")
print("Code Efficiency =", round(efficiency, 2), "%")
print("Redundancy =", round(redundancy, 2), "%")