import math
def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-12  # Small value to avoid log(0)
    y_pred = max(min(y_pred, 1 - epsilon), epsilon)  # Clip predictions
    return - (y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred))

print("Binary Cross-Entropy Loss:", end=' ')
print(binary_cross_entropy(1, 0.9))