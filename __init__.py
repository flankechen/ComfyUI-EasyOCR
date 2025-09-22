from .node import *
from .install import *

NODE_CLASS_MAPPINGS = {
    "Apply EasyOCR": ApplyEasyOCR,
    "EasyOCR text": EasyOCRforText,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Apply EasyOCR": "Apply EasyOCR",
    "EasyOCR text":"EasyOCR text",
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
