""" Table: Transactions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].

 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order. """

import pandas as pd
import numpy as np

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    
    transactions['trans_date'] = transactions['trans_date'].map(lambda x: x.strftime('%Y-%m'))
    transactions['approved_count'] = np.where( (transactions['state'] == 'approved'), 1, 0)
    transactions['approved_amount'] = np.where ( (transactions['state'] == 'approved'), transactions['amount'], 0)

    df = transactions.groupby(['trans_date', 'country'], sort=False, dropna=False).agg(
        trans_count = ('state', 'count'),
        approved_count = ('approved_count', 'sum'),
        trans_total_amount = ('amount', 'sum'),
        approved_total_amount = ('approved_amount', 'sum')
        ).reset_index()
    
    df = df.rename(columns={'trans_date':'month'})
    return df