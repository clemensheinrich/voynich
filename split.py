import os, sys
from PIL import Image

# image constants
REGIONSIZE = (256, 256)

def derive_filename(original, region):
    parts = original.split('.')
    middle = "-{}-{}-{}-{}".format(region[0],region[1], region[2], region[3])
    return parts[0] + '.' + parts[1] + middle + '.' + parts[2]

def crop_paste_save(from_img, from_region, to_region, to_filename):
    to_img = Image.new(from_img.mode, (256, 256))
    src = from_img.crop(from_region)
    to_img.paste(src, to_region)
    to_img.save(to_filename, 'jpeg')

def region_gen(img_xmax, img_ymax, region_width, region_height):
    # current values
    x = 0
    y = 0
    w = region_width
    h = region_height
    
    while y < img_ymax:
        while x < img_xmax:
        
            # yield current region
            yield (x, y, x + w - 1, y + h - 1)
            
            # next region in x
            x = x + w
        # next region in y
        y = y + h
        # reset x 
        x = 0
           

def split_image_into_regions(name, from_img):
    gen = region_gen(from_img.size[0], from_img.size[1], REGIONSIZE[0], REGIONSIZE[1])
    num_img = 0
    # generator over image blocks
    for from_region in gen:
        crop_paste_save(from_img, from_region, (0, 0, 255, 255), derive_filename(name, from_region))
        num_img = num_img + 1
    return num_img

def download_files_from_internet_archive_site(dest_path):
    # download from orginal source
    URL_INTERNET_ARCHIVE = 'https://archive.org/download/voynich/'
    
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    # images are named as 001.jpg ... 213.jpg    
    for id in ids: https://archive.org/download/voynich/001.jpg
        
    

def main():
    
    # settings
    PATH_ROOT = '.'
    PATH_ORIGINALS = os.path.join(PATH_ROOT, 'originals')
    
    # filenames as list of lists representing images in con secutive order
    FILENAMES = [
        ['7.1006116.jpg', '7.1006117.jpg']
    ]
    
    # download files from internet archive
    download_files_from_internet_archive_site(PATH_ORIGINALS) 
        
    
    for file in FILES:
        try:
            # with Image.open(file) as img:
            #     num_parts = split_image_into_regions(file, img)
            #     print( 'file: ' + file + ' ' + str(img.size[0]) + 'x' + str(img.size[1]) + 'px split into parts: ' + str(num_parts))
                
        except IOError as ioerr:
            print('ERROR (type: IOError): ' + str(ioerr))
        except Exception as excp:
            print('ERROR (type: Exception): ' + str(excp))
            

if __name__ == '__main__':
    main()
    
    