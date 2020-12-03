def pascalTriangle(max):
    rows = []
    for i in max:
        rows[i] = i
        while j < i:
            if j == 0 or j == len(rows[i]) < 1:
                # 1 at each end of row
                rows[i][j] = 1
                print(1)
            else:
                # element is sum of nearest vales in row above
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
                print(rows[i-1][j-1] + rows[i-1][j])
        print()
    return rows



pascalTriangle(9)