"""
Adds geo location and date-time to the bottom right of all the images specified
in a directory and its subdirectories.

Note:
    - The new output will overwrite the existing one
    - It is assumed that the output folder already exists
    - Error checking and handling is not done
"""

import exif
from PIL import Image, ImageDraw, ImageFont
from os import walk
from tqdm import tqdm


def get_watermark_text(path_in):
    """
    Returns a string that defines the text for the watermark
        path_in (string) - The path of the input image
    Returns:
        string
    """
    def convert_to_degrees(value):
        return value[0] + value[1]/60 + value[2]/3600

    with open(path_in, 'rb') as image_file:
        exif_data = exif.Image(image_file)
        watermark_text_template = '{:.5f} N, {:.5f} E, {}'
        print(exif_data.gps_longitude_ref)

        watermark_text = watermark_text_template.format(
            convert_to_degrees(exif_data.gps_latitude),
            convert_to_degrees(exif_data.gps_longitude),
            exif_data.datetime)
    return watermark_text


def add_watermark(path_in, path_out):
    """
    Adds watermark text to the image and saves it at the given location
        path_in (string) - The path of the input image
        path_out (string) - The path where the output image is to be generated
    """
    im = Image.open(path_in)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = get_watermark_text(path_in)
    font = ImageFont.truetype('arial.ttf', 100)
    textwidth, textheight = draw.textsize(text, font)

    margin = 40
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)
    im.save(path_out)


if __name__ == "__main__":
    base_path_in = "input"
    base_path_out = "output"

    walk_data = walk(base_path_in)
    filename_list = []

    for (_, _, dir_filename_list) in walk(base_path_in):
        filename_list.extend(dir_filename_list)

    for filename in tqdm(filename_list):
        in_path = '{}/{}'.format(base_path_in, filename)
        out_path = '{}/w_{}'.format(base_path_out, filename)
        add_watermark(in_path, out_path)
