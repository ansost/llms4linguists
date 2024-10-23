import random
import time

train = [
    [0, 0],
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8],
]
train_count = len(train)

def loss(w, b):
    result = 0.0
    for i in range(train_count):
        x = train[i][0]
        y = x * w + b
        d = y - train[i][1]
        result = result + d * d
    result = result/train_count
    return result

if __name__ == "__main__":
    random.seed(int(time.time()))
    w = random.random() * 10.0
    b = random.random() * 5.0

    eps = 1e-3
    rate = 1e-3

    print(f"{loss(w, b)}")
    for i in range(500):
        c = loss(w, b)
        dw = (loss(w + eps, b) - c) / eps
        db = (loss(w, b + eps) - c) / eps
        w = w - rate * dw
        b = b - rate * db
        print(f"loss = {loss(w, b)}, w = {w}, b = {b}")

    print("------------------------------")
    print(f"w = {w}, b = {b}")
