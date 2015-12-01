# quiz6b
# question 5
def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result

# question 7
def list_extend(n):
    numbers = range(2,n)
    results = []
    while numbers != []:
        results.append(numbers[0])
        numbers = [n for n in numbers if n % numbers[0]!=0]
    print len(results)
    
list_extend(1000)


# question 8
# the result is the begining of a new year, which equals to the ending of the
# last year
# As a result, the ultimate answer is (result -1)
ps =float(1000)
pf =float(1)
list1 = [1000]
list2 = [1]
while ps > pf:
    ps = ps * 2 * 0.6
    pf = pf *2 * 0.7
    list1.append(ps)
    list2.append(pf)
print list1
print list2
