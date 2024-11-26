import datetime

from  DrissionPage import *

import csv
f = open("智联招聘.csv","w",encoding="utf-8-sig")
c = csv.DictWriter(f,fieldnames=["职位","公司","薪资","学历","经验","城市","区域","街道","公司领域","公司性质","公司规模","岗位职责"])
c.writeheader()

driver = ChromiumPage()

driver.get("https://www.zhaopin.com/sou/jl530/p1")

driver.listen.start(" fe-api.zhaopin.com/c/i/search/positions")
resp = driver.listen.wait()
json_data = resp.response.body
comments = json_data['comments']
print(json_data)
