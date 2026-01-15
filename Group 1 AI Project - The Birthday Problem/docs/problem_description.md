# The Birthday Problem (Birthday Paradox)

The birthday problem calculates the likelihood of at least two people in a group sharing the same birthday, assuming 365 days and uniform distribution (ignoring leap years).

**Key Result**: With 23 people, the probability exceeds 50%; with 70, it's nearly 100%.

**Mathematical Derivation**  
Complementary probability (all unique):  
P(all unique) ≈ e^{-n(n-1)/(2d)} where d=365  

P(shared) = 1 - P(all unique)  

Exact:  
P(shared) = 1 - 365! / ((365-n)! × 365^n) for n ≤ 365  

**Applications in AI**  
1. Hashing: Collisions in hash tables (e.g., Python dicts, neural embeddings)  
2. Cryptography: Birthday attacks (e.g., forging hashes in AI model security)  
3. Probabilistic Structures: Bloom filters for recommendations/NLP  
4. Simulations: Monte Carlo in RL/Bayesian AI  
5. Optimization: Duplicate detection in data pipelines