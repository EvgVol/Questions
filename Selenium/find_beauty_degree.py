def find_beauty_degree(n, a):
    max_beauty = 0
    current_beauty = 0
    min_color = 0
    
    for i in range(n):
        if a[i] == min_color + 1:
            current_beauty += 1
            min_color = a[i]
        else:
            min_color = min(min_color, a[i])
    max_beauty = max(max_beauty, current_beauty)
    
    return max_beauty if max_beauty > 0 else 0

n = int(input())
a = list(map(int, input().split()))
print(find_beauty_degree(n, a))

