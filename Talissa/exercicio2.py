def solution(A, K):
    if A:
        A = []
        for i in range(0, K):
            A.insert(0, A[-1])
            del A[-1]
            return A


solution([2, 3, 4], 1)
