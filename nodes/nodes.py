import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
from dithering import ordered_dither

def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0) 
 
class DitherImage:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                    "image": ("IMAGE",),
                    }
                }

    RETURN_TYPES = ("IMAGE",)
    #RETURN_NAMES = ("Dithered",)
    FUNCTION = "draw_overlay_text"
    CATEGORY = "Axel"

    def draw_overlay_text(self, image):
        def normalize8(I):
            mn = I.min()
            mx = I.max()
            mx -= mn
            I = ((I - mn)/mx) * 255
            return I.astype(np.uint8)
        #image = Image.fromarray(np.array(image), "RGB")
        print(image.shape)
        array = np.array(image)
        array = normalize8(array)
        array = np.squeeze(array)
        dithered = ordered_dither(array, "Bayer4x4")
        print(dithered.shape)
        dithered = Image.fromarray(dithered)
        return image