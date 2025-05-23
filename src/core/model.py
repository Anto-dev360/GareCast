"""
model.py

Neural network model definition and training logic using Keras.

Author: Anthony Morin
Created: 2025-05-23
Project: GareCast
License: MIT
"""

from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


def build_model(input_dim):
    """
    Build and compile a simple dense neural network for regression.

    Args:
        input_dim (int): Number of features (input dimensions).

    Returns:
        keras.Model: Compiled Keras regression model.
    """
    model = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1)  # Output layer for regression
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
    return model
