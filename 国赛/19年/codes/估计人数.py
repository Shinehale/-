# 弗洛伊德
def floyd(n):
    for k in range(1, n + 1):  # 当前考虑的中间节点
        for i in range(1, n + 1):  # 遍历图中的每一个节点
            for j in range(1, n + 1):  # 考虑该节点的所有可能的邻接节点
                if new_graph[i][k] * new_graph[k][j] == 1:
                    new_graph[i][j] = 1


# 匈牙利
def dfs(node, node_cot):
    for k in range(1, node_cot + 1):
        if new_graph[node][k] == 1:
            if visited[k] == 0:
                visited[k] = 1
                if connected[k] == -1 or dfs(connected[k], node_cot):
                    connected[k] = node
                    return True
    return False


dx = [0, 1]
dy = [1, 0]
N, M = list(map(int, input().split()))
graph = [[0 for i in range(M)] for j in range(N)]

node_cot = 0
for i in range(N):
    strr = input()
    for j in range(M):
        e = int(strr[j])
        if e == 1:
            node_cot += 1
            graph[i][j] = [e, node_cot]
        else:
            graph[i][j] = [e, -1]

new_graph = [[0 for i in range(node_cot + 1)] for j in range(node_cot + 1)]
for i in range(N):
    for j in range(M):
        if graph[i][j][0] == 1:
            node_idx = graph[i][j][1]
            for x in range(2):
                new_i = i + dx[x]
                new_j = j + dy[x]
                if 0 <= new_i < N and 0 <= new_j < M and graph[new_i][new_j][0] == 1:
                    new_graph[node_idx][graph[new_i][new_j][1]] = 1

floyd(node_cot)

cot = 0

visited = [0 for i in range(node_cot + 1)]
connected = [-1 for i in range(node_cot + 1)]
for i in range(1, node_cot + 1):
    visited = [0 for i in range(node_cot + 1)]
    if dfs(i, node_cot):
        cot += 1
print(node_cot - cot)
