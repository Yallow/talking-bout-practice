""" Not the most elegant way of doing things Uses two lists as holders 
Assigned to matrix at the end """ 
def flip_vertical_axis(matrix):
    p_h = []
    op_h = []
    for x in matrix:
        for y in x:
            op_h.insert(0,y)
        p_h.append(op_h)
        op_h = []
    matrix[:] = p_h[:]
