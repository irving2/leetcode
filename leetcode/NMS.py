#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/5/13

# 从boundingboxes和score_list中进行非极大值抑制

import numpy as np
bounding_boxes = [(187, 82, 337, 317), (150, 67, 305, 282), (246, 121, 368, 304)]   # (x_start,y_start,x_end,y_end)
confidence_score = [0.9, 0.75, 0.8]

def Nms(bounding_boxes,confidence_score,threshhold):
    # 如果boundingbox 为空，返回空列表
    if len(bounding_boxes)==0:
        return [],[]

    # 计算每个boundingbox的面积
    bounding_boxes = np.array(bounding_boxes)
    confidence_score = np.array(confidence_score)
    start_x = bounding_boxes[:,0]
    start_y = bounding_boxes[:,1]
    end_x = bounding_boxes[:,2]
    end_y = bounding_boxes[:,3]
    area = (end_x-start_x+1)*(end_y-start_y)
    # 计算安照置信度排序的index参数列表
    order = np.argsort(confidence_score)     # 从小到大，排列索引值

    pick_boundingbox=[]
    pick_score = []
    # 遍历候选框列表
    while order.size:
        # pick置信度最大的框和置信度
        index = order[-1]
        pick_boundingbox.append(bounding_boxes[index])
        pick_score.append(confidence_score[index])
        # 计算其他候选框与目标框的insection area
        x1 = np.maximum(start_x[index],start_x[order[:-1]])
        x2 = np.minimum(end_x[index],end_x[order[:-1]])
        y1 = np.maximum(start_y[index],start_y[order[:-1]])
        y2 = np.minimum(end_y[index],end_y[order[:-1]])
        #  计算iou
        insection_area = np.maximum(0,x2-x1+1)*np.maximum(0,y2-y1+1)
        iou = insection_area/(area[index]+area[order[:-1]]-insection_area)
        # 根据阈值筛选
        left = order[np.where(iou<threshhold)]
        order = left
        # 更新候选框的index参数列表
    return pick_boundingbox,pick_score

print(Nms(bounding_boxes,confidence_score,0.4))