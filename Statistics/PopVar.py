n = [5, 3, 1, 2, 4]

def Popvar(n):
    var1 = []
    mean1 = sum(n)/len(n)
    for xs in n:
        var1.append((xs - mean1) ** 2)
