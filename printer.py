def solution(priorities, location):
    
    change = False
    count = 0

    length = len(priorities)

    if length == 1:
            return 1

    p = priorities

    twoDarray = [[0 for i in range(2)] for j in range(length)]

    for i in range(0, length):
        twoDarray[i][0] = p[i]

    twoDarray[location][1] = -1
    
    while True:
        main = twoDarray[count][0]
        
        for i in range(count, length - 1):
            if main < twoDarray[i][0]:
                twoDarray.append(twoDarray.pop(count))
                change = True
                break
        if not change:
            
            if twoDarray[count][1] == -1:
                count += 1
                return count
            else:
                count += 1
                #인쇄됨
        change = False

print(solution([2, 1, 3, 2], 2))
