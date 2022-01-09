from genericpath import isdir
from ntpath import join
import os
import shutil
from tqdm import tqdm


def clean_data(images_base_path, clean_labels_path, clean_images_base_path):

    # 1.读取标签路径
    labels_folders = os.listdir(clean_labels_path)

    # 2.创建新地址，分解标签，变成路径，移动label图像到新地址，修改名称（防止重名）

    #   1.创建新地址
    clean_images_ir_path = os.path.join(clean_images_base_path, 'ir')
    if not os.path.isdir(clean_images_ir_path):
        os.makedirs(clean_images_ir_path)

    clean_images_vis_path = os.path.join(clean_images_base_path, 'vis')
    if not os.path.isdir(clean_images_vis_path):
        os.makedirs(clean_images_vis_path)

    # 原有基地址：images_base_path = r'E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\origin_unzip'
    # 已有标签：把标签内容变成可用地址
    # 目标基地址：clean_images_base_path = r'E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\clean_images'
    # 正常地址示例： E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\origin_unzip\set00\V000\lwir\I00000.jpg

    for i, label in enumerate(tqdm(labels_folders)):
        #   2.分解标签
        # 如果label = 'set00_V000_I01225.txt'，则label_split = ['set00', 'V000', 'I01225.txt']
        label_split = label.split('_')
        # 去掉第三个的'.txt',变为['set00', 'V000', 'I01225']
        label_split[2] = label_split[2].replace('.txt', '')
        # 找到新地址
        clean_images_ir_path = os.path.join(clean_images_base_path, 'ir')
        clean_images_vis_path = os.path.join(clean_images_base_path, 'vis')

        #   3.把标签变成路径
        label_image_ir = os.path.join(
            images_base_path, label_split[0], label_split[1], 'lwir', label_split[2]) + '.jpg'
        label_image_vis = os.path.join(
            images_base_path, label_split[0], label_split[1], 'visible', label_split[2]) + '.jpg'

        #   4.移动label图像到新地址
        if os.path.exists(label_image_ir) and os.path.exists(label_image_vis):
            new_path_ir = shutil.copy(
                label_image_ir, clean_images_ir_path)         # 返回新地址
            new_path_vis = shutil.copy(
                label_image_vis, clean_images_vis_path)      # 返回新地址

        #   5.修改名称
        [ir_path, _] = os.path.split(new_path_ir)
        [vis_path, _] = os.path.split(new_path_vis)

        if not os.path.exists(os.path.join(ir_path, str(i+1))+'.jpg'):
            os.rename(new_path_ir, os.path.join(ir_path, str(i+1))+'.jpg')
        if not os.path.exists(os.path.join(vis_path, str(i+1))+'.jpg'):
            os.rename(new_path_vis, os.path.join(vis_path, str(i+1))+'.jpg')
