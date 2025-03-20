def beziercurve(array_of_points, t):
    #base case
    if len(array_of_points) == 1:
        print(array_of_points[-1])
        return array_of_points[-1]

    #recursive case
    arr = []
    for i in range(len(array_of_points) - 1):
        arr.append((array_of_points[i][0] + (array_of_points[i + 1][0] - array_of_points[i][0]) / 100 * t, (array_of_points[i][1] + (array_of_points[i + 1][1] - array_of_points[i][1]) / 100 * t)))

    return beziercurve(arr, t)

