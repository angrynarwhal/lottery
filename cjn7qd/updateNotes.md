            Simple Software Design Change
          ---------------------------------

In order to compensate for the more recent introduction of the 57-75 balls, I took the easiest and most statistically sound path: removing all data prior to October 19th, 2013. The "megamillions.csv" file found in this directory has been modified according to this standard. If there is a statistically significant disparity in number frequency caused by the dynamics of the drawing mechanism (i.e. the weight of the number paint leading to consistent differences in their collisions), then the introudction of an additional 20 balls would alter the entire dynamic. The increased likelihood is not inherent to any specific ball, rather it is a consequence of the interactions of the whole system.

As such, the "megamillions-from-apriori.py" file did not require modification. It is reading from the version of "megamillions.csv" found in this directory, so the data path was already correct.
