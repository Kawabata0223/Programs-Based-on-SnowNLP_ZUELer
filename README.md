### 您好！下面是此项目文件的相关信息：

## 4月3日紧急更新：
万分抱歉，由于微博的变动，现用爬虫无法正常工作，但情感分析等功能仍然正常。在使用时需将Startup_SnowNLP.py中爬虫相关部分注释掉，直接对files文件夹中留有的data.csv评论数据进行分析。我们将会尽快修复爬虫功能，保证项目的完整运行。








-------

## 一、python 推荐版本：3.10


## 二、所需库：
pandas
matplotlib
numpy
json
csv
requests
time
fake_useragent
seaborn
joypy
openpyxl
snownlp
Pillow（PIL）
base64
io
jieba
wordcloud
imageio
os


## 三、项目介绍

### 本项目基于 snownlp 库，可自动爬取目标微博评论区的评论，生成相关<font color="#ff0000">数据图</font>、<font color="#ff0000">数据文件</font>和<font color="#ff0000">情感分析报告</font>以及<font color="#ff0000">标签化评论区</font>

> SnowNLP是一个基于Python的自然语言处理（NLP）库，专门设计用于处理中文文本。它提供了一系列功能，包括分词、情感分析、文本相似度计算等，旨在帮助开发者轻松地进行中文文本处理和情感分析任务。该库提供了**情感分析功能**，可以分析文本中的情感倾向，识别文本中的正面、负面或中性情感，并给出相应的**情感评分**。


> 本项目为中南财经政法大学统数学院“基于大语言模型的网络舆情态势感知研究——舆情评论的群体情绪与语义标签化分析”项目**中期研究进展情况**的部分程序文件。




## 四、使用方法

### 1. 查看目标微博的 id

![image](https://github.com/Kawabata0223/test/blob/master/pic/278919608-89dcbb20-5c15-4e84-9e72-520babbaf057.png)

> 在 examples 文件夹中有各示例帖子的 id

![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240315130233.png)


### 2. 将 Crawl_SnowNLP.py 中79行的相应位置改为目标微博的 id

![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240315132709.png)

### 3. 运行 Startup_SnowNLP.py



### 4. 直接打开 SnowNLP_Summary.html 查看分析报告



### 5. 选择 pycharm 打开 SnowNLP_Page.html，在 pycharm 中用浏览器打开，生成标签化评论区（直接点开将无法正常载入评论）

![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240315124656.png)


![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240314213154.png)


![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240314212359.png)




## 五、程序说明

![image](https://github.com/Kawabata0223/test/blob/master/pic/%E7%A8%8B%E5%BA%8F%E6%9E%B6%E6%9E%841.png)



Startup_SnowNLP.py
次序运行其他程序文件，自动生成目标微博的分析结果

Crawl_SnowNLP.py
爬取目标微博评论区，并保存为csv文件（files/data.csv）

Preprocessing.py
对csv文件进行预处理，包括添加列标题，删去空行，保存为xlsx文件（files/comments.xlsx）


label_SnowNLP.py
使用 SnowNLP 对评论逐条进行情感打分，并按得分将其均匀分为五组，相关 xlsx 文件均存入 labels 文件夹

NoHeader.py
去除comments_score.xlsx内数据的列名，为生成标签化评论区做准备

scatter_SnowNLP.py
根据分析结果，绘制情感得分散点图，呈现得分的分布样态，图片存入scatter文件夹

pie_SnowNLP.py
根据分析结果，绘制情感得分散点图，呈现得分的分布样态，图片存入pie文件夹

bar_SnowNLP.py
根据分组结果，绘制各组数量的条形图，图片存入bar文件夹

joyplot_SnowNLP.py
根据各组内部的情感得分分布情况，绘制山脊图，图片存入joyp1ot文件夹

wordcloud_SnowNLP.py
根据所有评论的文本，绘制词云图，图片存入wordc1oud文件夹

SnowNLP_Summary.py
根据以上步骤绘制的图表与数据文件，生成一份综合报告HTML文件

SnowNLP_Page.html
在 pycharm 中用浏览器打开，生成标签化评论区


## 六、示例文件

在 examples 文件夹中有各事件的数据结果，分析报告

![image](https://github.com/Kawabata0223/test/blob/master/pic/Pasted%20image%2020240315123520.png)




## 七、补充说明

如果您无法正常运行程序，烦请通过以下方式联系我，您的任何批评指正都将使我们做的更好，感谢！

QQ：2859571794
微信：koregajiyuuda


