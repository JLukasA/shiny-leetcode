""" DataFrame report
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+

Write a solution to reshape the data so that each row represents sales data for a product in a specific quarter.

The result format is in the following example. """
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars = ['product'], var_name ='quarter', value_name = 'sales')