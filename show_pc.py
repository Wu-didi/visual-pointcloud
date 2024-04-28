import open3d as o3d

# 加载点云文件
point_cloud = o3d.io.read_point_cloud(r"E:\python_file\visual-pointcloud\kitti\training\velodyne\000000.bin")

# 创建窗口并显示点云
o3d.visualization.draw_geometries([point_cloud])