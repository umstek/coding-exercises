from scipy import stats

case_n = int(input())
for i in range(case_n):
    std_n = int(input())
    gpas = list(map(float, input().strip().split()))

    case, r = 0, -9999
    for j in range(5):
        scores = list(map(float, input().strip().split()))
        r_calc = stats.linregress(gpas, scores)[2]
        if r_calc > r:
            r = r_calc
            case = j + 1

    print(case)
