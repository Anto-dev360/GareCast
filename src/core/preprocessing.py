"""
preprocessing.py

Data cleaning and feature engineering functions.

Author: Anthony Morin
Created: 2025-05-23
Project: GareCast
License: MIT
"""

def redistribute_annual_to_weekly(df, year_col="annee", total_col="total_voyageurs"):
    """
    Estimate weekly passenger flow by dividing annual total by 52 weeks.

    Args:
        df (pd.DataFrame): Raw SNCF dataset.
        year_col (str): Name of the year column.
        total_col (str): Name of the total passengers column.

    Returns:
        pd.DataFrame: Weekly-level estimated passenger flow data.
    """
    df_weekly = df.copy()
    df_weekly["weekly_passengers"] = df_weekly[total_col] / 52
    return df_weekly
