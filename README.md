# Global Temperature Anomaly Animation

This program creates an animated line chart using the [pandas_alive](https://github.com/JackMcKew/pandas_alive) library to visualize global temperature anomaly data from the GISTEMP dataset.

## Requirements

- pandas
- pandas_alive
- matplotlib
- ffmpeg

## Usage

1. Download or clone this repository to your local machine.
2. Place your temperature anomaly data in a CSV file named 'annual_csv.csv' in the same directory as the script.
3. Run the script `app.py`.
4. An animated line chart named 'temp-anomaly-over-time-line.mp4' will be saved in the same directory.

## Details

The program reads in the CSV file 'annual_csv.csv' using the pandas library, selects the rows where the column 'Source' is equal to 'GISTEMP' and extracts the columns 'Year' and 'Mean' as a new dataframe, `df_gistemp`. 

Then, it creates an animated line chart using the `plot_animated` method of the `df_gistemp` dataframe, which is provided by the `pandas_alive` library. The chart is saved as an mp4 file named 'temp-anomaly-over-time-line.mp4' in the current working directory.

The `kind` parameter is set to 'line' to create a line chart, `period_fmt` is set to "%Y" to display the years in the format of 4 digits (e.g., 1880), `title` sets the title of the chart to 'Global Temperature Anomaly (1880 - 2016)', and `enable_progress_bar` adds a progress bar to the chart. Finally, `period_label` is set to False to remove the period label from the chart. 

## License

This project is licensed under the MIT License..

