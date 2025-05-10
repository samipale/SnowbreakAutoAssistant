# 读取 OCR 替换配置
import os
import json

from app.common.logger import logger
from app.modules.ocr.ocr import OCR

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../AppData/ocr_replacements.json"), 'r', encoding='utf-8') as file:
    replacements = json.load(file)

# 初始化 OCR 对象
ocr = OCR(logger, replacements)
