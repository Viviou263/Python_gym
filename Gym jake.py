max = int(input("Quelle est votre poid maximum ?"))

def gym(max):
    gym = {}
    lst = [65,70,75,80,85,90,95]
    for i in range(len(lst)):
        coeff = lst[i]/100
        poid = max*coeff
        gym[lst[i]] = poid
    print(gym)

gym(max)