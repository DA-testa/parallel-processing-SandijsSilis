# python3

import heapq

def parallel_processing(n, m, data):
    output = [(0, i) for i in range(n)]
    heapq.heapify(output)
    threadexec = [0] * n

    result = []
    for i in range(m):
        exec_time, thread = heapq.heappop(output)
        result.append((thread, exec_time))
        exec_time += data[i]
        threadexec[thread] = exec_time
        heapq.heappush(output, (exec_time, thread))

    return result

def main():
    # n = 2
    # m = 5
    # data = [1,2,3,4,5]
    in_type = list(map(int, input().split()))
    n = in_type[0]
    m = in_type[1]
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i,j)



if __name__ == "__main__":
    main()
