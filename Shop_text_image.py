import matplotlib.pyplot as plt
import pandas as pd
import os
import PIL
from PIL import Image, ImageDraw, ImageFont
import math

img=plt.imread('./bowl.jpg')
plt.imshow(img)
#plt.show()
list=pd.read_excel('./excel.xlsx',engine='openpyxl')

for i in range(len(list)):
   if str(list.iloc[i,1]) == 'nan':
        pass
   else:
        print(list.iloc[i,1])
        #아이템 폴더
        print(os.path.isdir('./output/'+list.iloc[i][1]))

        if str(os.path.isdir('./output/'+list.iloc[i][1])) == 'True':
            pass
        else:
            os.makedirs('./output/'+list.iloc[i][1])

        target_image = Image.open('./bowl.jpg')  # 일단 기본배경폼 이미지를 open 합니다.
        fontsFolder = './'  # 글자로 쓸 폰트 경로
        selectedFont = ImageFont.truetype(os.path.join(fontsFolder, 'malgun.ttf'), 12)  # 폰트경로과 사이즈를 설정해줍니다.
        draw = ImageDraw.Draw(target_image)
        draw.text((182,3922), list.iloc[i][1], fill = "black", font = selectedFont, align = 'center')  # fill= 속성은 무슨 색으로 채울지 설정,font=는 자신이 설정한 폰트 설정
        draw.text((182,4012), list.iloc[i][7], fill = "black", font = selectedFont, align = 'center')
        draw.text((182,4130), list.iloc[i][6], fill = "black", font = selectedFont, align = 'center')
        draw.text((542,4012), list.iloc[i][3], fill = "black", font = selectedFont, align = 'center')
        draw.text((542,4130), list.iloc[i][5], fill = "black", font = selectedFont, align = 'center')

        add_image = Image.open(str(list.iloc[i,0]))
        w,h = add_image.size
        if h > 834:
            fixed_height = 820
            height_percent = (fixed_height / float(add_image.size[1]))
            width_size = int((float(add_image.size[0]) * float(height_percent)))
            add_image = add_image.resize((width_size, fixed_height), PIL.Image.NEAREST)

        if add_image.size[0] > 780 :
            fixed_width = 770
            width_percent = (fixed_width / float(add_image.size[0]))
            height_size = int((float(add_image.size[1]) * float(width_percent)))
            add_image = add_image.resize((fixed_width, height_size), PIL.Image.NEAREST)

        aw = (780 - add_image.size[0])/2
        ah = (834 - add_image.size[1])/2
        ah2 = (883 - add_image.size[1])/2
        target_image.paste(im=add_image, box=(math.ceil(aw), math.ceil(ah + 2823)))

        target_image.paste(im=add_image, box=(math.ceil(aw), math.ceil(ah2 + 168)))

        target_image.save('./output/' + str(list.iloc[i,1])+ '/' + str(list.iloc[i,2])+'.jpg')  # 편집된 이미지를 저장합니다.
