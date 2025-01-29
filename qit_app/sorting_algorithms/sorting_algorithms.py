import time


def compare_sorts(input_data):
    results = list()
    methods = [bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort]
    sorted_output = None

    for method in methods:
        start_t = time.time()
        sorted_d = method(input_data)
        end_t = time.time()
        is_sorted = "correct" if check_sorting(sorted_d) else "incorrect"
        if sorted_output is None and is_sorted == "correct":
            sorted_output = str(sorted_d)[1:-1]
        name = " ".join([s.capitalize() for s in method.__name__.split("_")])
        results.append([name, is_sorted, end_t - start_t])

    return sorted_output, results


def check_sorting(data):

    return all([True if data[x] <= data[x + 1] else False for x in range(len(data) - 1)])


# Time complexity:
#   Best:   O(n)
#   Avg:    O(n^2)
#   Worst:  O(n^2)
def bubble_sort(input_data):
    d = input_data.copy()
    n = len(d)

    for i in range(n - 1):
        s = False
        for j in range(n - i - 1):
            if d[j] > d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
                s = True
        if not s:
            break

    return d


# Time complexity:
#   Best:   O(n)
#   Avg:    O(n^2)
#   Worst:  O(n^2)
def insertion_sort(input_data):
    d = input_data.copy()
    n = len(d)

    for i in range(1, n):
        t = d[i]
        j = i - 1
        while j >= 0 and d[j] > t:
            d[j + 1] = d[j]
            j -= 1
        d[j + 1] = t

    return d


# Time complexity:
#   Best:   O(n*log(n))
#   Avg:    O(n*log(n))
#   Worst:  O(n*log(n))
def merge_sort(input_data):
    def merge(t, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        t1 = [t[l + i] for i in range(n1)]
        t2 = [t[m + 1 + i] for i in range(n2)]

        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if t1[i] <= t2[j]:
                t[k] = t1[i]
                i += 1
            else:
                t[k] = t2[j]
                j += 1
            k += 1

        for x in range(i, n1):
            t[k] = t1[x]
            k += 1

        for x in range(j, n2):
            t[k] = t2[x]
            k += 1

    def sort(t, l, r):
        if l < r:
            m = (l + r) // 2
            sort(t, l, m)
            sort(t, m + 1, r)
            merge(t, l, m, r)

    d = input_data.copy()
    n = len(d)

    sort(d, 0, n - 1)

    return d


# Time complexity:
#   Best:   O(n*log(n))
#   Avg:    O(n*log(n))
#   Worst:  O(n^2)
def quick_sort(input_data):
    def swap(t, i, j):
        if i != j:
            t[i], t[j] = t[j], t[i]

    def divide(t, l, r):
        m = l + ((r - l) // 2)
        p = t[m]
        swap(t, m, r)

        k = l
        for i in range(k, r):
            if t[i] < p:
                swap(t, i, k)
                k += 1
        swap(t, k, r)

        return k

    def sort(t, l, r):
        if l < r:
            p = divide(t, l, r)
            sort(t, l, p - 1)
            sort(t, p + 1, r)

    d = input_data.copy()
    n = len(d)

    sort(d, 0, n - 1)

    return d


# Time complexity:
#   Best:   O(n*log(n))
#   Avg:    O(n*log(n))
#   Worst:  O(n*log(n))
def heap_sort(input_data):
    def build(t, m, j):
        h = j
        l = (2 * j) + 1
        r = (2 * j) + 2

        if l < m and t[l] > t[h]:
            h = l
        if r < m and t[r] > t[h]:
            h = r
        if h != j:
            t[h], t[j] = t[j], t[h]
            build(t, m, h)

    d = input_data.copy()
    n = len(d)

    for i in range(n // 2, -1, -1):
        build(d, n, i)

    for i in range(n - 1, 0, -1):
        d[0], d[i] = d[i], d[0]
        build(d, i, 0)

    return d
