import pandas as pd
import matplotlib.pyplot as plt


excel_file_path = 'labels/comments_score.xlsx'
df = pd.read_excel(excel_file_path)


y = df.iloc[1:, 1]


plt.scatter(range(1, len(y) + 1), y)  # x轴为数据点的序号
plt.xlabel('Data Point')
plt.ylabel('Emotional Values')
plt.title('Scatter Plot of Emotional Values')
plt.savefig("scatter/scatters.png")


plt.clf()

print("散点图绘制完成")


