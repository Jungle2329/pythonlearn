from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# im = Image.open('getcontent.png')
im =Image.open('c:/users/administrator/desktop/Screenshot_2.png')
w, h = im.size
print('w=%s,h=%s' % (w, h))

# 输出大小
im.thumbnail((w/2, h/2))
im.save('c:/users/administrator/desktop/Screenshot_2-1.png', 'png')


# 模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('thumbnail.png', 'png')


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
