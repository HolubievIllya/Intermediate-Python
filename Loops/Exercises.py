# TASK 1

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    print(offset)
    offset = offset - 1

# TASK 2

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 1:
      offset -= 1
    else : 
      offset += 1
    print(offset)

# TASK 3

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

# TASK 4

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for a, b in enumerate(areas):
    print(f"room {a}: {b}")

# TASK 5

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

# TASK 6

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for i in house:
    print(f"the {i[0]} is {i[1]} sqm")

# TASK 7

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() :
    print("the capital of" + key + "is" + str(value))

# TASK 8

# Import numpy as np
import numpy as np

# For loop over np_height
for i in np.nditer(np_height):
    print(f"{i} inches")

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)

# TASK 9 

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# TASK 10

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ":", row["cars_per_cap"])

# TASK 11

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

# TASK 12

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

