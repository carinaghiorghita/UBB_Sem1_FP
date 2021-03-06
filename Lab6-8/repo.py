from entities import *
from exceptions import *
from undocontroller import *
import pickle
import iterable

class StudentRepo:
    def __init__(self,undoController):
        self._studentRepo=iterable.Iter()
        self._undoController=undoController

    def addS(self,s):
        for stud in self._studentRepo:
            if s.SId==stud.SId:
                raise DuplicateId('You already have this id!')
        undo=FunctionCall(self.removeS,s.SId)
        redo=FunctionCall(self.addS,s)
        op=CascadedOperation(Operation(undo,redo))
        self._undoController.recordOperation(op)
        self._studentRepo.appendl(s)
    def removeS(self,id):
        ok=0
        for i in self._studentRepo:
            if i.SId==id:
                ok=1
                undo = FunctionCall(self.removeS, i.SId)
                redo = FunctionCall(self.addS, i)
                op = CascadedOperation(Operation(redo,undo))
                self._undoController.recordOperation(op)
                self._studentRepo.remove(i)

        if ok==0:
            raise NoID_S("The id you introduced is not in the list of students")
    def updaten(self,id,name):
        ok = 0
        for i in self._studentRepo:
            if i.SId == id:
                ok = 1
                undo = FunctionCall(self.updaten, i.SId, i.Name)
                redo = FunctionCall(self.updaten, i.SId, name)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Name=name
        if ok == 0:
            raise NoID_S("The id you introduced is not in the list of students")
    def updateg(self,id,group):
        ok = 0
        for i in self._studentRepo:
            if i.SId == id:
                ok = 1
                undo = FunctionCall(self.updateg, i.SId, i.Group)
                redo = FunctionCall(self.updateg, i.SId, group)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Group=group
        if ok == 0:
            raise NoID_S("The id you introduced is not in the list of students")
    def gividname(self,id):
        for i in self._studentRepo:
            if i.SId==id:
                return i.Name

    def getallS(self):
        return self._studentRepo[:]

    def listS(self):
        for i in self._studentRepo:
            print(str(i))

    def setList(self, list):
        self._studentRepo = list
    def __getitem__(self, item):
        return self._studentRepo[item]


class StudTextRepo(StudentRepo):
    def __init__(self, ud,fileName):
        StudentRepo.__init__(self,ud)
        self._fileName = fileName
        self.__loadFile(fileName)

    def __loadFile(self,filename):
        file=open(filename,'r')
        while True:
            line=file.readline()

            #end of file
            if line=='':
                break

            #empty line
            elif line=='\n':
                continue
            else:
                line=line.strip().split(",")
                self.addS(Student(int(line[0]),line[1],line[2],1))
        file.close()


    def _writeFile(self):

        f = open(self._fileName, "w")
        for s in self.getallS():
            st = str(s.SId) + "," + s.Name + "," + s.Group +'\n'
            f.write(st)
        f.close()
class StudRepoBinary(StudentRepo):
    def __init__(self,ud,fileName):
        StudentRepo.__init__(self,ud)
        self.__filename = fileName

    def getFileName(self):
        return self.__filename

    def writeFile(self):
        f = open(self.getFileName(), "wb")
        pickle.dump(self.getallS(), f)
        f.close()

    def readFile(self):
        try:
            f = open(self.getFileName(), "rb")
            self.setList(pickle.load(f))
        except EOFError:
            self.__students = []
        except IOError as e:
            print("An error occurred - " + str(e))
            raise e
class AssignmentRepo:
    def __init__(self,undoController):
        self._assignmentRepo=iterable.Iter()
        self._undoController=undoController

    def addA(self,a):
        for i in self._assignmentRepo:
            if i.AId==a.AId:
                raise DuplicateId('You already have this id!')
        undo=FunctionCall(self.removeA,a.AId)
        redo=FunctionCall(self.addA,a)
        op=CascadedOperation(Operation(undo,redo))
        self._undoController.recordOperation(op)
        self._assignmentRepo.appendl(a)
    def removeA(self,id):
        ok=0
        for i in self._assignmentRepo:
            if i.AId==id:
                ok=1
                undo = FunctionCall(self.removeA, i.AId)
                redo = FunctionCall(self.addA, i)
                op = CascadedOperation(Operation(redo, undo))
                self._undoController.recordOperation(op)
                self._assignmentRepo.remove(i)
        if ok==0:
            raise NoID_A("The id you introduced is not in the list of assignments")
    def updatedesc(self,id,desc):
        ok = 0
        for i in self._assignmentRepo:
            if i.AId == id:
                ok = 1
                undo=FunctionCall(self.updatedesc,i.AId,i.Desc)
                redo=FunctionCall(self.updatedesc,i.AId,desc)
                op = CascadedOperation(Operation(undo, redo))
                self._undoController.recordOperation(op)
                i.Desc=desc
        if ok == 0:
            raise NoID_A("The id you introduced is not in the list of assignments")
    def updatedead(self,id,dead):
        ok = 0
        for i in self._assignmentRepo:
            if i.AId == id:
                ok = 1
                undo=FunctionCall(self.updatedead,i.AId,i.Dead)
                redo=FunctionCall(self.updatedead,i.AId,dead)
                op=CascadedOperation(Operation(undo,redo))
                self._undoController.recordOperation(op)
                i.Dead=dead
        if ok == 0:
            raise NoID_A("The id you introduced is not in the list of assignments")

    def givweek(self,id):
        for i in self._assignmentRepo:
            if i.AId==id:
                return  i.Dead

    def listA(self):
        for i in self._assignmentRepo:
            print(str(i))

    def getallA(self):
        return self._assignmentRepo[:]
    def setList(self, list):
        self._assignmentRepo = list

    def __getitem__(self, item):
        return self._assignmentRepo[item]

class AssignTextRepo(AssignmentRepo):
    def __init__(self, ud,fileName):
        AssignmentRepo.__init__(self,ud)
        self._fileName = fileName
        self.__loadFile(fileName)

    def __loadFile(self,filename):
        file=open(filename,'r')
        while True:
            line=file.readline()

            #end of file
            if line=='':
                break

            #empty line
            elif line=='\n':
                continue
            else:
                line=line.strip().split(",")
                self.addA(Assignment(int(line[0]),line[1],int(line[2])))
        file.close()


    def _writeFile(self):

        f = open(self._fileName, "w")
        for a in self.getallA():
            st = str(a.AId) + "," + a.Desc + "," + str(a.Dead) +'\n'
            f.write(st)
        f.close()
class AssignRepoBinary(AssignmentRepo):
    def __init__(self,ud,fileName):
        AssignmentRepo.__init__(self,ud)
        self.__filename = fileName

    def getFileName(self):
        return self.__filename

    def writeFile(self):
        f = open(self.getFileName(), "wb")
        pickle.dump(self.getallA(), f)
        f.close()

    def readFile(self):
        try:
            f = open(self.getFileName(), "rb")
            self.setList(pickle.load(f))
        except EOFError:
            self.__students = []
        except IOError as e:
            print("An error occurred - " + str(e))
            raise e
class GradeRepo:
    def __init__(self,undoController):
        self._gradeRepo=iterable.Iter()
        self._undoController=undoController
    def addG(self,g):
        self._gradeRepo.appendl(g)
        undo = FunctionCall(self.deleteGS, g.SId)
        redo = FunctionCall(self.addG, g)
        op = CascadedOperation(Operation(undo, redo))
        self._undoController.recordOperation(op)
        self._gradeRepo.appendl(g)
    def listG(self):
        for i in self._gradeRepo:
            print(str(i))
    def getallG(self):
        return self._gradeRepo[:]
    def setList(self, list):
        self._gradeRepo = list

    def __getitem__(self, item):
        return self._gradeRepo[item]

    def deleteGS(self,ids):
        res=[]
        remove=[]
        for i in self._gradeRepo:
            if i.SId==ids:
                remove.append(i)
        for i in remove:
                undo = FunctionCall(self.addG, i)
                redo = FunctionCall(self.deleteGS, i.SId)
                op = CascadedOperation(Operation(undo, redo))
                res.append(op)
                self._gradeRepo.remove(i)
        return res
    def deleteGA(self,ida):
        res=[]
        remove=[]
        for i in self._gradeRepo:
            if i.AId==ida:
                remove.append(i)
        for i in remove:
            undo = FunctionCall(self.addG, i)
            redo = FunctionCall(self.deleteGA, i.AId)
            op = CascadedOperation(Operation(undo, redo))
            res.append(op)
            self._gradeRepo.remove(i)


    def gradestud(self,ids,ida,gr):
        ok = 0
        for i in self._gradeRepo:
            if i.SId == ids and i.AId == ida:
                if i.GradeV == 0:
                    i.GradeV = gr
                    ok = 1
                    break
                else:
                    raise GradeError("The grade can not be modified after it was given")
        if ok == 0:
            raise GradeError('The student you selected does not have the assigment you selected')

    def getstud(self,ida):
        l=[]
        ok=0
        for i in self._gradeRepo:
            if i.AId==ida and i.GradeV !=0:
                l.append(i.SId)
                l.append(i.GradeV)
            if i.GradeV==0:
                ok=1
        else:
            if  not l:
                if ok==0:
                    raise GradeError('The assigment you introduced was not given to any of the students')
                else:
                    raise GradeError('The students which have that assignment are currently ungraded')
            else:
                return l

class GradeTextRepo(GradeRepo):
    def __init__(self, ud,fileName):
        GradeRepo.__init__(self,ud)
        self._fileName = fileName
        self.__loadFile(fileName)

    def __loadFile(self,filename):
        file=open(filename,'r')
        while True:
            line=file.readline()

            #end of file
            if line=='':
                break

            #empty line
            elif line=='\n':
                continue
            else:
                line=line.strip().split(",")
                self.addG(Grade(int(line[0]),int(line[1]),int(line[2])))
        file.close()


    def _writeFile(self):

        f = open(self._fileName, "w")
        for g in self.getallG():
            st = str(g.SId) + "," + str(g.AId) + "," + str(g.GradeV) +'\n'
            f.write(st)
        f.close()

class GradeRepoBinary(GradeRepo):
    def __init__(self,ud,fileName):
        GradeRepo.__init__(self,ud)
        self.__filename = fileName

    def getFileName(self):
        return self.__filename

    def writeFile(self):
        f = open(self.getFileName(), "wb")
        pickle.dump(self.getallG(), f)
        f.close()

    def readFile(self):
        try:
            f = open(self.getFileName(), "rb")
            self.setList(pickle.load(f))
        except EOFError:
            self.__students = []
        except IOError as e:
            print("An error occurred - " + str(e))
            raise e