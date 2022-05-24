"""SDF to Occupancy Grid"""
import numpy as np
from exercise_1.sdf_grid import sdf_grid#import sdf_grid function



def occupancy_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An occupancy grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with value 0 outside the shape and 1 inside.
    """

    # ###############
    # TODO: Implement
    gridfloat=sdf_grid(sdf_function, resolution)
    grid_bool = np.zeros_like(gridfloat)#构造一个矩阵grid_bool，其维度与矩阵grid_float一致，为其初始化为全0；方便的构造了新矩阵，无需参数指定shape大小
    grid_bool[gridfloat<=0] = 1 #给距离为负-在内部的点 赋值为1
    return grid_bool
    # ###############
