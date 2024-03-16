# extract spcific number of rows from DataFrame
# https://leetcode.com/problems/display-the-first-three-rows/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df= employees
    return df.head(3)  # write number of rows in the "head" function to extract the top rows
    