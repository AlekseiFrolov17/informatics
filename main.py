A = [1, 2, 3, -2, 4]
length = len(A)
for i in range(length):
    currrent_element = A[i]
    if currrent_element == 0 or currrent_element -2:
        continue
    B = currrent_element + 2
    C = (currrent_element + 3) / (currrent_element + 2)
    D = (currrent_element + 4) / (currrent_element + 3)
    E = (currrent_element + 5) / (currrent_element + 4)
    print(B, '\n', C, '\n' , D, '\n', E)
