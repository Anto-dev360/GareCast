"""
visualization.py

Visualization functions

Author: Anthony Morin
Created: 2025-05-23
Project: GareCast
License: MIT
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_affluence_by_week(df, gare_name):
    """
    Display a line plot showing weekly affluence for a specific station.

    Args:
        df (pd.DataFrame): DataFrame containing 'week' and 'passenger_count' columns.
        gare_name (str): Name of the station.
    """
    df_station = df[df['gare'] == gare_name]
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_station, x="week", y="passenger_count")
    plt.title(f"Affluence hebdomadaire – {gare_name}")
    plt.xlabel("Semaine")
    plt.ylabel("Nombre de voyageurs")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
