# 1.导入自动化工具
import datetime

from  DrissionPage import *

# 创建excel文件对象
import csv
f = open("评论.csv","w",encoding="utf-8-sig")
c = csv.DictWriter(f,fieldnames=["昵称","地区","时间","评论"])
c.writeheader()

# 2.打开浏览器
driver = ChromiumPage()

# 3.打开指定网址
driver.get("https://www.douyin.com/video/7441030870259010870")

# 4.监听数据包
driver.listen.start("aweme/v1/web/comment/list")

for i in range(30):
    # 评论滚动到底部
    print(f"正在采集第{i+1}页评论内容....")
    # 5.等待数据包加载
    resp = driver.listen.wait()

    # 6.获取数据包返回的数据
    json_data = resp.response.body
    comments = json_data['comments']
    print(json_data)
    # 7.解析数据 昵称 时间 地区 评论
    for i in comments:
        driver.scroll.to_bottom()
        text = i["text"]
        create_time = i["create_time"]
        # 将日期的格式转换一下
        date = str(datetime.datetime.fromtimestamp(create_time))
        nickname = i["user"]["nickname"]
        ip_label = i["ip_label"]
        dict = {
            "昵称":nickname,
            "地区":ip_label,
            "时间":date,
            "评论":text
        }
        c.writerow(dict)