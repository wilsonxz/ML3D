""" Procrustes Aligment for point clouds """
import numpy as np
from pathlib import Path


def procrustes_align(pc_x, pc_y):
    """
    calculate the rigid transform to go from point cloud pc_x to point cloud pc_y, assuming points are corresponding
    :param pc_x: Nx3 input point cloud
    :param pc_y: Nx3 target point cloud, corresponding to pc_x locations
    :return: rotation (3, 3) and translation (3,) needed to go from pc_x to pc_y
    """
    R = np.zeros((3, 3), dtype=np.float32)
    t = np.zeros((3,), dtype=np.float32)

    # TODO: Your implementation starts here ###############
    # 1. get centered pc_x and centered pc_y
    # 2. create X and Y both of shape 3XN by reshaping centered pc_x, centered pc_y
    # 3. estimate rotation
    # 4. estimate translation
    # R and t should now contain the rotation (shape 3x3) and translation (shape 3,)
    center_x = np.mean(pc_x,axis=0)
    center_y = np.mean(pc_y,axis=0)
    X = (pc_x-center_x).T # 3*N
    Y = (pc_y-center_y).T
    U, _, V = np.linalg.svd(Y@X.T)
    if np.isclose(np.linalg.det(U)*np.linalg.det(V.T), 1):
        S=np.eye(U.shape[0], U.shape[1])
    else:
        diag = np.ones(U.shape[0])
        diag[-1] = -1
        S=np.diag(diag)
    R = U @ S @ V
    t = - R @ center_x + center_y
    # TODO: Your implementation ends here ###############

    t_broadcast = np.broadcast_to(t[:, np.newaxis], (3, pc_x.shape[0]))
    print('Procrustes Aligment Loss: ', np.abs((np.matmul(R, pc_x.T) + t_broadcast) - pc_y.T).mean())

    return R, t


def load_correspondences():
    """
    loads correspondences between meshes from disk
    """

    load_obj_as_np = lambda path: np.array(list(map(lambda x: list(map(float, x.split(' ')[1:4])), path.read_text().splitlines())))
    path_x = (Path(__file__).parent / "resources" / "points_input.obj").absolute()
    path_y = (Path(__file__).parent / "resources" / "points_target.obj").absolute()
    return load_obj_as_np(path_x), load_obj_as_np(path_y)
