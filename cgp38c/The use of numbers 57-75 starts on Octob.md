The use of numbers 57-75 starts on October-22-2013
according to the data and the data in the csv file
this means that these numbers were only used in 54%
of winning numbers

we can normalize the frequency of these numbers by
adding a function that will multiply the probabilities
of the numbers 57-75 by about 1.85 and the other numbers by 0.746

number_probabilities = {number: (freq * 1.85 if number >= 57 else freq * 0.746) / total_draws_1_year for number, freq in number_frequency.items()}

replace line 51 with the code above
