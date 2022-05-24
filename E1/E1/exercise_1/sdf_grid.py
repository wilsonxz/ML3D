"""Creating an SDF grid"""
import numpy as np


def sdf_grid(sdf_function, resolution):
    """
    Create an occupancy grid at the specified resolution given the implicit representation.
    :param sdf_function: A function that takes in a point (x, y, z) and returns the sdf at the given point.
    Points may be provides as vectors, i.e. x, y, z can be scalars or 1D numpy arrays, such that (x[0], y[0], z[0])
    is the first point, (x[1], y[1], z[1]) is the second point, and so on
    :param resolution: Resolution of the occupancy grid
    :return: An SDF grid of specified resolution (i.e. an array of dim (resolution, resolution, resolution) with positive values outside the shape and negative values inside.
    """

    # ###############
    # TODO: Implement
    pos_1dim = np.linspace(-0.5, 0.5, num = resolution)
    pos_cube = np.meshgrid(pos_1dim, pos_1dim, pos_1dim)
    pos_array=[]
    for i in range(3):
        pos_array.append(pos_cube[i].reshape(-1))  #[x,y,z] 3 columns reshape(-1)按照行排列为一维数组
    SDF_grid_array = sdf_function(pos_array[0], pos_array[1], pos_array[2])   
    SDF_grid = SDF_grid_array.reshape([resolution, resolution, resolution])

    return SDF_grid
    # ###############
