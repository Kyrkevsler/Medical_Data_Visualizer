# Medical Data Visualization
## Data Description
The dataset provided `medical_examination.csv` contains information about patients, including body measurements, results from various blood tests, and lifestyle choices. The dataset will be utilized to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

File Information:
File Name: `medical_examination.csv`

Tasks
Create a chart: Generate a chart similar to examples/Figure_1.png. Display the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with cardio= 1 and cardio= 0 in different panels.

Add an `overweight` column: Calculate BMI for each patient and determine if a person is overweight. If BMI > 25, set the overweight value to 1, otherwise 0.

Normalize the data: Make 0 always represent good and 1 always represent bad. For cholesterol and glucose variables, if the value is 1, set it to 0; if it's more than 1, set it to 1.

Draw the Categorical Plot: Convert the data into long format and create a chart that shows the value counts of the categorical features split by Cardio using seaborn's catplot().

Clean the data: Filter out incorrect data segments:

Diastolic pressure higher than systolic (Keep the correct data with df['ap_lo'] <= df['ap_hi'])
Height less than the 2.5th percentile or more than the 97.5th percentile
Weight less than the 2.5th percentile or more than the 97.5th percentile
Create a correlation matrix: Calculate the correlation matrix and plot it using seaborn's heatmap(). Mask the upper triangle of the heatmap.

Instructions
Follow the numbered instructions in the medical_data_visualizer.py file to implement each task. The unit tests are provided in test_module.py for testing your code. Use main.py for development and testing purposes.
