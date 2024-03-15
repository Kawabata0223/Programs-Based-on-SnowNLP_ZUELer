import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_length(file_path):

    df = pd.read_excel(file_path)
    first_column = df.iloc[1:, 0]

    return len(first_column)


length1 = get_length('labels/label1.xlsx')
length2 = get_length('labels/label2.xlsx')
length3 = get_length('labels/label3.xlsx')
length4 = get_length('labels/label4.xlsx')
length5 = get_length('labels/label5.xlsx')


categories = ['0-0.2', '0.2-0.4', '0.4-0.6', '0.6-0.8','0.8-1.0']
values = [length1,length2,length3,length4,length5]


# 设置渐变颜色
colors = plt.cm.Reds(np.linspace(0.2, 1, len(categories)))
#colors = plt.cm.Blues(np.linspace(0.2, 1, len(categories)))
#colors = plt.cm.Greens(np.linspace(0.2, 1, len(categories)))


bar_width = 0.5


fig, ax = plt.subplots(figsize=(11, 7))  # Adjust the width and height as needed


ax.barh(categories, values, color=colors, height=bar_width)


ax.set_xlabel('Quantity', fontsize=17)
ax.set_ylabel('Emotional Value Categories', fontsize=17)


# 使网格在条形图后面
ax.set_axisbelow(True)
ax.grid(True, which='major', linestyle='--', linewidth=0.5)


plt.savefig('bar/Bars.png')

#plt.show()

print("条形图绘制完成")

