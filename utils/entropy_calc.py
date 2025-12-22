import math
from collections import Counter

def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0
    occurences = Counter(data)
    entropy = 0
    for count in occurences.values():
        p_x = count / len(data)
        entropy -= p_x * math.log2(p_x)
    return entropy