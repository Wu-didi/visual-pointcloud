'''可视化截取的视锥体'''

import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'models'))
sys.path.append('D:\BaiduNetdiskWorkspace\python_file2\frustum_pointnets_pytorch-master\kitti')
import pickle
from kitti_object import *
pickle_data_path = r'D:\BaiduNetdiskWorkspace\python_file2\frustum_pointnets_pytorch-master\kitti\frustum_caronly_train.pickle'
f = open(pickle_data_path,'rb')   #pickle_data_path为.pickle文件的路径；
info = pickle.load(f)
box2d_list = pickle.load(f)
box3d_list = pickle.load(f)
input_list = pickle.load(f)
label_list = pickle.load(f)
type_list = pickle.load(f)
heading_list = pickle.load(f)
size_list = pickle.load(f)
frustum_angle_list = pickle.load(f)
print(len(input_list))
import mayavi.mlab as mlab
for i in range(10):
    p1 = input_list[i]
    seg = label_list[i]
    fig = mlab.figure(figure=None, bgcolor=(0.4,0.4,0.4),
        fgcolor=None, engine=None, size=(500, 500))
    mlab.points3d(p1[:,0], p1[:,1], p1[:,2], p1[:,1], mode='point',
        colormap='gnuplot', scale_factor=1, figure=fig)
    fig = mlab.figure(figure=None, bgcolor=(0.4,0.4,0.4),
        fgcolor=None, engine=None, size=(500, 500))
    mlab.points3d(p1[:,2], -p1[:,0], -p1[:,1], seg, mode='point',
        colormap='gnuplot', scale_factor=1, figure=fig)
    raw_input()
f.close()  #别忘记close pickle文件
