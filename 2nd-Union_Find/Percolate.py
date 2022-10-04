import statistics
import math
import random

ids = []  # ids[i] <= 자신의 parent 값을 저장
size = []  # size[i] : size of tree rooted at i

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
results = []


# root를 찾는 과정
def root(i):
    while i != ids[i]: i = ids[i]
    return i


def connected(p, q):
    return root(p) == root(q)


def union(p, q):
    id1, id2 = root(p), root(q)
    if id1 == id2: return
    if size[id1] <= size[id2]:
        ids[id1] = id2
        size[id2] += size[id1]
    else:
        ids[id2] = id1
        size[id1] += size[id2]


def simulate(n, t):
    for _ in range(t):
        opencount = 0
        # 사이즈와 루트를 초기화
        ids.clear()
        size.clear()

        for idx in range((n * n) + 2):
            ids.append(idx)
            size.append(1)

        # 2차원 배열 선언 및 모두 닫힌 상태로 초기화
        check = [[0 for j in range(n)] for i in range(n)]

        arr = [[0 for j in range(n)] for i in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                arr[i][j] = cnt
                cnt += 1

        # tuplearr 선언 및 초기화
        tuplearr = [[0 for j in range(n)] for i in range(n)]
        cnt1 = 0
        cnt2 = 0
        for i in range(n):
            for j in range(n):
                tuplearr[i][j] = (cnt1, cnt2)
                cnt2 += 1
            cnt1 += 1
            cnt2 = 0

        random.shuffle(tuplearr)

        # 가장 위, 가장 아래 배열값을 가상객체에 연결해준다.

        for k in range(n):
            union(arr[0][k], n)  # 가장 위의 가상 객체 연결

        for k in range(n):
            union(arr[n - 1][k], n + 1)  # 가장 밑의 가상 객체 연결

        # random 한 값을 열어준다.: (0, 0) ... (n-1, n-1) 까지 구성된 튜플 배열을 random.shuffle로 해서 앞에부터 열어준다.

        for val in tuplearr:
            for x, y in val:
                check[x][y] = 1
                opencount += 1
                # 인접한 4곳을 검사해본다
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 범위 밖이라면 넘긴다.
                    if nx < 0 or nx > (n - 1) or ny < 0 or ny > (n - 1):
                        continue
                    elif check[nx][ny] == 0:  # 닫혀있는 경우
                        continue
                    else:
                        union(arr[x][y], arr[nx][ny])

            if connected(n, n + 1):
                results.append((opencount / (n * n)))
                break

    meanval = statistics.mean(results)
    stdevval = statistics.stdev(results)
    intervalval = []
    intervalval.append(meanval - 1.96 * stdevval / math.sqrt(t))
    intervalval.append(meanval + 1.96 * stdevval / math.sqrt(t))

    print('mean = %.10f' % meanval)
    print('stdev = %.10f' % stdevval)
    print('95 confidence interval = [%.10f'% intervalval[0], end='')
    print(', %.10f] ' % intervalval[1])

    return meanval, stdevval
