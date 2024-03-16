# creating a data frame from 2D list 
#https://leetcode.com/problems/create-a-dataframe-from-list/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    column_names=["student_id", "age"]
    df=pd.DataFrame(student_data, columns=column_names)
    print(df)
    return df