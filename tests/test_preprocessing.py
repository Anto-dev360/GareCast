"""
tests/test_preprocessing.py

Unit tests for the data preprocessing functions of the GareCast project.
"""

import pandas as pd
import pytest
from src.core.preprocessing import redistribute_annual_to_weekly

def test_redistribute_annual_to_weekly():
    """
    Test that redistribute_annual_to_weekly correctly computes weekly passengers
    by dividing the annual total by 52.
    """
    # Prepare sample input dataframe
    data = {
        "annee": [2023, 2024],
        "total_voyageurs": [5200, 10400]
    }
    df_input = pd.DataFrame(data)

    # Call the function
    df_output = redistribute_annual_to_weekly(df_input)

    # Check output is a DataFrame
    assert isinstance(df_output, pd.DataFrame)

    # Check new column exists
    assert "weekly_passengers" in df_output.columns

    # Check weekly passengers calculation
    expected_values = df_input["total_voyageurs"] / 52
    expected_values.name = "weekly_passengers"
    pd.testing.assert_series_equal(df_output["weekly_passengers"], expected_values)

    # Optional: check original columns unchanged
    pd.testing.assert_series_equal(df_output["annee"], df_input["annee"])
    pd.testing.assert_series_equal(df_output["total_voyageurs"], df_input["total_voyageurs"])