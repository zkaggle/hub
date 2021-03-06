# coding:utf-8
# ocr识别

import os
from paddleocr import PaddleOCR, draw_ocr
import paddlenlp
from paddlenlp.taskflow import Taskflow
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib

from paddlenlp import Taskflow

seg = Taskflow("word_segmentation")
seg.help()
from paddlenlp import Taskflow

seg = Taskflow("word_segmentation")
seg("第十四届全运会在西安举办")
'''
['第十四届', '全运会', '在', '西安', '举办']
'''

seg(["第十四届全运会在西安举办", "三亚是一个美丽的城市"])
'''
[['第十四届', '全运会', '在', '西安', '举办'], ['三亚', '是', '一个', '美丽', '的', '城市']]
'''

# # 命名实体识别与词频统计
#
# def deletaNum(doc):
#     return [i for i in doc if len(i) > 1]
#
#
# def LAC(lac, res_list):  # 根据结果筛选
#     doc = [text[1][0] for res in res_list for text in res]
#
#     doc = deletaNum(doc)
#     # print('\n\ndoc is ',doc)
#     lac_dic = lac(doc)
#     enti = []
#     for la in lac_dic:
#         ent = []
#         for l in la:
#             if l[1] in ['nt', 'ORG']:
#                 ent.append(l[0])
#         enti += ent
#
#     return enti
#
#
# def PlotHist(counter):
#     matplotlib.rc("font", family='FZHuaLi-M14S')
#
#     cnt = {}
#     for key in counter.keys():
#         if counter[key] >= 10:  # 此处只绘制出现频率大于10的机构
#             cnt[key] = counter[key]
#     print(cnt)
#     plt.figure(figsize=(10, 5))
#     plt.bar(range(len(cnt)), cnt.values(), tick_label=list(cnt.keys()))
#     plt.xticks(rotation=45)
#     plt.savefig('./img.png')
#     plt.show()
#
#
# if __name__ == '__main__':
#     # 模型路径下必须含有model和params文件
#     ocr = PaddleOCR(det_model_dir='./PaddleOCR/output/ch_db_mv3_inference/inference',
#                     use_angle_cls=True)
#     lac = Taskflow("pos_tagging")
#
#     enti_list = []
#     pdfFolder = './ResearchReport'
#     for p in os.listdir(pdfFolder):
#         if os.path.isdir(os.path.join(pdfFolder, p)):
#             print('Processing folder:', p)
#             imgPath = pdfFolder + '/' + p
#             res_list = []
#             for i in os.listdir(imgPath):
#                 img_path = os.path.join(imgPath, i)
#                 result = ocr.ocr(img_path, cls=True)
#                 res_list.append(result)
#
#             enti = LAC(lac, res_list)
#             enti_list += enti
#
#     counter = Counter(enti_list)
#     print('Entity results:', counter)
#
#     PlotHist(counter)
