from clean import clean_data

if __name__ == '__main__':

    images_base_path = r'E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\origin_unzip'
    clean_labels_path = r'E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\clean_labels'
    clean_images_base_path = r'E:\Tin\code\3.dataset\1.ir_vis_dataset\Kaist\clean_images'

    clean_data(images_base_path, clean_labels_path, clean_images_base_path)
    print('Clean data finished')
