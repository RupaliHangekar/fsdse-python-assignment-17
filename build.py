import operator

dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def solution_asc(dic):
    sort_asc = sorted(dic.items(), key=operator.itemgetter(0))
    return sort_asc

def solution_desc(dic):
    sort_desc = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
    return sort_desc

print "sorted in asc: "+str(solution_asc(dic))
print "sorted in desc: "+str(solution_desc(dic))
