from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    "Apply EasyOCR": ApplyEasyOCR,
    "EasyOCR text": EasyOCRforText,
    "EasyOCR draw rectangle": EasyOCRdrawRectangle,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Apply EasyOCR": "Apply EasyOCR",
    "EasyOCR text":"EasyOCR text",
    "EasyOCR draw rectangle":"EasyOCR draw rectangle",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
