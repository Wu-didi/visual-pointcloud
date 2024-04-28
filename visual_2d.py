import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 读取 JSON 文件路径
json_file_path = r'E:\BaiduNetdiskDownload\mnt\data\GT_json\front\1707142486.529829000_0.json'

# 读取图片路径
image_path = r'E:\BaiduNetdiskDownload\mnt\data\image\front\1707142486.529829000_0.jpg'


# 读取 JSON 文件
with open(json_file_path, 'r') as f:
    data = json.load(f)

# 读取图片
image = cv2.imread(image_path)

# 绘制 2D 盒子和标签
for annotation in data['annotations']:
    bbox = annotation['2dbbox']
    category_id = int(annotation['category_id'])
    if bbox:
        x, y, w, h = map(int, bbox)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, str(category_id), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 显示绘制了 2D 盒子的图片
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# 绘制 3D 盒子
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for annotation in data['annotations']:
    bbox = annotation['3dbbox']
    if bbox:
        x, y, z, w, h, l, yaw = map(float, bbox)
        yaw_rad = np.deg2rad(yaw)
        # 计算3D盒子的8个顶点坐标
        corner_points = np.array([
            [x - l/2 * np.cos(yaw_rad) - w/2 * np.sin(yaw_rad), y - l/2 * np.sin(yaw_rad) + w/2 * np.cos(yaw_rad), z],
            [x + l/2 * np.cos(yaw_rad) - w/2 * np.sin(yaw_rad), y + l/2 * np.sin(yaw_rad) + w/2 * np.cos(yaw_rad), z],
            [x + l/2 * np.cos(yaw_rad) + w/2 * np.sin(yaw_rad), y + l/2 * np.sin(yaw_rad) - w/2 * np.cos(yaw_rad), z],
            [x - l/2 * np.cos(yaw_rad) + w/2 * np.sin(yaw_rad), y - l/2 * np.sin(yaw_rad) - w/2 * np.cos(yaw_rad), z],
            [x - l/2 * np.cos(yaw_rad) - w/2 * np.sin(yaw_rad), y - l/2 * np.sin(yaw_rad) + w/2 * np.cos(yaw_rad), z + h],
            [x + l/2 * np.cos(yaw_rad) - w/2 * np.sin(yaw_rad), y + l/2 * np.sin(yaw_rad) + w/2 * np.cos(yaw_rad), z + h],
            [x + l/2 * np.cos(yaw_rad) + w/2 * np.sin(yaw_rad), y + l/2 * np.sin(yaw_rad) - w/2 * np.cos(yaw_rad), z + h],
            [x - l/2 * np.cos(yaw_rad) + w/2 * np.sin(yaw_rad), y - l/2 * np.sin(yaw_rad) - w/2 * np.cos(yaw_rad), z + h]
        ])
        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], [2, 6], [3, 7]]
        for edge in edges:
            ax.plot3D(corner_points[edge, 0], corner_points[edge, 1], corner_points[edge, 2], 'b')

plt.show()
