n,m = map(int, input().strip().split())
#strip делит по пробельчикам табуляциям, обрубает переводы строки
my_map = []
for i in range(n):
    my_map.append(list(map(int, input().strip().split())))

maxx = -1
for i in range(n):
     for j in range(m):
         if my_map[i][j] > 0:
             q = []
             q.append((i, j))
             my_map[i][j] = 0
             while len(q):
                 cur = q.pop()
                 if i + 1 < n:
                     if my_map[i + 1][j] == my_map[i][j]:
                         print(2)
