import jieba
# 下载 pip install jieba
import pandas as pd
import wordcloud
# 下载 pip install wordcloud==1.8.2.2

# 使用pandas读取csv文件
df = pd.read_csv("评论.csv")
text = "".join([str(i) for i in df["评论"]])

# 使用结巴分词切分这一大段内容
s = " ".join(jieba.lcut(text))
print(s)

# 词云图
word = wordcloud.WordCloud(
    font_path="C:\Windows\Fonts\simhei.ttf",
    width=400,
    height=300,
    background_color="white"
)
word.generate(s)
word.to_file("抖音评论词云图.png")
