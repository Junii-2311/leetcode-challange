#Finding Rows and columns in a DataFrame
#https://leetcode.com/problems/get-the-size-of-a-dataframe/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(players)
    num_rows, num_columns = df.shape
    return [num_rows, num_columns]