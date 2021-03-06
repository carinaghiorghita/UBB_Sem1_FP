from domain4 import *
from function4 import *
from copy import deepcopy

def showTr(listTransact):
    for tr in listTransact:
        print("day:"+str(getDay(tr))+", value:"+str(getValue(tr))+" ,type:"+getType(tr)+", description:"+getDescr(tr))



def readCommand():
    cmd=input('Command:')
    idx=cmd.find(' ')
    if idx==-1:
        return (cmd,[])
    
    command=cmd[:idx]
    params=cmd[idx:]
    params=params.split()
    for i in range(len(params)):
        params[i]=params[i].strip()
    return (command,params)


def readTransact():
    trday=input("Day of transaction:")
    trvalue=input("Value of transaction:")
    trtype=input("Transaction type:")
    trdescr=input("Description:")
    tr=setTransact(trday,trvalue,trtype,trdescr)
    if tr is not None:
        return tr
    else:
        print("Could not create transaction")

def opt1Add(listTransact,history,params):
    '''
            Adds transaction to current day
            params:
                -listTransact: the list of transactions
                -history: the list of former lists of transactions
                -params: the instruction parameters
    '''
    if len(params)!=3:
        print('Bad command format for <add>')
    else:
        import datetime
        x = datetime.datetime.now()
        trday=int(x.strftime("%d"))
        trvalue=int(params[0])
        tr=setTr(trday,trvalue,params[1],params[2])
        if tr==None:
            print("Could not create transaction")
        else:
            AddInsertElem(listTransact,history,tr)

def opt1Insert(listTransact,history,params):
    '''
            Adds transaction on a given date
            params:
                -listTransact: the list of transactions
                -history: the list of former lists of transactions
                -params: the instruction parameters
     '''
    if len(params)!=4:
        print('Bad command format for <insert>')
    else:
        trday=int(params[0])
        trvalue=int(params[1])
        tr=setTr(trday,trvalue,params[2],params[3])
        if tr==None:
            print("Could not create transaction")
        else:
            AddInsertElem(listTransact,history,tr)

def opt2RemoveDayAll(listTransact,history,params):
    '''
            Remove all transactions on a given date
            params:
                -listTransact: the list of transactions
                -history: the list of former lists of transactions
                -params: the instruction parameters
    '''
    if len(params)!=1:
        print('Bad command format')
    else:
        import copy
        copyList=[]
        copyList=copy.deepcopy(listTransact)
        i=0
        while i<len(listTransact):
            if int(params[0])==getDay(listTransact[i]):
                del listTransact[i]
            else:
                i+=1
    history.append(copyList[:])

def opt2RemoveStartEnd(listTransact,history,params):
    '''
               Remove all transactions between two given dates
               params:
                   -listTransact: the list of transactions
                   -history: the list of former lists of transactions
                   -params: the instruction parameters
    '''
    if len(params)!=3:
        print('Bad command format')
    else:
        import copy
        copyList=[]
        copyList=copy.deepcopy(listTransact)
        i=0
        while i<len(listTransact):
            if int(params[0])<=getDay(listTransact[i]) and int(params[2])>=getDay(listTransact[i]):
                del listTransact[i]
            else:
                i+=1
        history.append(copyList[:])

def opt2RemoveTypeAll(listTransact,history,params):
    '''
               Remove all transactions of a given type
               params:
                   -listTransact: the list of transactions
                   -history: the list of former lists of transactions
                   -params: the instruction parameters
       '''
    if len(params)!=1:
        print('Bad command format')
    else:
        import copy
        copyList=[]
        copyList=copy.deepcopy(listTransact)
        i=0
        while i<len(listTransact):
            if params[0]==getType(listTransact[i]):
                del listTransact[i]
            else:
                i+=1
        history.append(copyList[:])

def opt2Replace(listTransact,history,params):
    '''
               Replaces the value of a transaction with a given date,type and description
               params:
                   -listTransact: the list of transactions
                   -history: the list of former lists of transactions
                   -params: the instruction parameters
    '''
    if len(params)!=5:
        print('Bad command format')
    else:
        import copy
        copyList=[]
        copyList=copy.deepcopy(listTransact)
        i=0
        while i<len(listTransact):
            if int(params[0])==getDay(listTransact[i]) and params[1]==getType(listTransact[i]) and params[2]==getDescr(listTransact[i]):
                listTransact[i]["value"]=int(params[4])
            i+=1
        history.append(copyList[:])

def opt3ListType(listTransact,params):
    '''
               Lists all transaction of a given type
               params:
                   -listTransact: the list of transactions
                   -history: the list of former lists of transactions
                   -params: the instruction parameters
       '''
    if len(params)!=1:
        print('Bad command format')
    else:
        for tr in listTransact:
            if getType(tr)==params[0]:
                print(tr)

def opt3ListCompareValue(listTransact,params):
    '''
         Lists all transaction greater than, smaller than or equal to a given value
             params:
                    -listTransact: the list of transactions
                    -history: the list of former lists of transactions
                    -params: the instruction parameters
    '''
    if len(params)!=2:
        print('Bad command format')
    else:
        if params[0]=='=':
            for tr in listTransact:
                if getValue(tr)==int(params[1]):
                    print(tr)
        elif params[0]=='<':
            for tr in listTransact:
                if getValue(tr)<int(params[1]):
                    print(tr)
        else:
            for tr in listTransact:
                if getValue(tr)>int(params[1]):
                    print(tr)

def opt3ListBalanceDay(listTransact,params):
    '''
             Lists the balance on a given date
                 params:
                        -listTransact: the list of transactions
                        -history: the list of former lists of transactions
                        -params: the instruction parameters
        '''
    if len(params)!=2:
        print('Bad command format')
    else:
        sum=0
        for tr in listTransact:
            if getType(tr)=='in':
                sum+=getValue(tr)
        i=0
        while getDay(listTransact[i])<=int(params[1]):
            if getType(listTransact[i])=='out':
                sum-=getValue(listTransact[i])
            i+=1
        return sum

def opt4Sum(listTransact,params):
    '''
             Calculates the total amount of transactions of a given type
                 params:
                        -listTransact: the list of transactions
                        -history: the list of former lists of transactions
                        -params: the instruction parameters
            Returns the sum
     '''
    if len(params)!=1:
        print('Bad command format')
    else:
        sum=0
        for tr in listTransact:
            if getType(tr)==params[0]:
                sum+=getValue(tr)
        return sum

def opt4Max(listTransact,params):
    '''
             Calculates the maximum amount of transactions of a given type on a given date
                 params:
                        -listTransact: the list of transactions
                        -history: the list of former lists of transactions
                         -params: the instruction parameters
             Returns the max
      '''
    if len(params)!=2:
        print('Bad command format')
    else:
        max=0
        for tr in listTransact:
            if getType(tr)==params[0] and getDay(tr)==int(params[1]) and getValue(tr)>max:
                max=getValue(tr)
        return max

def start():
    history=[]
    listTransact=[]
    initTransact(listTransact)
    while True:
        command=readCommand()
        opt=command[0]
        params=command[1]
        if opt=='add':
            opt1Add(listTransact,history,params)
        elif opt=='insert':
            opt1Insert(listTransact,history,params)
        elif opt=='remove':
            if params[0].isdigit():
                if len(params)==1:
                    opt2RemoveDayAll(listTransact,history,params)
                elif params[1]=='to':
                    opt2RemoveStartEnd(listTransact,history,params)
                else:
                    print('Bad command format')
            elif params[0]=='in' or params[0]=='out':
                opt2RemoveTypeAll(listTransact,history,params)
        elif opt=='replace':
            opt2Replace(listTransact,history,params)
        elif opt=='list':
            if len(params)==0:
                showTr(listTransact)
            elif params[0]=='in' or params[0]=='out':
                opt3ListType(listTransact,params)
            elif params[0] in '<=>':
                opt3ListCompareValue(listTransact,params)
            elif params[0]=='balance':
                print(opt3ListBalanceDay(listTransact,params))
            else:
                print('Bad command format')
        elif opt=='sum':
            print(opt4Sum(listTransact,params))
        elif opt=='max':
            max=(opt4Max(listTransact,params))
            if max == 0:
                print("No transaction with specified type and date")
            else:
                print(max)
        elif opt=='filter':
            if len(params)==1:
                opt5Filter(listTransact,history,params)
            elif len(params)==2:
                opt5FilterVal(listTransact,history,params)
            else:
                print('Bad command format')
        elif opt=='undo':
            opt6Undo(listTransact,history)
        elif opt=='exit':
            return
        else:
            print('Invalid option')

start()

