import pydicom
from PIL import Image
import numpy as np
import io

def convert_dcm_to_jpg(file):
    ds = pydicom.dcmread(file)
    pixel_array = ds.pixel_array

    if len(pixel_array.shape) == 3:
        img = Image.fromarray(pixel_array[0])
    else:
        img = Image.fromarray(pixel_array)

    img = img.convert("L")
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    return buffer
