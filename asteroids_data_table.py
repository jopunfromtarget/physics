from asteroids import clean_data
import pandas as pd

# This file cleanly prints a table of all
# relevant data.
df = pd.DataFrame(clean_data)
print(df)