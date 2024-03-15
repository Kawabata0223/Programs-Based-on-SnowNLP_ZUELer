import base64
from PIL import Image
import io


output_width = 1000  # 调整后的宽度
output_height = 750  # 调整后的高度

image_path1 = 'scatter/scatters.png'

with open(image_path1, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    # 将调整大小后的图片编码为Base64格式
    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image1 = base64.b64encode(buffered.getvalue()).decode('utf-8')



with open('bar/bars.png', 'rb') as image_file2:
    encoded_image2 = base64.b64encode(image_file2.read()).decode('utf-8')



output_width = 1000
output_height = 1000

image_path3 = 'wordc1oud/wordcloud_SnowNLP.png'

with open(image_path3, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image3 = base64.b64encode(buffered.getvalue()).decode('utf-8')



output_width = 1000
output_height = 800

image_path4 = 'joyp1ot/joyplot.png'

with open(image_path4, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image4 = base64.b64encode(buffered.getvalue()).decode('utf-8')



output_width = 1000
output_height = 750

image_path5 = 'pie/pie.png'

with open(image_path5, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image5 = base64.b64encode(buffered.getvalue()).decode('utf-8')


#---------------------------------------------------


# 构建HTML代码
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary Based on SnowNLP</title>
    <style>
        h1 {{
            font-size: 50px;  /* 设置中文标题的字体大小，单位可以根据需要调整 */
            margin-left: 20px; 
        }}
        
    </style>
</head>
<body>
    <h1>散点图</h1>
    <img src="data:image/jpeg;base64,{encoded_image1}" alt="Embedded Image">
    <h1>饼图</h1>
    <img src="data:image/jpeg;base64,{encoded_image5}" alt="Embedded Image">
    <h1>条形图</h1>
    <img src="data:image/jpeg;base64,{encoded_image2}" alt="Embedded Image">
    <h1>山脊图</h1>
    <img src="data:image/jpeg;base64,{encoded_image4}" alt="Embedded Image">
    <h1>词云图</h1>
    <img src="data:image/jpeg;base64,{encoded_image3}" alt="Embedded Image">
    
    <h1>点击下面的链接下载Excel文件</h1>
    <a href="labels/comments_score.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">总文件</a><br>
    <a href="labels/label1.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">label1</a><br>
    <a href="labels/label2.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">label2</a><br>
    <a href="labels/label3.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">label3</a><br>
    <a href="labels/label4.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">label4</a><br>
    <a href="labels/label5.xlsx" download="filename.xlsx" style="font-size: 40px; margin-left: 20px;">label5</a><br>

    

    
</body>
</html>
'''

# 将HTML代码写入文件
with open('SnowNLP_Summary.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print("报告创建完成")












