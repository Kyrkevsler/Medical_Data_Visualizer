import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('medical_examination.csv')

# Add an "overweight" column to dataset
df['BMI'] = df['weight'] / (df['height'] / 100)**2  # Create BMI column for reference
df['overweight'] = (df['BMI'] > 25).astype(int)

# Normalize the values for cholesterol and gluc
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1
                                            if x > 1 else x)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1 
                              if x > 1 else x)

def draw_cat_plot():
    '''
      Creates a categorical plot for the medical values 
    '''
    # Create a Dataframe for categorical plot using selected columns
    cols_catplot = [
        'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'
    ]
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=cols_catplot)
    df_cat["count"] = 0
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])["count"].count().reset_index(name='count')

    # Plot the values in a catplot
    catplot = sns.catplot(data=df_cat,
                          x="variable",
                          y="count",
                          hue="value",
                          col="cardio",
                          kind="bar")
    fig = catplot.fig

    # Save the figure
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    '''
      Creates a heatmap of the medical values
    '''
    # Cleaning and filtering patient segments in Dataframe
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['ap_lo'] <= df['ap_hi'])
                     & (df['height'] >= df['height'].quantile(0.025)) &
                     (df['height'] <= df['height'].quantile(0.975)) &
                     (df['weight'] >= df['weight'].quantile(0.025)) &
                     (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Create a mask for the upper triangle 
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Plot the correlation matrix
    fig, ax = plt.subplots(figsize= (10,10))
    sns.heatmap(corr, mask= mask, annot= True, cmap= 'coolwarm', fmt= ".2f", linewidths= 0.5)

    #  Save the figure
    fig.savefig('heatmap.png')
    return fig