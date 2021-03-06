class Iter(object):
    def __init__(self):
        self._list = []
        self._ind = 0

    def __iter__(self):
        self._ind = 0
        return self

    def __next__(self):
        try:
            res = self._list[self._ind]
        except IndexError:
            raise StopIteration
        self._ind+= 1
        return res

    def __setitem__(self, ind, val):
        self._list[ind] = val

    def __delitem__(self, ind):
        del self._list[ind]
        #return

    def appendl(self, other):
        self._list.append(other)

    def remove(self, obj):
        self._list.remove(obj)
    '''
    def index(self, obj):
        return self._list.index(obj)

    def __getitem__(self, ind):
        return self._list[ind]

    def __len__(self):
        return len(self._list)

    def getAll(self):
        return self._list
    '''


def compare(a,b):
    return a<b

def gnomeSort(sortList,compFunc=compare):
    i=0
    n=len(sortList)
    while i<n:
        if i== 0:
            i+=1
        if not compFunc(sortList[i-1],sortList[i]):
            i+=1
        else:
            sortList[i], sortList[i-1] = sortList[i-1], sortList[i]
            i-=1

def filterFunc(p):
    return p[1]>2

def filterList(fList,filterFunc):
    res=[]
    for p in fList:
        if filterFunc(p):
            res.append(p)
    return res

