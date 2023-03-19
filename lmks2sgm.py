import argphase

def closed_regions(points, canvas_size): 
    """_summary_

    Args:
        points (list[np.ndarray]): a set of points
        canvas_size (tuple(height, width)): the attributes of canvas
    """    
    H, W = canvas_size
    points.append(points[0])
    N = len(points)
    vec_lines = [ points[i+1] - points[i] for i in range(N-1) ]
    # vec_lines.append( points[0] - points[-1] )

    # agl_lines = [ np.arccos( vec_lines[i][0]/np.sqrt(vec_lines[i][0]**2 + vec_lines[i][1]**2) ) for i in range(N+1)]

    # find inner vector
    inner_vec = np.array(vec_lines[0])
    for i in range(1, N): 
        inner_vec = inner_vec + vec_lines[i]
        # Not co-line
        if inner_vec.dot(vec_lines[0]) < np.sqrt((inner_vec.dot(inner_vec))*(vec_lines[0].dot(vec_lines[0]))): 
            break

    # find normal vector of line 0
    norm_vec_line_0_0 = np.array([-vec_lines[0][1], vec_lines[0][0]])/np.sqrt(vec_lines[0][0]**2 + vec_lines[0][1]**2)
    norm_vec_line_0_1 = np.array([vec_lines[0][1], -vec_lines[0][0]])/np.sqrt(vec_lines[0][0]**2 + vec_lines[0][1]**2)

    # find normal vector for each line
    if norm_vec_line_0_0.dot(inner_vec) > 0: 
        norm_vec = np.array([ np.array([-vec_lines[i][1], vec_lines[i][0]])/np.sqrt(vec_lines[i][0]**2 + vec_lines[i][1]**2) for i in range(N)])
    else if: norm_vec_line_0_1.dot(inner_vec) > 0: 
        norm_vec = np.array([ np.array([vec_lines[i][1], -vec_lines[i][0]])/np.sqrt(vec_lines[i][0]**2 + vec_lines[i][1]**2) for i in range(N)])
    else: raise Exception
    points = np.array(points)

    coord = np.meshgrid(np.arrange(height), np.arrange(width))
    dist = coord[None, :, :, :] - points[:, None, None, :]
    prod = np.einsum('nhwp,np->nhw', dist, points)




if __name__ == '__main__': 
    pass
