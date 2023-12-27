import colorsys
import glob
import json
import math
import pathlib

import numpy as np
from PIL import Image


JSON_FILE_NAME = 'nodes_array.json.js'
NODE_SIZE = 10
ZOOM_RATIO = NODE_SIZE/2
OFFSET_REF_ID = 1000000000
IMAGE_WIDTH = 100


def rotateImage(img, orientation):
    """
    画像ファイルをOrientationの値に応じて回転させる
    """
    #orientationの値に応じて画像を回転させる
    if orientation == 1:
        pass
    elif orientation == 2:
        #左右反転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        #180度回転
        img_rotate = img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        #上下反転
        img_rotate = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        #左右反転して90度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
    elif orientation == 6:
        #270度回転
        img_rotate = img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        #左右反転して270度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    elif orientation == 8:
        #90度回転
        img_rotate = img.transpose(Image.ROTATE_90)
    else:
        pass

    return img_rotate


if __name__ == '__main__':
    image_files = glob.glob('./images/**/*.jpg', recursive=True) + glob.glob('./images/**/*.JPG', recursive=True) + glob.glob('./images/**/*.jpeg', recursive=True)
    image_files = list(set(image_files))
    image_files = sorted(image_files)
    #image_files = glob.glob('./refs/*.png')

    data_size = len(image_files)
    json_data = []
    for index, image_file in enumerate(image_files):
        id = index + 1
        print(f'{id}/{data_size}')

        # 画像読み込み ⇒ 画像縮小
        im = Image.open(image_file)
        new_height = int(im.height * IMAGE_WIDTH / im.width)
        im_resize = im.resize((IMAGE_WIDTH, new_height))
        data = im_resize.getdata()
        arr2d = np.array(list(data))
        try:
            exifinfo = im._getexif()
            orientation = exifinfo.get(0x112, 1)
            im_resize = rotateImage(im_resize, orientation)
        except:
            pass
        thumbnail_file = f'./thumbnail/{index}.jpg'
        im_resize.save(thumbnail_file)

        # 中央重点係数作成
        coef = []
        image_height = int(arr2d.shape[0] / IMAGE_WIDTH)
        center_x = float((IMAGE_WIDTH - 1) / 2)
        center_y = float((image_height - 1) / 2)
        max_dist = max(center_x, center_y)
        for y in range(0, image_height):
          for x in range(0, IMAGE_WIDTH):
              dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
              angle = math.atan(dist / max_dist)
              coef.append(math.cos(angle))
        coef_np = np.array(coef)
        sum_coef = np.sum(coef_np)

        # 中央重点で平均RGB/HSV算出
        ave_r = np.sum(arr2d[0:,0] * coef_np) / sum_coef
        ave_g = np.sum(arr2d[0:,1] * coef_np) / sum_coef
        ave_b = np.sum(arr2d[0:,2] * coef_np) / sum_coef
        ave_h, ave_s, ave_v = colorsys.rgb_to_hsv(ave_r/255,ave_g/255,ave_b/255)
        ave_h = int(360 * ave_h)
        ave_s = int(100 * ave_s)
        ave_v = int(100 * ave_v)

        # 座標計算
        x = ave_s * math.cos(math.pi * (90 - ave_h) / 180)
        y = -ave_s * math.sin(math.pi * (90 - ave_h) / 180)

        # 結果格納
        json_data.append({
            'id': id,
            'shape': "image",
            'size': NODE_SIZE,
            'fixed': {
                'x': True,
                'y': True,
            },
            'image': thumbnail_file,
            'clipboard': image_file,
            'title': f'{image_file}\nHSV:{ave_h},{ave_s},{ave_v}',
            'x': x * ZOOM_RATIO,
            'y': y * ZOOM_RATIO,
            })

    # json書き出し
    json_path = pathlib.Path(JSON_FILE_NAME)
    with json_path.open('w') as fj:
        fj.write('NODES_ARRAY = ')
        json.dump(json_data, fj, ensure_ascii=True, indent=2)
        fj.write(';')
