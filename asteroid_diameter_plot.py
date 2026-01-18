from asteroids import clean_data
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(clean_data)

bins = 20

hazardous = df[df["hazardous"]]["mean_diameter_m"]
non_hazardous = df[~df["hazardous"]]["mean_diameter_m"]

# Using matplotlib, a histogram plot is created,  compiling all asteroids
# from the outlined dates, sorting them based on diameter and whether
# they posed a threat to Earth.
plt.figure()
plt.hist(hazardous, bins=bins, alpha=0.6, label="Potentially Hazardous")
plt.hist(non_hazardous, bins=bins, alpha=0.6, label="Not Hazardous")

plt.xlabel("Estimated Diameter (m)")
plt.ylabel("Number of Asteroids")
plt.title("Asteroid Diameter Distribution (7-Day Window)")
plt.legend()
plt.show()
