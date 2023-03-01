import pandas as pd
import pandas_alive
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('annual_csv.csv')

# Extract the data for GISTEMP
df_gistemp = df[df.Source == 'GISTEMP'][['Year', 'Mean']].set_index('Year')

# Create an animated line chart using plot_animated
df_gistemp.plot_animated(kind='line', filename="temp-anomaly-over-time-line.mp4",period_fmt="%Y", title='Temperature Anomaly (1880 - 2016)', enable_progress_bar=True)

