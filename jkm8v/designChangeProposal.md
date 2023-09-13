Joseph Kelley

CS4320

Simple Software Design Change

---
### Problem
Current method of calculating number frequencies are flawed because on 10/19/2013 megamillions chagned the numebr pool to include the numbers 57-75.
https://www.megamillions.com/About.aspx

The number frequencies code does not adjust for this change so the number probabalities distribution is right-skewed instead of uniform. 

### Proposed Solution

The software solution I am proposing would take the average frequency from the first draw on 05/17/2002 to the last draw of the original matrix on 10/15/2013 and add a randomized amount about one standard deviation to the numbers 57-75, before continuing to count.

This solution is acceptable due to the fact that the megamillions drawing is inherintly random, so adding a small amount of randomness to the normalization of the data may not affect the outcomes too much.

e.g.

```python
for _, row in data.iterrows():
    date = row['date']

    ###
    # proposed pseudocode
    if(date is 10/15/2013):
        x̄, σ = getStats(number_frequency)
        for number = 57 to 75:
            number_frequency[number] = randomInRange(x̄ - σ, x̄ + σ)
    ###
    
    # Calculate the weekly frequency
    for column in number_columns:
        number = row[column]
        if pd.notnull(number):
            number = int(number)
            if 1 <= number <= max_number:  # Check if the number is within the valid range
                number_frequency[number] = number_frequency.get(number, 0) + 1

    # Calculate the cumulative frequency by month, quarter, and year
    for column in number_columns:
        number = row[column]
        if pd.notnull(number):
            number = int(number)
            if 1 <= number <= max_number:  # Check if the number is within the valid range
                cumulative_frequency[number].append((date, number_frequency[number]))
```