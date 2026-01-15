# Time & Space Complexity Comparison

**Brute-Force (Pairwise)**: O(n²) time, O(n) space  
- Compare every pair  
- No early exit  

**Hash-Set**: O(n) expected time, O(n) space  
- Track seen birthdays  
- Stops on first duplicate  

| Aspect        | Brute Force | Hash Set      |  
|---------------|-------------|---------------|  
| Approach      | All pairs   | Seen set      |  
| Time          | O(n²)       | O(n) expected |  
| Space         | O(n)        | O(n)          |  
| Early Exit    | ❌          | ✅            |  
| Scalability   | Poor        | Excellent     |  
| Practical Use | ❌          | ✅            |  