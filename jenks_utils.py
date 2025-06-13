
import numpy as np
import pandas as pd

def jenks_breaks(data, k=5):
    """Calculate Jenks Natural Breaks classification"""
    data = sorted(data)
    n = len(data)
    mat1, mat2 = np.zeros((n+1, k+1)), np.zeros((n+1, k+1))
    
    for i in range(1, k+1):
        mat1[1][i] = 1
        for j in range(2, n+1):
            mat2[j][i] = float('inf')
    
    for i in range(2, n+1):
        s1 = s2 = w = 0
        for j in range(1, i+1):
            val = data[i-j]
            s1 += val
            s2 += val * val
            w += 1
            variance = s2 - (s1 * s1) / w
            if i-j > 0:
                for m in range(2, k+1):
                    if mat2[i][m] >= variance + mat2[i-j][m-1]:
                        mat1[i][m] = i-j+1
                        mat2[i][m] = variance + mat2[i-j][m-1]
        mat1[i][1] = 1
        mat2[i][1] = s2 - (s1 * s1) / w
    
    breaks = []
    k_idx = n
    for i in range(k, 0, -1):
        breaks.append(data[int(mat1[k_idx][i])-1])
        k_idx = int(mat1[k_idx][i]-1)
    
    return sorted(set(breaks))
