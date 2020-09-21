"""
------------------------------------------------------------------------------------------------------------------------
문제
서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction Manager Craft)가 발매되었다.

이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과
두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는 순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될
때까지 Delay가 존재한다.
----------------------------------------------------------------------------------------

위의 예시를 보자.

이번 게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이 가능하다)
 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.

따라서 4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다. 그리고 2번 건물과 3번 건물을 동시에 건설하기
시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 3번 건물이 완성되고 나면 그때 4번
건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다.

프로게이머 최백준은 애인과의 데이트 비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 최백준은 화려한 컨트롤 실력을 가지고 있기
때문에 모든 경기에서 특정 건물만 짓는다면 무조건 게임에서 이길 수 있다. 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은
좌절하고 있었다. 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.
-------------------------------------------
입력
첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N 과 건물간의 건설순서규칙의 총
개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)

둘째 줄에는 각 건물당 건설에 걸리는 시간 D가 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은
다음에 건물 Y를 짓는 것이 가능하다는 의미이다)

마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.
-----------------------------
출력
건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.

모든 건물을 지을 수 없는 경우는 없다.
--------------------------------------------------------------------------------------
제한
2 ≤ N ≤ 1000
1 ≤ K ≤ 100000
1 ≤ X,Y,W ≤ N
0 ≤ D ≤ 100000
--------------------------------------------------------------------------------------
예제 입력 1
------------------------------------------------------------------------------------------------------------------------
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
------------------------------------------------------------------------------------------------------------------------
예제 출력 1
------------------------------------------------------------------------------------------------------------------------
120
39
------------------------------------------------------------------------------------------------------------------------
예제 입력 2
------------------------------------------------------------------------------------------------------------------------
5
3 2
1 2 3
3 2
2 1
1
4 3
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7
------------------------------------------------------------------------------------------------------------------------
예제 출력 2
6
5
399990
2
0
"""
"""
#플로이드 위셜 알고리즘

imp = int(-1e9)
T = int(input())
for A in range(T):
    N, K = map(int, input().split())

    D = list(map(int, input().split()))

    graph = [[imp] * (N+1) for _ in range(N+1)]

    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                graph[a][b]=0

    for i in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = D[X-1]

    W = int(input())

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = max(graph[a][b], graph[a][k]+graph[k][b])
    print(graph[1][W]+D[W-1])
"""
"""
#다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(-1e9)
result=[]
t = int(input())
for A in range(t):
    # 노드의 개수, 간선의 개수 입력받기
    n, m = map(int, input().split())
    # 시작 노드 번호를 입력받기

    # 각 건물당 걸리는시간
    D = list(map(int, input().split()))
    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기

    graph = [[] for i in range(n+1)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance=[INF]*(n+1)

    # 모든 간선 정보를 입력받기
    for _ in range(m):
        a, b= map(int, input().split())
        # a번 노드에서 b번노드로 가는 거리가 c라는 의미
        graph[b].append((a,D[a-1]))

    def improved_dijkstra(start):
        q=[]
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0,0, start))
        distance[start]=0
        while q: # 큐가 빌때까지 반복
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            distminus, dist, now= heapq.heappop(q) # dist, now 변수에 거리와 현재 노드위치 를 q에서 꺼내서 입력
            # 현재 노드를 처리하려 할때 이미처리된 노드거리가 더 짧으면 무시
            if distance[now]>dist:
                continue
            # 현재 노드와 연결된 다른 인접한 노드들 확인
            for i in graph[now]:
                # 인접한 노드들의 거리를 cost 변수에 넣어줌 graph[1]은 거리를 저장한값
                cost = i[1]+dist
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우,
                # i[0]은 인접한 노드 번호 distance[i[0]]은 인접한 노드정보 거리가 저장된 값
                if cost > distance[i[0]]:
                    # 거리정보를 새로 업데이트해줌
                    distance[i[0]]=cost
                    # 우선순위큐 q 에 현재 가장 짧은 해당노드까지의 거리와 해당노드를 푸쉬
                    heapq.heappush(q, (-cost,cost,i[0]))
        # 개선된 다익스트라 알고리즘 수행 , start값으로수행


    # 모든 노드로 가기 위한 최단 거리를 출력 , 노드의 개수가 n개이므로 1부터 n개까지반복을 위해 1, n+1

    w = int(input())
    improved_dijkstra(w)
    result.append(max(distance)+D[w-1])
for C in range(t):
    print(result[C])
"""
"""
import heapq
import sys
input = sys.stdin.readline
imp = int(-1e9)
result = []
t = int(input())
for A in range(t):
    # 노드의 개수, 간선의 개수 입력받기
    n, m = map(int, input().split())

    # 각 건물당 걸리는시간
    D = list(map(int, input().split()))

    graph = [[imp] * (n+1) for _ in range(n+1)]


    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b]=0
    for i in range(m):
        X, Y = map(int, input().split())
        graph[X][Y] = D[X-1]

    W = int(input())

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = max(graph[a][b], graph[a][k]+graph[k][b])
    maxx=0
    for B in graph:
        if B[W]>maxx:
            maxx=B[W]

    result.append(maxx+D[W-1])
print(result)
"""

import sys
input = sys.stdin.readline
from collections import deque

result = []


t = int(input())

for A in range(t):

    n, m = map(int, input().split())
    ingreed = [0 for _ in range(n + 1)]
    distance = [0 for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]

    d = [0]+list(map(int, input().split()))
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        ingreed[y] += 1

    q = deque()
    for i in range(1, n+1):
        if ingreed[i] == 0:
            q.append(i)
            distance[i]=d[i]

    while q:
        a = q.popleft()

        for i in graph[a]:

            ingreed[i] -= 1
            distance[i]=max(d[i]+distance[a], distance[i])
            if ingreed[i]==0:
                q.append(i)
    w= int(input())

    result.append(distance[w])
for i in range(t):
    print(result[i])