#!/usr/bin/python
# -*- coding:utf-8 -*-

from os import listdir, path
from os.path import abspath, dirname, isfile, join, isdir
import json
from PIL import Image

if __name__ == '__main__':

    # Variables
    src_dir = dirname(abspath(__file__))
    images_dir = join(src_dir, "images")
    json_path = join(src_dir, "TestImage.json")
    remote_base_url = "https://raw.githubusercontent.com/gumob/ImageExtractTest/master/images/"

    extensions = [
        '.png',
        '.jpg',
        '.gif',
        '.tif',
        '.tiff',
        '.bmp',
        '.webp'
    ]
    dataset = {
        'png': [],
        'jpg': [],
        'gif': [],
        'tif': [],
        'bmp': [],
        'webp': [],
        'invalid_ext': [],
    }

    for img_dir_name in listdir(images_dir):
        img_dir_path = join(images_dir, img_dir_name)
        
        if isdir(img_dir_path) and not img_dir_name == 'invalid_bytedata':
            for infile_filename in listdir(img_dir_path):

                infile_path = join(img_dir_path, infile_filename)
                infile_basename, infile_ext = path.splitext(infile_filename)

                if isfile(infile_path) and any(ext in infile_ext for ext in extensions):
                    with Image.open(infile_path) as img:
                        width, height = img.size

                        remote_url = join(remote_base_url, img_dir_name, infile_filename)

                        print(remote_url, width, height)

                        if img_dir_name == "jpg":
                            dataset['jpg'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "png":
                            dataset['png'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "gif":
                            dataset['gif'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "tif":
                            dataset['tif'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "bmp":
                            dataset['bmp'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "webp":
                            dataset['webp'].append({'url': remote_url, 'size': [width, height]})
                        elif img_dir_name == "invalid-ext":
                            dataset['invalid_ext'].append({'url': remote_url, 'size': [width, height]})

    with open(json_path, 'w') as f:
        json.dump(dataset, f, indent=4)
