# Updated Apriori Code

## The main issue is derivided from the life of balls 57-75
## Currently the balls have the same life span as balls 1-56
## However this is not accurate, as these balls have only been available since 2013-October

# Solution

## The solution I found was that by splitting these balls into their own seperate list, and assigning them each their own life span.
## Doing this allows you to create more accurate probabiltity odds, as now every number is being determined using correct variables.


# Psuedo Code

## 2. Define the column names that represent the lottery numbers (e.g., 'Number 1', 'Number 2', ...).

## 3. Determine the maximum number present in the dataset.

## 4. Define the introduction dates of balls 1-56 and balls 57-75.

## 5. Create dictionaries and lists to store the frequency and cumulative frequency of each number for 1-56 and 57-75.

## 6. Iterate through each row of the data:
    a. Extract the date of the draw.
    b. For each number column:
        - Extract the number.
        - If the number is not null and within the valid range:
            - Check the introduction date of the number:
                - If it's 1-56 and the draw date is after the introduction date:
                    - Update the frequency and cumulative frequency for 1-56.
                - If it's 57-75 and the draw date is after the introduction date:
                    - Update the frequency and cumulative frequency for 57-75.

## 7. Calculate the total number of draws in the previous 1 year for balls 1-56 and 57-75 separately.

## 8. Calculate the probability of each number occurring in the previous 1 year for 1-56 and 57-75 separately.

## 9. Combine the probabilities of numbers 1-56 and 57-75.

## 10. Sort the numbers by their probability in descending order.

## 11. Display the probabilities of each number occurring in the previous 1 year.

## 12. Generate a bar chart to visualize the probability of each number and save it to a file.

## 13. Save the most frequent numbers by week, month, quarter, and year to a file.

## 14. Generate and save the cumulative frequency for each number by week, month, and year.

