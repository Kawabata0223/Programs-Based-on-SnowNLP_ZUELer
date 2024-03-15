import seaborn as sns
import matplotlib.pyplot as plt
from joypy import joyplot
import pandas as pd


file_paths = ['labels/label1.xlsx', 'labels/label2.xlsx', 'labels/label3.xlsx', 'labels/label4.xlsx', 'labels/label5.xlsx']


df = pd.read_excel('labels/label1.xlsx')
df['Category'] = 1
df.to_excel('labels/label1.xlsx', index=False)


df = pd.read_excel('labels/label2.xlsx')
df['Category'] = 2
df.to_excel('labels/label2.xlsx', index=False)


df = pd.read_excel('labels/label3.xlsx')
df['Category'] = 3
df.to_excel('labels/label3.xlsx', index=False)


df = pd.read_excel('labels/label4.xlsx')
df['Category'] = 4
df.to_excel('labels/label4.xlsx', index=False)


df = pd.read_excel('labels/label5.xlsx')
df['Category'] = 5
df.to_excel('labels/label5.xlsx', index=False)


category_column = 'Category'

all_data = pd.concat([pd.read_excel(file_path) for file_path in file_paths], ignore_index=True)

category_dict = {1: '0.0-0.2', 2: '0.2-0.4', 3: '0.4-0.6', 4: '0.6-0.8', 5: '0.8-1.0'}

all_data['category_label'] = all_data[category_column].map(category_dict)



joyplot(all_data, by='category_label', column='Unnamed: 1', figsize=(10, 8),
        colormap=sns.color_palette("viridis", as_cmap=True), alpha=0.7)


plt.xlabel('Emotional Values', fontsize=17)

plt.subplots_adjust(top=0.95, bottom=0.1)

plt.savefig('joyp1ot/joyplot.png', dpi=300)

print("山脊图绘制完成")

#plt.show()

















