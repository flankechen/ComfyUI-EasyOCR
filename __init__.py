from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    "Apply EasyOCR": ApplyEasyOCR,
    "EasyOCR text": EasyOCRforText,
    "EasyOCR draw rectangle": EasyOCRdrawRectangle,
    "EasyOCR Image Resize to toal pixels keep ratio": EasyOCRImageResizeToTotalAndKeepRatio,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Apply EasyOCR": "Apply EasyOCR",
    "EasyOCR text":"EasyOCR text",
    "EasyOCR draw rectangle":"EasyOCR draw rectangle",
    "EasyOCR Image Resize to toal pixels keep ratio":"EasyOCR Image Resize to toal pixels keep ratio",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
