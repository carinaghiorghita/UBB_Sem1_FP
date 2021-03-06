from domain4 import *

from copy import deepcopy

def AddInsertElem(listTransact,history,tr):
    '''
    Adds a transaction to the list
    params:
        -listTransact: the list of transactions
        -history: the list of former lists of transactions
        -tr: the transaction to be added
    '''
    import copy
    copyList=[]
    copyList=copy.deepcopy(listTransact)
    i=0
    x=-1
    day=getDay(tr)
    while i<len(listTransact)-1 and x==-1:
        if getDay(listTransact[i])>=day:
            x=i
        i+=1
    if x==-1:
        listTransact.append(tr)
    else:
        listTransact.insert(x,tr)
    history.append(copyList[:])

def opt5Filter(listTransact,history,params):
    '''
        Filters transactions by type
        params:
            -listTransact: the list of transactions
            -history: the list of former lists of transactions
            -params: the instruction parameters
    '''
    import copy
    copyList=[]
    copyList=copy.deepcopy(listTransact)
    i=0
    while i<len(listTransact):
        if params[0]!=getType(listTransact[i]):
            del listTransact[i]
        else:
            i+=1
    history.append(copyList[:])

def opt5FilterVal(listTransact,history,params):
    '''
            Filters transactions by type and value
            params:
                -listTransact: the list of transactions
                -history: the list of former lists of transactions
                -params: the instruction parameters
    '''
    import copy
    copyList=[]
    copyList=copy.deepcopy(listTransact)
    i = 0
    while i < len(listTransact):
        if not (getType(listTransact[i])==params[0] and getValue(listTransact[i])<int(params[1])):
            del listTransact[i]
        else:
            i += 1
    history.append(copyList[:])

def opt6Undo(listTransact,history):
    '''
            Undoes the last operation that modified the transaction list
            params:
                -listTransact: the list of transactions
                -history: the list of former lists of transactions
        '''
    if len(history)==0:
        raise ValueError("No more undos")
    listTransact.clear()
    import copy
    copyList=[]
    copyList=copy.deepcopy(history.pop())
    listTransact.extend(copyList)
