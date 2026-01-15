import random
import time

def birthday_hashset(n):
    seen = set()
    for _ in range(n):
        birthday = random.randint(1, 365)
        if birthday in seen:
            return True
        seen.add(birthday)
    return False

if __name__ == "__main__":
    n = 1000
    start = time.time()
    result = birthday_hashset(n)
    print("Hash Set Result (collision?):", result)
    print("Time:", time.time() - start)