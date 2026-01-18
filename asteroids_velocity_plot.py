from asteroids import clean_data
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

df = pd.DataFrame(clean_data)

SD = st.stdev(df["velocity_km_s"])
mean_velocity = st.mean(df["velocity_km_s"])

bins = 20

hazardous = df[df["hazardous"]]["velocity_km_s"]
non_hazardous = df[~df["hazardous"]]["velocity_km_s"]

# Using matplotlib, a histogram plot is created,  compiling all asteroids
# from the outlined dates, sorting them based on diameter and whether
# they posed a threat to Earth.
plt.figure()
plt.hist(hazardous, bins=bins, alpha=0.6, label="Potentially Hazardous")
plt.hist(non_hazardous, bins=bins, alpha=0.6, label="Not Hazardous")

plt.xlabel("Estimated Velocity (km/s)")
plt.ylabel("Number of Asteroids")
plt.title("Asteroid Velocity Distribution (7-Day Window)")
plt.legend()
plt.show()
