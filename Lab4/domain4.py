
from copy import deepcopy

def getDay(tr):
    return tr["day"]

def getValue(tr):
    return tr["value"]

def getType(tr):
    return tr["type"]

def getDescr(tr):
    return tr["descr"]

def setTr(trday,trvalue,trtype,trdescr):
    return validateTransact(trday,trvalue,trtype,trdescr)

def validateTransact(trday,trvalue,trtype,trdescr):
    if trday<1 or trday>31 or trvalue<0 or (trtype!="in" and trtype!="out"):
        return None
    return {"day":trday,"value":trvalue,"type":trtype,"descr":trdescr}

def initTransact(listTransact):
    listTransact.append(setTr(2,10,"out","coffee"))
    listTransact.append(setTr(7,150,"out","gas"))
    listTransact.append(setTr(10,50,"out","groceries"))
    listTransact.append(setTr(12,1700,"in","salary"))
    listTransact.append(setTr(15,200,"out","food"))
    listTransact.append(setTr(20,1000,"in","gift"))
    listTransact.append(setTr(23,200,"out","jacket"))
    listTransact.append(setTr(24,50,"out","book"))
    listTransact.append(setTr(24,70,"out","fine"))
    listTransact.append(setTr(30,1500,"out","rent"))

def test_opt1Add():
    listTr=[]
    params=[]
    history=[]
    params.append('30')
    params.append('out')
    params.append('food')
    opt1Add(listTr,history,params)
    assert len(listTr)==1
    import datetime
    x = datetime.datetime.now()
    assert getDay(listTr[0])==int(x.strftime("%d"))
    opt1Add(listTr,history,params)
    assert len(listTr)==2
    


def test_opt1Insert():
    listTr=[]
    params=[]
    history=[]
    params.append('15')
    params.append('30')
    params.append('out')
    params.append('food')
    opt1Insert(listTr,history,params)
    assert len(listTr)==1
    opt1Insert(listTr,history,params)
    assert len(listTr)==2



def test_opt2RemoveDayAll():
    listTr=[]
    listTr.append(setTr(2,10,"out","coffee"))
    listTr.append(setTr(2,10,"in","tip"))
    listTr.append(setTr(20,10,"out","coffee"))
    params=[]
    history=[]
    params.append('2')
    opt2RemoveDayAll(listTr,history,params)
    assert len(listTr)==1



def test_opt2RemoveStartEnd():
    listTr=[]
    listTr.append(setTr(2,10,"out","coffee"))
    listTr.append(setTr(10,10,"in","tip"))
    listTr.append(setTr(20,10,"out","coffee"))
    params=[]
    params.append('2')
    params.append('to')
    params.append('10')
    history=[]
    opt2RemoveStartEnd(listTr,history,params)
    assert len(listTr)==1



def test_opt2RemoveTypeAll():
    listTr=[]
    listTr.append(setTr(2,10,"out","coffee"))
    listTr.append(setTr(2,10,"in","tip"))
    listTr.append(setTr(20,10,"out","coffee"))
    params=[]
    history=[]
    params.append('out')
    opt2RemoveTypeAll(listTr,history,params)
    assert len(listTr)==1



def test_opt2Replace():
    listTr=[]
    listTr.append(setTr(2,10,"out","coffee"))
    listTr.append(setTr(2,10,"in","tip"))
    listTr.append(setTr(20,10,"out","coffee"))
    params=[]
    params.append('2')
    params.append('out')
    params.append('coffee')
    params.append('with')
    params.append('15')
    history=[]
    opt2Replace(listTr,history,params)
    assert len(listTr)==3


def test_opt5Filter():
    listTransact=[]
    listTransact.append(setTr(2,10,"out","groceries"))
    listTransact.append(setTr(7,150,"in","gift"))
    params=[]
    params.append("in")
    history=[]
    opt5Filter(listTransact,history,params)
    assert len(listTransact)==1
    assert getType(listTransact[0])=="in"



