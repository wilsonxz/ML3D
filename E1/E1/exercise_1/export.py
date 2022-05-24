"""Export to disk"""


def export_mesh_to_obj(path, vertices, faces):
    """
    exports mesh as OBJ
    :param path: output path for the OBJ file
    :param vertices: Nx3 vertices
    :param faces: Mx3 faces
    :return: None
    """

    # write vertices starting with "v "
    # write faces starting with "f "

    # ###############
    # TODO: Implement
    with open(path, 'w') as f:
        for i in range(vertices.shape[0]):
            string_one = ''.join([format(vertices[i,j],".4f")+' ' for j in range(3)])
            string_one = 'v ' + string_one
            f.write(string_one+'\n')
        for k in range(faces.shape[0]):
            faces_p1 = faces[k,:]+1
            string_one = ''.join([str(faces_p1[j].astype(int))+' ' for j in range(3)])
            string_one = 'f ' + string_one
            f.write(string_one+'\n')
    return None
    # ###############


def export_pointcloud_to_obj(path, pointcloud):
    """
    export pointcloud as OBJ
    :param path: output path for the OBJ file
    :param pointcloud: Nx3 points
    :return: None
    """

    # ###############
    # TODO: Implement
    with open(path, 'w') as f:
        for i in range(pointcloud.shape[0]):
            string_one = ''.join([format(pointcloud[i,j],".4f")+' ' for j in range(3)])
            string_one = 'v ' + string_one
            f.write(string_one+'\n')
    return None
    # ###############
