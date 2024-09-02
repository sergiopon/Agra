import sys

def time_for_y(y, segments):
    total_time = 0
    for d, s in segments:
        if s + y <= 0:
            return float('inf')
        total_time += d / (s + y)
    return total_time

def find_y(n, T, segments):
    low, high = -1000, 1000
    while high - low > 1e-7:
        mid = (low + high) / 2
        if time_for_y(mid, segments) > T:
            low = mid
        else:
            high = mid
    return high

input = sys.stdin.read
data = input().split()

index = 0
results = []
while index < len(data):
    n = int(data[index])
    T = int(data[index + 1])
    index += 2
    segments = []
    for _ in range(n):
        d = int(data[index])
        s = int(data[index + 1])
        segments.append((d, s))
        index += 2
    y = find_y(n, T, segments)
    results.append(f"{y:.6f}")

for result in results:
    print(result)