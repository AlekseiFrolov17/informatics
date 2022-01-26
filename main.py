A = [1, 2, 3, -2, 4]
length = len(A)
def h(A):
    global length
    result_list = []
    for i in range(length):
        currrent_element = A[i]
        if currrent_element == 0 or currrent_element -2:
            continue
        B = currrent_element + 2
        result_list.append(B)
        C = (currrent_element + 3) / (currrent_element + 2)
        result_list.append(C)
        D = (currrent_element + 4) / (currrent_element + 3)
        result_list.append(D)
        E = (currrent_element + 5) / (currrent_element + 4)
        result_list.append(E)
        print(B, C, D, E)
    return result_list
result = h(A)
result.sort()
print(result)
