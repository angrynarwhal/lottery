Here is my suggested algorithm for calculating the frequencies.

For each number that appears in the data,
    Determine the first and last occurence
    For each unit of time you wish to measure average occurence in,
        Divide time from first to last occurence into segments of time unit and remove the remainder number of days from consideration
        Count occurences of number in each segment of time line
        Average occurence counts

This process will more accurately normalize the data regardless of when numbers where added/taken out of available powerball numbers.