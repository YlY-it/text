#  1.导入
from DrissionPage import *

# 2.指定浏览器
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


# 3.在dp中配置edge浏览器
edge = ChromiumOptions().set_browser_path(path=edge_path)

# 4.在dp中使用edge浏览器,新开一个标签页
web = Chromium(edge).latest_tab

# 5.打开指定浏览器路径
web.get("https://www.12306.cn/index/")
web.ele("#fromStationText").click(by_js=True).input("武汉")
web.ele("#toStationText").click(by_js=True).input("长沙")
