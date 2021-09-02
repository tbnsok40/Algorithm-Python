def solution(triangle):
    R = len(triangle)
    C = len(triangle[-1])
    result = []

    # 재귀 ( r, c, triangle, sum)
    def recursive(row, column, triangle, total):
        for r in range(row, R):
            C_ = len(triangle[r])
            for c in range(column, column + 2):
                if r == R:
                    result.append(total)
                    return
                if (r + 1) < R or (c + 1) < C_:
                    total += triangle[r][c]
                    recursive(r + 1, c, triangle, total)
                    recursive(r + 1, c + 1, triangle, total)

    recursive(0, 0, triangle, triangle[0][0])

    return result


print(solution(triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
