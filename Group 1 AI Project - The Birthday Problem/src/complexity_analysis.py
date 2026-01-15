"""
complexity_analysis.py
Compares TIME and SPACE for brute-force vs hash-set birthday collision detection
"""

import time
from birthday_bruteforce import birthday_bruteforce
from birthday_hashset import birthday_hashset

try:
    from memory_profiler import memory_usage
    HAS_MEMORY_PROFILER = True
except ImportError:
    HAS_MEMORY_PROFILER = False
    print("memory_profiler not installed → space stats will be skipped")
    print("Install with: pip install memory-profiler\n")


def compare(n=2000, time_runs=15):
    print(f"\n=== Birthday Collision Detection Comparison (n={n:,}) ===\n")

    # ─── Time ────────────────────────────────────────────────────────────────
    print("Measuring TIME (average of {} runs)...".format(time_runs))

    # Brute force time
    bf_times = []
    for _ in range(time_runs):
        start = time.perf_counter()
        birthday_bruteforce(n)
        bf_times.append(time.perf_counter() - start)
    bf_time_avg = sum(bf_times) / time_runs

    # Hash set time
    hs_times = []
    for _ in range(time_runs):
        start = time.perf_counter()
        birthday_hashset(n)
        hs_times.append(time.perf_counter() - start)
    hs_time_avg = sum(hs_times) / time_runs

    print(f"Brute Force Avg Time: {bf_time_avg:.6f} seconds")
    print(f"Hash Set Avg Time:    {hs_time_avg:.6f} seconds")
    print(f"Hash Set is {bf_time_avg / hs_time_avg:.1f}x faster\n")

    # ─── Space ───────────────────────────────────────────────────────────────
    if HAS_MEMORY_PROFILER:
        print("Measuring SPACE (peak memory)...")

        # Brute force memory
        mem_bf = max(memory_usage(lambda: birthday_bruteforce(n), interval=0.01))
        print(f"Brute Force Peak Memory: {mem_bf:.1f} MiB")

        # Hash set memory
        mem_hs = max(memory_usage(lambda: birthday_hashset(n), interval=0.01))
        print(f"Hash Set Peak Memory:    {mem_hs:.1f} MiB")

        diff = mem_bf - mem_hs
        print(f"Memory difference: {diff:+.1f} MiB")
    else:
        print("Space measurement skipped (install memory_profiler for full results)")


if __name__ == "__main__":
    compare(n=2000, time_runs=15)  # adjust n if needed