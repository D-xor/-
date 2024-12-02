#%%
import numpy as np
import matplotlib.pyplot as plt
from random import randint, choice

class BezierCurve:
    def __init__(self) -> None:
        pass

    # 贝塞尔曲线生成函数
    def bezier_curve(self, P0, P1, P2, P3, n_points=100):
        t = np.linspace(0, 1, n_points).reshape(-1, 1)  # t 转为列向量 (n_points, 1)
        curve = (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3
        return curve

    def generate_curve_point(self, x):
        P0 = np.array([0, 0])                       # 起点
        # P1 = np.array([0, randint(200, 400)])       # 第一个控制点
        P1 = np.array([0, 400])       # 第一个控制点
        P2 = np.array([x/2, 0])                       # 第二个控制点
        P3 = np.array([x, randint(800, 1000)+x*randint(1, 3)])         # 终点

        # plt.scatter([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], color="red", label="控制点")
        # plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], '--', color="gray", label="控制点连线")
        # curve = self.bezier_curve(P0, P1, P2, P3, n_points=200)
        
        n_points = int(10 + (x / 100) * 100)
        curve_points = self.bezier_curve(P0, P1, P2, P3, n_points)
        return curve_points
    
    def format_track(self, points):
        # 转为int
        curve_points_int = np.round(points).astype(int)
        # 末尾添加断崖坐标
        last_point = curve_points_int[-1]
        curve_points_int = np.append(curve_points_int, [[last_point[0], last_point[1]+randint(200, 500)]], axis=0)
        # x坐标添加随机偏移
        curve_points_int[:, 0] += randint(10, 40)
        # 添加z坐标
        init_z = randint(15, 25)
        z_array = [init_z + choice([0, 0, 0, 1, -1]) for _ in range(curve_points_int.shape[0])]
        combined_points = np.column_stack((curve_points_int[:, 0], z_array, curve_points_int[:, 1]))
        
        return combined_points
    
    def generate_track_str(self, points_array):
        track_point_list = []
        for point in points_array:
            item = ','.join(map(str, point))
            track_point_list.append(item)
        return "|".join(track_point_list) + "|"

    def curve_show(self, curve):
        # 可视化
        plt.figure(figsize=(8, 6))
        plt.plot(curve[:, 0], curve[:, 1], color="black", linewidth=3)
        plt.legend()
        plt.grid(True)
        plt.show()

def get_track(x):
    bc = BezierCurve()
    c = bc.generate_curve_point(x)
    z = bc.format_track(c)
    ts = bc.generate_track_str(z)
    return ts

if __name__ == '__main__':
    import os
    os.chdir("..")
    bc = BezierCurve()
    c = bc.generate_curve_point(x=200)
    z = bc.format_track(c)
    ts = bc.generate_track_str(z)
    print(ts)