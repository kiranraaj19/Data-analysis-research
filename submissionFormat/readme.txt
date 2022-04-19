WARNING: THE INPUT FILE SHOULD BE 'inputFile.csv'!

This model uses a Linear regression model depending on multiple variables.

Let y(total runs) depend on the variables(x2) average batsmen runrate(runs/ball), (x3) average bowlers weakness(runs scored against them/ball) and (x1) difficulty level of venue(average runs scored per match in that venue)

giving us:

y = m1*x1 + m2*x2 + m3*x3 + c

The model is trained with the past data to figure out what the approximate (m1,m2,m3,c) might be. With this information we can find out the total runs that might be scored in the future match just knowing x1,x2,x3 which can be calculated from the provided input file.


Each player and venue is represented w a numeric value which either represents their strength or weakness depending on the data. This information is stored in './used_for_hashing' file.

