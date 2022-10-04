import math


def grahamScan(points):
    ymin = 99999999;
    xmax = 0;

    for i in range(len(points)):
        if points[i][1] < ymin:
            ymin = points[i][1]
            p = i
        elif points[i][1] == ymin and points[i][0] > xmax:
            xmax = points[i][0]
            p = i
    angles = []

    for i in range(len(points)):
        if i == p: continue
        angles.append((math.atan2(points[i][1] - points[p][1], points[i][0] - points[p][0]), points[i]))

    # angles : 각도가 적은순으로 정렬 (각도, (x좌표, y좌표))
    # angles[0] : 각도, angles[1] : 좌표 ([1][0] : x 좌표, [1][1] : y 좌표)
    angles.sort()

    # 최종 값이 담길 리스트, 시작값 2개 초기화
    result = [points[p], angles[0][1]]

    # 연결하고 convex 한지 (concave or straight) 한지 판단한다.
    cnt = 1
    while cnt < len(angles):
        while len(result) >= 2:
            k = angles[cnt][1]
            j = result.pop()
            i = result[-1]
            if (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) > 0:
                result.append(j)
                break

        result.append(angles[cnt][1])
        cnt += 1

    # 마지막 예외처리
    if (len(result)) >= 3:
        k = points[p]
        j = result[len(result) - 1]
        i = result[len(result) - 2]
        if (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) <= 0:
            result.remove(j)

    # 결과 출력
    for val in result:
        print(val, " ", end='')


if __name__ == "__main__":
    grahamScan(
        [(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1), (-2, -1), (-2, -3), (-3, 3), (-4, 0), (-4, -2),
         (-4, -4)])
