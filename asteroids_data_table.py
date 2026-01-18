from asteroids import clean_data
import pandas as pd
import statistics as st

# This file cleanly prints a table of all
# relevant data.
df = pd.DataFrame(clean_data)

SD_velocity = st.stdev(df["velocity_km_s"])
mean_velocity = st.mean(df["velocity_km_s"])

SD_diameter = st.stdev(df["mean_diameter_m"])
mean_diameter = st.mean(df["mean_diameter_m"])

print(df)
print(f'Velocity Standard Deviation: {round(SD_velocity, 4)}')
print(f'Velocity Mean: {round(mean_velocity, 4)}')
print(f'Diameter Standard Deviation: {round(SD_diameter, 4)}')
print(f'Diameter Mean: {round(mean_diameter, 4)}')
