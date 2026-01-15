"""
space_complexity.py
Measures approximate peak memory usage for brute-force vs hash-set birthday collision detection
Requires: pip install memory-profiler
"""

from memory_profiler import memory_usage
import random

def birthday_bruteforce(n):
    birthdays = [random.randint(1, 365) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if birthdays[i] == birthdays[j]:
                return True
    return False


def birthday_hashset(n):
    seen = set()
    for _ in range(n):
        birthday = random.randint(1, 365)
        if birthday in seen:
            return True
        seen.add(birthday)
    return False


def measure_memory(func, n=5000):
    # Warm-up run (optional but helps stability)
    func(n)
    
    # Measure peak during actual run
    peak_mem = memory_usage((func, (n,)), interval=0.01, max_usage=True)
    return peak_mem  # returns float (peak memory in MiB)


if __name__ == "__main__":
    n = 5000  # adjust based on your machine (too large → may take time or OOM)

    print(f"\nMeasuring peak memory for n = {n:,} people\n")

    print("Brute-force version...")
    mem_bf = measure_memory(birthday_bruteforce, n)
    print(f"Brute Force Peak Memory: {mem_bf:.1f} MiB\n")

    print("Hash-set version...")
    mem_hs = measure_memory(birthday_hashset, n)
    print(f"Hash Set Peak Memory:    {mem_hs:.1f} MiB\n")

    diff = mem_bf - mem_hs
    print(f"Difference: {diff:+.1f} MiB")
    if abs(diff) < 5:
        print("→ Memory usage is very similar (normal for this problem)")
    elif diff > 0:
        print("→ Hash-set used noticeably less memory")
    else:
        print("→ Brute-force used less memory (small difference)")