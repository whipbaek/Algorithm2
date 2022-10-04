
# 기울기 : p0 = (x0, y0), pi = (xi, yi) 일 경우,
#  si = (yi - y0) / (xi - x0)

def collinearPoints(points):
    answer = []
    i = 0
    for p0 in points:
        angles = []
        for pi in points:
            # 본인과 비교하면 넘어간다.
            if p0 == pi : continue
            else:
                angles.append( ((pi[0], pi[1]), ((pi[1] - p0[1])/(pi[0] - p0[0]))) )

        print('p0 : ' , p0)
        list.sort(angles, key=lambda x: (x[0], x[1]))
        for val in angles:
            print(val)

        straight = []
        for a0 in angles :
            temp = []
            for ai in angles:
                if a0 == ai : continue
                else:
                    if a0[1] == ai[1]:
                        temp.append(ai[0])
            if len(temp) >= 3 :
                # temp.append(p0)
                straight.append(temp)


        print('-'*45)
        print('직선 배열')
        for val in straight:
            print(val)

        print()
        print()

    return answer

if __name__ == "__main__":
    if [1,2,3] in [1,2,3,4] : print('yes')
    result = collinearPoints([(19000, 10000), (18000,10000), (32000,10000), (21000, 10000),(1234, 5678), (14000,10000)])
