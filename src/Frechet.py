import numpy as np
import math

def euc_dist(pt1, pt2):
    '''
    calculate the euclidean distance between pt1 to pt2
    '''
    return math.sqrt((pt2[0]-pt1[0])*(pt2[0]-pt1[0])+(pt2[1]-pt1[1])*(pt2[1]-pt1[1]))


def cal_frechet(cal_result,i,j,P,Q):
    '''
    the process of calculating Fréchet Distance

    Args:
    cal_result: the calculating result matrix
    i: index of curve P
    j: index of curve Q
    P: curve, stored by point sequence, e.g: curve P: [(x1,y1),(x2,y2)]
    Q: curve, stored by point sequence, e.g: curve Q: [(x1,y1),(x2,y2),(x3,y3)]

    '''
    if cal_result[i][j] > -1:
        return cal_result[i][j]
    elif i == 0 and j == 0:
        cal_result[i][j] = euc_dist(P[0],Q[0])
    elif i > 0 and j == 0:
        cal_result[i][j] = max(cal_frechet(cal_result,i-1,0,P,Q),euc_dist(P[i],Q[0]))
    elif i == 0 and j > 0:
        cal_result[i][j] = max(cal_frechet(cal_result,0,j-1,P,Q),euc_dist(P[0],Q[j]))
    elif i > 0 and j > 0:
        cal_result[i][j] = max(min(cal_frechet(cal_result,i-1,j,P,Q),cal_frechet(cal_result,i-1,j-1,P,Q),cal_frechet(cal_result,i,j-1,P,Q)),euc_dist(P[i],Q[j]))
    else:
        cal_result[i][j] = float("inf")
    return cal_result[i][j]


def frechet_distance(P,Q):
    '''
    calculate the Fréchet Distance
    '''
    cal_result = np.ones((len(P),len(Q))) # cal_result: len(P)*len(Q) matrix, default value: 1
    cal_result = np.multiply(cal_result,-1)
    return cal_frechet(cal_result, len(P)-1, len(Q)-1, P, Q)


if __name__ == "__main__":
    P = [(1,1),(2,2)]
    Q = [(1,1),(2,2),(3,3)]
    print(frechet_distance(P,Q)) # 1.414