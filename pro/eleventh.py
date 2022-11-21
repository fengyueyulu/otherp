import xlwt
import json
from collections import OrderedDict

with open("../text/city.txt",encoding="utf-8")as fp:
    jeson_text=OrderedDict(json.load(fp))

wb=xlwt.Workbook()
ws=wb.add_sheet("city")
row=0

for k,v in jeson_text.items():
    ws.write(row,0,k)
    ws.write(row,1,v)
    row+=1
wb.save('../text/city.xls')