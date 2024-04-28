import open3d as o3d
import numpy as np

# 使用open3d显示点云

def show_small_point_v2(path,size=2):
    # name = '000001'
    # # -------------------------加载点云-----------------------------
    # binary = f'D:/python_files4/frustum-convnet-master/frustum-convnet-master\data\kitti/training/velodyne/{name}.bin'

    # read raw data from binary
    # scan = np.fromfile(path, dtype=np.float32).reshape((-1,4))
    # points = scan[:, 0:3] # lidar xyz (front, left, up)
    points = path

    pcd = o3d.geometry.PointCloud()#传入3d点云
    pcd.points = o3d.utility.Vector3dVector(points)	#point3D二维numpy矩阵,将其转换为open3d点云格式

    vis = o3d.visualization.Visualizer()
    vis.create_window()	#创建窗口
    render_option: o3d.visualization.RenderOption = vis.get_render_option()	#设置点云渲染参数
    render_option.background_color = np.array([0, 0, 0])	#设置背景色（这里为黑色）
    render_option.point_size = size	#设置渲染点的大小
    vis.add_geometry(pcd)	#添加点云
    vis.run()


def show_small_point(path,size=2):
    # -------------------------加载点云-----------------------------
    points = path

    pcd = o3d.geometry.PointCloud()#传入3d点云
    pcd.points = o3d.utility.Vector3dVector(pcd)	#point3D二维numpy矩阵,将其转换为open3d点云格式

    # -----------------------初始化显示窗口--------------------------
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name='可视化', width=800, height=600)
    # -----------------------可视化参数设置--------------------------
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0])  # 设置背景色*****
    opt.point_size = size                  # 设置点的大小*************
    opt.show_coordinate_frame = True    # 设置是否添加坐标系
    pcd.paint_uniform_color([1, 0, 0])  # 自定义点云显示颜色
    vis.add_geometry(pcd)               # 加载点云到可视化窗口
    vis.run()                           # 激活显示窗口，这个函数将阻塞当前线程，直到窗口关闭。
    vis.destroy_window()                # 销毁窗口，这个函数必须从主线程调用。



if __name__ == "__main__":
    name = '000000'
    # -------------------------加载点云-----------------------------
    binary = f'E:\python_file\visual-pointcloud\000000.bin'

    show_small_point(binary,12)

