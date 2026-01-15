# Birthday Paradox Project

This project explores the **Birthday Problem** (also known as the Birthday Paradox):  
**How many people are needed in a room so that the probability of at least two sharing the same birthday exceeds 50%?**  
(Assuming 365 days in a year, uniform distribution, ignoring leap years.)

### Key Result (the famous surprise)
With only **23 people**, the probability is already ≈ **50.7%** — much lower than most people's intuition.

With **70 people**, it approaches **99.9%**.

### Project Contents

- **Implementations** of two collision-detection methods:
  - Brute-force pairwise comparison → O(n²) time
  - Hash-set based detection → O(n) expected time
- **Time & Space Complexity Comparison** (measured on real runs)
- **Matplotlib visualization** of the probability curve
- **Recursive exploration simulation** (showing how collisions emerge in a search-like process)

### Measured Results (n = 5,000 people)

**Time** (average over multiple runs):
- Brute-force: significantly slower (exact value depends on machine)
- Hash-set: dramatically faster (often 100–500× speedup in practice)

**Space** (peak memory usage):
- Brute Force Peak Memory: **24.8 MiB**
- Hash Set Peak Memory:    **24.8 MiB**
- Difference: **-0.0 MiB**  
→ Memory usage is **very similar** — normal for this problem size, as both store roughly the same amount of data (list vs set of integers).

### Files Overview

birthday-paradox-project/
├── README.md
├── requirements.txt
├── src/
│   ├── birthday_bruteforce.py
│   ├── birthday_hashset.py
│   ├── complexity_analysis.py
│   ├── space_complexity.py
│   └── visualize_birthday_recursive.py
├── docs/
│   ├── problem_description.md
│   ├── complement_method.md
│   └── complexity_comparison.md
├── Presentation/
│   └── Birthday_Paradox_Presentation.pptx
├── images/
│   ├── cake.png
│   └── birthday_probability_curve.png
├── main.py
└── Person.py

### Requirements

```bash
pip install -r requirements.txt
```

### How to Run

### 1. See time

``` bash
python src/complexity_analysis.py
```

### 2. See time comparison

``` bash
python src/complexity_analysis.py
```

### 3. See space/memory usage

``` bash
python src/space_complexity.py
```

### 4. Watch the probability curve + recursive exploration animation

``` bash
python src/visualize_birthday_recursive.py
```

→ Shows people being added, first collision highlighted, theoretical curve, and recursion tree of attempts.

### Key Insights
- Time: Hash-set wins dramatically — constant-time lookups make it scale much better.
- Space: Almost identical in practice — both methods need to store up to n birthdays.
- Probability intuition: Humans greatly underestimate how quickly collisions occur in large possibility spaces.
- AI relevance: Same principle underlies hash collisions, birthday attacks in cryptography, Bloom filter sizing, etc.

### Group Members
- Fouad Abdulhakeem - 20233277
- Einstein Dokpesi - 20233068
- Jad Chouaib - 20233011
- Oladipupo Oyewobi Benedict - 20233037
- Onogbeye Joseph - 20233502
- Okopido Imeobong - 20233418
- Hassan Kalili - 20233491
- Nweke Okechukwu - 20233357
- Oyiborhoro Samuel - 20233321
- Michael Afegbua - 20231148
- Abdulaziz Abubakar Sayyadi - 20233050
- Metu Lotana - 20231056

