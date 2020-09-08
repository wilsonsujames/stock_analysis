
import requests
import re

def TellBuyIndex(StockNum="1218"):
    # StockNum="1218"

    link="https://tw.stock.yahoo.com/d/s/company_"+StockNum+".html"
    r = requests.get(link )
    print(StockNum)
    print(r)
    # print("*******")
    # print()
    # print(r.text)

    link="https://tw.stock.yahoo.com/d/s/dividend_"+StockNum+".html"
    divr = requests.get(link )

    # print(r.text)
    Cash108divgex=re.compile("108年.+?/tr",re.DOTALL) 
    Cash108div = Cash108divgex.findall(divr.text)
    Cash108div=Cash108div[0].split("\n          ")
    Cash108div=Cash108div[-1]
    Cash108div=Cash108div.replace("\n        ","")
    Cash108div=Cash108div.replace('<td align="center">',"")
    Cash108div=Cash108div.replace('</td></tr',"")
    # print(Cash108div)

    Cash107divgex=re.compile("107年.+?/tr",re.DOTALL) 
    Cash107div = Cash107divgex.findall(divr.text)
    Cash107div=Cash107div[0].split("\n          ")
    Cash107div=Cash107div[-1]
    Cash107div=Cash107div.replace("\n        ","")
    Cash107div=Cash107div.replace('<td align="center">',"")
    Cash107div=Cash107div.replace('</td></tr',"")
    # print(Cash107div)

    Cash106divgex=re.compile("106年.+?/tr",re.DOTALL) 
    Cash106div = Cash106divgex.findall(divr.text)
    Cash106div=Cash106div[0].split("\n          ")
    Cash106div=Cash106div[-1]
    Cash106div=Cash106div.replace("\n        ","")
    Cash106div=Cash106div.replace('<td align="center">',"")
    Cash106div=Cash106div.replace('</td></tr',"")
    # print(Cash106div)

    Cashdiv=(float(Cash108div)+float(Cash107div)+float(Cash106div))/3

    
    # print(Cashdiv)

    Indexregex = re.compile("最近四年每股盈餘.+?股東權益報酬率",re.DOTALL) 
    Index=Indexregex.findall(r.text)

    # print(Index)
    Index=Index[0]
    Index=Index.replace("</td>","")
    Index=Index.replace("</tr>","")
    Index=Index.replace('<tr bgcolor="#FFFFFF">',"")
    Index=Index.replace('<td height="25" bgcolor="#FFFAE8">',"")
    Index=Index.replace('<td align="center">',"")
    Index=Index.replace('<td bgcolor="#FFFAE8">',"")
    Index=Index.replace('<td height="25" bgcolor="#FFFAE8" align="left">',"")
    Index=Index.replace('最近四年每股盈餘\n      \n      \n        ',"")
    Index=Index.replace('\n      \n      \n        股東權益報酬率',"")
    # Index=Index.replace('\n      ',"")
    Index=Index.split("\n        ")

    # print(Index)

    y108=Index[5].replace("元\n      \n      ","")
    # print("108年:")
    # print(y108)

    y107=Index[11].replace("元\n      \n      ","")
    # print("y107年:")
    # print(y107)

    y106=Index[17].replace("元\n      \n      ","")
    # print("y106年:")
    # print(y106)

    # y105=Index[23].replace("元","")
    # print("y105年:")
    # print(y105)

    earn3Y=(float(y108)+float(y107)+float(y106))/3
    earn3Y=round(earn3Y,3)
    # print("***")
    # print(earn3Y)

    # 三年內賺錢能力 / 現在股價
    # 三年內 股利股息


    link="https://tw.stock.yahoo.com/q/q?s="+StockNum
    r = requests.get(link )
    # print(r.text)

    Priceregex = re.compile("加到投資組合.+?成交彙整",re.DOTALL) 
    StockPrice=Priceregex.findall(r.text)

    StockPrice=StockPrice[0].split("\n                ")
    # print(StockPrice[2])
    StockPrice=StockPrice[2].replace('<td align="center" bgcolor="#FFFfff" nowrap><b>',"")
    StockPrice=StockPrice.replace('</b></td>','')
    # print(StockPrice)

    BuyIndex= round(earn3Y / float(StockPrice),2)
    # print(BuyIndex)
    Cashdiv=round(Cashdiv / float(StockPrice),2)

    return Cashdiv,BuyIndex

# TellBuyIndex("1101")    