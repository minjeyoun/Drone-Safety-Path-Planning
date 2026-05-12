import random
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

# 격자의 크기 설정
n = 101  # 0부터 100까지

# 격자 초기화, 0은 이동 가능한 칸을 의미
grid = [[0 for _ in range(n)] for _ in range(n)]

# 장애물(1)을 랜덤하게 배치, 시작점(0,0)과 끝점(100,100)은 제외
obstacles = 2000
while obstacles:
    x, y = random.randint(0, n - 1), random.randint(0, n - 1)
    if (x, y) != (0, 0) and (x, y) != (n - 1, n - 1) and grid[x][y] == 0:
        grid[x][y] = 1
        obstacles -= 1


def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    prev = {start: None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                prev[(nx, ny)] = (x, y)

    # 경로 복원
    path = []
    at = goal
    while at != None:
        path.append(at)
        at = prev[at]
    path.reverse()
    return path


start = (0, 0)
goal = (n - 1, n - 1)
path = bfs(start, goal)

# 경로 출력 (있을 경우)
if path:
    for x, y in path:
        grid[x][y] = 2  # 경로를 2로 표시

# 격자 상태 출력
for row in grid:
    print(' '.join(str(cell) for cell in row))

# 격자 상태 numpy 배열로 변환
grid_array = np.array(grid)

# 격자와 경로 시각화
plt.figure(figsize=(10, 10))
plt.imshow(grid_array, cmap='hot', interpolation='nearest')

# 격자의 각 셀에 좌표 라벨링
for y in range(n):
    for x in range(n):
        if grid_array[y, x] == 0:  # 이동 가능
            plt.text(x, y, '·', ha='center', va='center', color='white')
        elif grid_array[y, x] == 1:  # 장애물
            plt.text(x, y, 'X', ha='center', va='center', color='black')
        elif grid_array[y, x] == 2:  # 경로
            plt.text(x, y, 'O', ha='center', va='center', color='cyan')

# 시작점과 끝점 표시
plt.text(0, 0, 'S', ha='center', va='center', color='green')
plt.text(n - 1, n - 1, 'G', ha='center', va='center', color='red')

plt.xticks(range(0, n, 10))
plt.yticks(range(0, n, 10))
plt.grid(which='both')
plt.show()
