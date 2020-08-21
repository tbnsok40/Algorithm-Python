# dfs
def solution(n, computers):
    answer =0
    visit = [0] * n
    def dfs_def(start):
        dfs = [start]
        while dfs:
            com_num = dfs.pop()
            # if visit[com_num] == 0:
            #     visit[com_num] = 1
            visit[com_num] = 1
            for i in range(n):
                if visit[i] == 0 and computers[com_num][i] == 1:
                    # 아직 방문은 안했는데, 현재 노드와 연결된 노드를 찾는다.
                    dfs.append(i)
            # 그럼 현재 while 문이 계속 돌면서, 이어진 노드들에 대한 연쇄적으로 탐색이 이루어진다.
            # 깊이 우선 탐색이 된다.
        return
    i = 0
    while 0 in visit:
        if visit[i] == 0:
            dfs_def(i)
            answer += 1
        i += 1
    return answer
computers= [[1,0,0],[0,1,0],[0,0,1]]
print(solution(3,computers))


# bfs
def solution2(n, computers):
    # 1
    answer = 0 # 네트워크의 개수를 저장할 변수
    bfs = [] # 탐색을 위한 큐
    visited = [0]*n # 방문한 노드를 체크해 둘 리스트

    # 2
    while 0 in visited:
        bfs.append(visited.index(0))

        while bfs: # 큐 값이 존재하면 반복문 수행
            node = bfs.pop(0) # 큐 첫번째 값 pop하여 node로 지정
            visited[node] = 1 # 방문한 인덱스(노드)는 1로 치환 (기존엔 0이었다)

            for i in range(n): # 꺼낸 노드의 인접 노드 방문하기 위해 반복문 수행

                # 아직 미방문된 and 인접노드인(1이라는 것은 연결됐다는 것이니까)
                if visited[i] == 0 and computers[node][i] == 1:

                    bfs.append(i) # 인덱스를 append
        answer += 1
    return answer

print(solution2(3, computers))
