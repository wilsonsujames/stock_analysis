import OneP
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

df=pd.read_csv('stock_id.csv')  
# print(df.head())

# print(df["證券代號"])

# print(type(df["證券代號"]))

CashDivArr=[]
BuyIndexArr=[]

for stockId in df["證券代號"]:
    # print(stockId)
    time.sleep(1)
    try:
        BuyIndex=OneP.TellBuyIndex(stockId)
        CashDivArr.append(BuyIndex[0])
        BuyIndexArr.append(BuyIndex[1])
        if BuyIndex[0] >= 0.1 and BuyIndex[1] >= 0.1:
            with open("JackPOT.txt","a") as f:
                f.write(stockId+"\n")
            
            # print("JackPOT:")
            # print(stockId)
    except:
        pass



plt.scatter(CashDivArr, BuyIndexArr)
plt.show()


# BuyIndex=OneP.TellBuyIndex("2882")
# print()
# print(BuyIndex)