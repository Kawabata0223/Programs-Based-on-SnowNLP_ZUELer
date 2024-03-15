import pandas as pd
from PIL import Image
import numpy as np
import jieba
from wordcloud import WordCloud,ImageColorGenerator
import imageio


file_path = 'files/stopwords.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 移除每行末尾的换行符
lines = [line.strip() for line in lines]

#-------------------------------------------

excel_file_path = 'files/comments.xlsx'
df = pd.read_excel(excel_file_path)

first_column_data = df.iloc[1:, 0]

txt_file_path = 'files/output.txt'

with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
    for item in first_column_data:
        txt_file.write(str(item) + '\n')

#-------------------------------------------

with open("files/output.txt", encoding="utf-8") as f:
    s = f.read()

# 中文分词
text = ' '.join(jieba.cut(s))


mk = imageio.imread("files/1mage.png")
image_colors = ImageColorGenerator(mk)


img = Image.open("files/1mage.png")  # 打开遮罩图片
# 生成蒙版
mask = np.array(img)  # 将图片转换为数组

# 生成WordCloud
wc = WordCloud(font_path="files/msyh.ttc",
               mask=mask,
               width=1000,
               height=800,
               background_color='white',
               max_words=200,
               collocations=False,
               color_func=image_colors,
               stopwords=lines).generate(text)


wc.to_file("wordc1oud/wordcloud_SnowNLP.png")

print("词云图绘制完成")

