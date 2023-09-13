**CS_4320 Simple Software Design Change**

MegaMillions was establised in May 2002. There are drawings every Tuesday and Friday.

If we average 52 Tuesdays and 52 Fridays per year, there have been ~2,200 total drawings.

The numbers 57-75 were added in October 2013. Since October 2013, there have been around 1,500 drawings. This means that the numbers 57-75 were only available in ~68% of drawings

This means that for 32% of the drawings, the probability of drawing a number between 57-75 was 0, which is severely skewing the data

My solution would be to only include the data from Ocotber 2013-Present. This way the data is not estimated at all and each number should have a similar probability of being drawn

The Way I implemented this was by creating a new csv file (megamillinons13.csv) with data from 2013-Present. Then I changed the data variable in megamillions-from-apriori.py to reference the new csv file
