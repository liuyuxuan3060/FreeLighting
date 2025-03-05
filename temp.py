import os, tqdm

def list_local_dir(folder_in):
    image_path_list = []
    for srcroot, dirs, files in os.walk(folder_in):
        for file in files:
            image_path = os.path.join(srcroot, file)
            if image_path.endswith('g') or image_path.endswith('G'):
                if 'mask.png' in image_path or 'white' in image_path or 'gray' in image_path or 'shen' in image_path or 'tmp' in image_path or 'sam' in image_path or 'ref-' in image_path: continue
                image_path_list.append(image_path)
    return image_path_list

# folder_in = 'A312422288-5 20142'
# image_path_li = list_local_dir(folder_in)
# image_path_li = [x for x in image_path_li if 'seed' in x]

# for image_path in tqdm.tqdm(image_path_li):
#     basename = os.path.basename(image_path)
#     subdir = image_path.replace('/' + basename, '')
#     os.system('cp "{}" "{}"'.format(image_path, subdir + '.png'))
#     os.system('rm -rf "{}"'.format(subdir))

folder_in = '鞋静物_换背景_灯光_旋转90度-res-v3-creative-scene-relighting'
image_path_li = list_local_dir(folder_in)
image_path_li = [x for x in image_path_li if 'no-relight' in x]

for image_path in tqdm.tqdm(image_path_li):
    os.system('rm -rf "{}"'.format(image_path))
    
    
    


