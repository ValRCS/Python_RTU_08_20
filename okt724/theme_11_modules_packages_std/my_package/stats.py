# some stats functions
# of cours we could import stats standard library but let's create our own

def mean(data):
    return sum(data) / len(data)

def median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        return data[n // 2]