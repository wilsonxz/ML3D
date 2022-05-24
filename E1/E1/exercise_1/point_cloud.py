"""Triangle Meshes to Point Clouds"""
import numpy as np


def sample_point_cloud(vertices, faces, n_points):
    """
    Sample n_points uniformly from the mesh represented by vertices and faces
    :param vertices: Nx3 numpy array of mesh vertices
    :param faces: Mx3 numpy array of mesh faces
    :param n_points: number of points to be sampled
    :return: sampled points, a numpy array of shape (n_points, 3)
    """

    # ###############
    # TODO: Implement
    def area_of_one_triangle(one_triangle):
        #* one_triangle: 3*3 -> area: float
        ab=one_triangle[:,1]-one_triangle[:,0]
        ac=one_triangle[:,2]-one_triangle[:,0]
        area=1/2*np.sqrt(np.sum(np.cross(ab, ac)**2))
        return area
    p = np.zeros([n_points, 3])
    area = np.zeros(faces.shape[0])
    for i in range(faces.shape[0]):
        area[i] = area_of_one_triangle(vertices[faces[i,:], :])
    sum_area=sum(area)
    fraction_each=area/sum_area
    sample=np.random.choice(np.arange(faces.shape[0]), n_points, replace=True, p=fraction_each)
    for i in range(n_points):
        face_rand = faces[sample[i],:] # 3*1
        p_triangle=vertices[face_rand,:] # 3*3
        A=p_triangle[0,:]
        B=p_triangle[1,:]
        C=p_triangle[2,:]
        r1=np.random.rand()
        r2=np.random.rand()
        u=1-np.sqrt(r1)
        v=np.sqrt(r1)*(1-r2)
        w=np.sqrt(r1)*r2
        p[i]=u*A+v*B+w*C
    return p
    # ###############
