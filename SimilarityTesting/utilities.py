import numpy as np

def longest_common_subarray(arr1, arr2):
    matrix = [[0 for _ in range(len(arr1)+1)] for _ in range(len(arr2)+1)]
    max_length = 0
    ret = []

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if arr1[j-1] == arr2[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    ret = arr1[j-max_length:j]

    return ret


def union(arr1, arr2):
    return list(set(arr1) | set(arr2))

def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

def jaccard(a, b):
    return len(intersection(a, b)) / len(union(a, b))

def FI(a, b, lcs, alpha, beta):
    return alpha*(jaccard(a, b)) + beta*(jaccard(a, lcs))