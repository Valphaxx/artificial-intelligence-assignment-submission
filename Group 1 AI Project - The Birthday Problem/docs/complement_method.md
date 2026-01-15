# Birthday Problem: Using the Complement (Detailed)

Directly calculating "at least one match" is complex due to overlapping cases. Use the complement: all birthdays unique.

**Steps**:  
1. First person: 365/365 = 1  
2. Second: 364/365  
3. Third: 363/365  
...  
n-th: (365 - n + 1)/365  

P(all unique) = product of above  

P(shared) = 1 - P(all unique)  

**Why it works**:  
- Clear decreasing pattern  
- No enumeration of matches  
- Easy for computation/exams