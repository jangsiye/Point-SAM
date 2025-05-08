import numpy as np


# def load_ply(filename):
#     with open(filename, "r") as rf:
#         while True:
#             try:
#                 line = rf.readline()
#             except:
#                 raise NotImplementedError
#             if "end_header" in line:
#                 break
#             if "element vertex" in line:
#                 arr = line.split()
#                 num_of_points = int(arr[2])

#         # print("%d points in ply file" %num_of_points)
#         points = np.zeros([num_of_points, 6])
#         for i in range(points.shape[0]):
#             point = rf.readline().split()
#             assert len(point) == 6
#             points[i][0] = float(point[0])
#             points[i][1] = float(point[1])
#             points[i][2] = float(point[2])
#             points[i][3] = float(point[3])
#             points[i][4] = float(point[4])
#             points[i][5] = float(point[5])
#     rf.close()
#     del rf
#     return points

import open3d as o3d
import numpy as np

def load_ply(filename):
    pcd = o3d.io.read_point_cloud(filename)
    points = np.asarray(pcd.points)  # (N, 3) shape

    if pcd.has_colors():
        colors = np.asarray(pcd.colors)  # (N, 3) shape
        # 0~1 사이 값을 0~255 범위로 변환
        colors = (colors * 255).astype(np.float32)
        combined = np.concatenate([points, colors], axis=1)  # (N, 6)
    else:
        # 색깔 정보 없는 경우
        combined = np.concatenate([points, np.zeros_like(points)], axis=1)  # (N, 6)

    return combined

