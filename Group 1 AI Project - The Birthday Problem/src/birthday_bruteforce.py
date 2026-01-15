import random
import time

def birthday_bruteforce(n):
    birthdays = [random.randint(1, 365) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if birthdays[i] == birthdays[j]:
                return True
    return False

if __name__ == "__main__":
    n = 1000
    start = time.time()
    result = birthday_bruteforce(n)
    print("Brute Force Result (collision?):", result)
    print("Time:", time.time() - start)