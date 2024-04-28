# 参加的国汽智联的比赛，给的数据是点云数据，需要将点云数据可视化

import open3d as o3d
import json
import numpy as np

# 读取 JSON 文件路径
json_file_path = r'E:\BaiduNetdiskDownload\mnt\data\GT_json\pcd\1707142519.052345000.json'

# 读取点云文件路径
pcd_file_path = r'E:\BaiduNetdiskDownload\mnt\data\pcd\1707142519.052345000.pcd'


# 读取 JSON 文件
with open(json_file_path, 'r') as f:
    data = json.load(f)

# 读取点云数据
pcd_data = o3d.io.read_point_cloud(pcd_file_path)

# 创建 Open3D 可视化窗口
vis = o3d.visualization.Visualizer()
vis.create_window()

# 将点云对象添加到可视化窗口中
vis.add_geometry(pcd_data)

# 绘制 3D 盒子
for annotation in data['annotations']:
    bbox = annotation['3dbbox']
    if bbox:
        # 解析数据
        x, y, z, length, width, height, yaw = bbox
        
        # 计算旋转矩阵
        R = np.array([[np.cos(yaw), -np.sin(yaw), 0],
                      [np.sin(yaw), np.cos(yaw), 0],
                      [0, 0, 1]])

        # 计算顶点坐标
        points = np.array([[-length / 2, -width / 2, 0],
                           [length / 2, -width / 2, 0],
                           [length / 2, width / 2, 0],
                           [-length / 2, width / 2, 0],
                           [-length / 2, -width / 2, height],
                           [length / 2, -width / 2, height],
                           [length / 2, width / 2, height],
                           [-length / 2, width / 2, height]])

        # 进行旋转并平移
        points = np.dot(R, points.T).T
        points += [x, y, z]

        # 绘制3D盒子
        lines = [[0, 1], [1, 2], [2, 3], [3, 0],
                 [4, 5], [5, 6], [6, 7], [7, 4],
                 [0, 4], [1, 5], [2, 6], [3, 7]]
        colors = [[1, 0, 0] for i in range(len(lines))]
        line_set = o3d.geometry.LineSet()
        line_set.points = o3d.utility.Vector3dVector(points)
        line_set.lines = o3d.utility.Vector2iVector(lines)
        line_set.colors = o3d.utility.Vector3dVector(colors)
        vis.add_geometry(line_set)

# 设置相机参数
view_control = vis.get_view_control()
view_control.set_lookat([0, 0, 0])  # 设置相机看向的点
view_control.set_up([0, -1, 0])  # 设置相机的朝向
view_control.set_zoom(0.5)  # 设置缩放

# 运行可视化窗口
vis.run()
vis.destroy_window()
