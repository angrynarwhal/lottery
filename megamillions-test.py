#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the lottery data from a CSV file (replace 'megamillions.csv' with the actual file path)
# Use 'date_format' instead of 'date_parser'
data = pd.read_csv('megamillions.csv', parse_dates=['date'], date_format='%m-%d-%y')

# Assuming the numbers are represented in separate columns (e.g., 'Number 1', 'Number 2', ... 'Number N')
# You can adjust the column names according to your dataset.
number_columns = ['a', 'b', 'c', 'd', 'e']

# Determine the maximum number present in the dataset
max_number = data[number_columns].max().max()

# Create dictionaries to store the frequency of each number for 1-56 and 57-75
number_frequency_1_56 = {number: 0 for number in range(1, 57)}
number_frequency_57_75 = {number: 0 for number in range(57, 76)}

# Create a list to store the cumulative frequency for each number for 1-56 and 57-75
cumulative_frequency_1_56 = {number: [] for number in range(1, 57)}
cumulative_frequency_57_75 = {number: [] for number in range(57, 76)}

# Calculate the start date for the previous 1 year
one_year_ago = data['date'].max() - pd.DateOffset(years=1)

# Iterate through each row of the data and calculate the weekly and cumulative frequencies
for _, row in data.iterrows():
    date = row['date']
    
    # Calculate the weekly frequency
    for column in number_columns:
        number = row[column]
        if pd.notnull(number):
            number = int(number)
            if 1 <= number <= max_number:  # Check if the number is within the valid range
                if number <= 56:
                    number_frequency_1_56[number] = number_frequency_1_56.get(number, 0) + 1
                    cumulative_frequency_1_56[number].append((date, number_frequency_1_56[number]))
                else:
                    number_frequency_57_75[number] = number_frequency_57_75.get(number, 0) + 1
                    cumulative_frequency_57_75[number].append((date, number_frequency_57_75[number]))

# Calculate the total number of draws in the previous 1 year
total_draws_1_year = data[data['date'] >= one_year_ago]['date'].count()

# Calculate the probability of each number occurring in the previous 1 year for 1-56 and 57-75
number_probabilities_1_56 = {number: freq / total_draws_1_year for number, freq in number_frequency_1_56.items()}
number_probabilities_57_75 = {number: freq / total_draws_1_year for number, freq in number_frequency_57_75.items()}

# Combine the probabilities of numbers 1-56 and 57-75
number_probabilities = {**number_probabilities_1_56, **number_probabilities_57_75}

# Sort the numbers by their probability in descending order
sorted_probabilities = sorted(number_probabilities.items(), key=lambda x: x[1], reverse=True)

# Display the probabilities of each number occurring in the previous 1 year
for number, probability in sorted_probabilities:
    print(f"Number {number}: Probability = {probability:.6f}")

# ...

# ...

# Rest of the code (visualization, saving plots, etc.)
# ...
