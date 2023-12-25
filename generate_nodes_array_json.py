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

        # 画像読み込み
        im = Image.open(image_file)
        data = im.getdata()
        arr2d = np.array(list(data))

        # 平均RGB/HSV算出
        ave_r = np.average(arr2d[0:,0])
        ave_g = np.average(arr2d[0:,1])
        ave_b = np.average(arr2d[0:,2])
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
            'image': image_file,
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
