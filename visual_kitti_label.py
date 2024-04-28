import open3d as o3d
import numpy as np

# 读取点云数据
point_cloud = o3d.io.read_point_cloud(r"E:\python_file\visual-pointcloud\kitti\velodyne\000000.bin")

# 从文本文件中读取标签行
label_file = r"E:\python_file\visual-pointcloud\kitti\label_2\000000.txt"
with open(label_file, "r") as f:
    label_line = f.readline().strip()  # 读取一行并去除首尾空白字符

# 按空格分割标签信息
label_info = label_line.split(" ")

# 获取标签名称
label_name = label_info[0]

# 获取边界框的坐标信息
bbox = [float(x) for x in label_info[11:15]]  # 边界框信息的索引位置根据具体情况调整

# 边界框的8个顶点坐标
bbox_points = np.array([
    [bbox[0], bbox[1], bbox[2]],
    [bbox[3], bbox[1], bbox[2]],
    [bbox[3], bbox[4], bbox[2]],
    [bbox[0], bbox[4], bbox[2]],
    [bbox[0], bbox[1], bbox[5]],
    [bbox[3], bbox[1], bbox[5]],
    [bbox[3], bbox[4], bbox[5]],
    [bbox[0], bbox[4], bbox[5]]
])

# 边界框的边
lines = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

# 创建边界框线段集合
lineset = o3d.geometry.LineSet()
lineset.points = o3d.utility.Vector3dVector(bbox_points)
lineset.lines = o3d.utility.Vector2iVector(lines)
lineset.colors = [[1, 0, 0] for _ in range(len(lines))]  # 边界框线段的颜色为红色

# 将边界框添加到点云中
point_cloud += lineset

# 创建窗口并显示点云和边界框
o3d.visualization.draw_geometries([point_cloud])
