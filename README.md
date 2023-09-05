# Sustainability_urbanisation
Building energy consumption prediction leveraging labeled data of (1) energy consumption measurement (*meter_reading*), (2) building characteristics and (3) the corresonding weather data.
It's a panel data set with approx. 1500 unique buildings, with data across the entirety of 2016, recorded on an hourly basis. (Source: https://we.tl/t-NuFrNvbCuU)

The two files contain Python Notebooks, with an overview of the overall analytics process, with the intention of convenient and time-friendly code evaluation. Note that the data should still be downloaded from the link above, and manually linked to the notebook by specifying the data source filepath in the notebook's first part (variable "data_filepath").

--- 
Notebook stucture:
- Part 0: Import raw data (Specify data filepath here)
- Part 1: Exploratory analysis (Summary statistics, Outliers, Segmentation, Trend/Seasonality)
- Part 2: Feature engineering (Parsing, Scaling, Missing data, Seasonality)
- Part 3: Model specification (OLS, LASSO, Random Forest)
- Part 4: Performance evaluation

