n=int(input())
al=[]
for i in range(n):
    a,b=map(int,input().split())
    al.append([i,a,b])
al.sort(key=lambda x: (-x[2],x[1]))
current_time = 0
max_end_time = 0
for i,compute, write in al:
    # 完成当前进程的计算
    current_time += compute
    # 计算当前进程的结束时间
    end_time = current_time + write
    # 更新所有进程结束的最晚时间
    max_end_time = max(max_end_time, end_time)
print(max_end_time)



