import collections

c = collections.Counter()
count_of_years = int(input())

for _ in range(count_of_years):
    team = input().split(" ")
    team.sort()
    team = " ".join(team)
    c[team] += 1
print(c.most_common()[0][1])

# ALLA ANNA JON
# ANNA ALLA JON
# JON JOE IVAN
# JOY JON JOE
# ANNA JON JOY