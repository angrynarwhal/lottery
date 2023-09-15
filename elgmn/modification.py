# Instead of having cumulative_frequency measure total number of appearances for each number
# it'll measure average number of appearances for the years that the number is in play.
# Wikipedia tells me that the numbers were 1-56 from the start up to and including October 18, 2013.
# It was then superseded by 1-75 from October 22, 2013 to October 27, 2017.
# This was followed by the current 1-70, starting from October 31, 2017.
# So for the numbers 1-56, we'll divide each frequency by (July 28, 2023) - (May 17, 2002).
# The numbers 57-70 will be divided by (July 28, 2023) - (October 22, 2013).
# Finally, the numbers 70-75 will be divided by (October 27, 2017) - (October 22, 2013).
# Since timedelta only supports totalSeconds, we'll have to do some multiplication to get
# numbers that aren't super small. Let's say 86400, to get the number of days?
# (In the end I went with 86400 * 100000 so that there are no decimals in the plot. Looks nicer that way.)
# (Of course, you can modify scaling_factor to change how the plot looks.)
# (To maybe make the changes easier to spot, changes are on lines 6, 10, and 47-60.)