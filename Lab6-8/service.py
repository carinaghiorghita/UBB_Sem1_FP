from repo import *
import random
from undocontroller import *

class Service:
    def __init__(self,ud,filestud,fileassign,filegrade):
        self._students=StudTextRepo(ud,filestud)
        self._assign=AssignTextRepo(ud,fileassign)
        self._grades=GradeTextRepo(ud,filegrade)
        self._Ud=ud

    def initS(self):
        '''

        :returns the initial list of students
        '''
        i=0
        while i<=9:
            id=random.randint(1,10)
            ok=1
            inst=0
            for s in self._students:
                if id==s.SId:
                    ok=0
                    break
            if ok==1:
                name=self.RandomName()
                for s in self._students:
                    if name == s.Name:
                        inst=s.Inst
                        s.Inst+=1
                group=self.RandomGroup()
                if inst==0:
                    self._students.addS(Student(id,name,group,inst+1))
                else:
                    self._students.addS(Student(id,name+'('+str(inst+1)+')',group,inst+1))
            else :
                i-=1
            i+=1

    def initA(self):
        '''

        :returns the inital list of assignments
        '''
        for i in range(0,10):
            id=random.randint(100,999)
            ok=1
            for j in range(0,i-1):
                if id==self._assign[j].AId:
                    i=i-1
                    ok=0
                    break
            if ok==1:
                desc=self.RandomDesc()
                dead=self.RandomDead()
                self._assign.addA(Assignment(id,desc,dead))
    def RandomDesc(self):
        '''

        :returns a procedurally generated Description of the assignment:
        '''
        desc=['Point','Problem','Exercise','Subsection']
        d=random.randint(0,3)
        w=random.randint(1,100)
        Desc=desc[d]+' '+str(w)
        return Desc
    def RandomDead(self):
        '''

        :returns a procedurally generated DeadLine for the assignment
        '''
        dead=random.randint(1,16)
        Dead=dead
        return  Dead


    def RandomName(self):
        '''

        :returns a procedurally generated name for the student
        '''
        nume=['Alexe','Bulai','Craciun','Dinu','Eftimie','Farcas','Ghilea','Hortan','Iancu','Jochiac']
        prenume=['Alex','Bogdan','Corina','Darius','Elena','Florin','George','Horia','Ioana','John']
        n=random.randint(0,9)
        p=random.randint(0,9)
        Nume=nume[n]+' '+prenume[p]
        return Nume
    def RandomGroup(self):
        '''

       :returns a procedurally generated group for the student
         '''
        group=[911,912,913,914,915,916,917]
        g=random.randint(0,5)
        return group[g]
    def service_addS(self,id,name,group):
        '''

        :param id:
        :param name:
        :param group:
        :return: it adds a new student in the list of students
        '''
        try:
            id=int(id)
        except:
            raise ValidationError("Id should be an integer!")
        try:
            group=int(group)
        except:
            raise ValidationError("Group should be an integer!")
        inst=0
        for s in self._students:
            if name == s.Name:
                inst = s.Inst
                s.Inst += 1
        group = self.RandomGroup()
        if inst == 0:
            self._students.addS(Student(id, name, group, inst + 1))
        else:
            self._students.addS(Student(id, name + '(' + str(inst + 1) + ')', group, inst + 1))
        self._students.addS(s)
    def service_addA(self,id,desc,dead):
        '''

        :param id:
        :param desc:
        :param dead:
        :return: it adds a new assignment in the list of assignments
        '''
        try:
            id=int(id)
        except:
            raise ValidationError("Id should be an integer!")
        try:
            dead=int(dead)
        except:
            raise ValidationError("Description should be an integer!")
        a=Assignment(id,desc,dead)
        self._assign.addA(a)
    def service_removeS(self,id):
        '''

        :param id:
        :return: it removes from students list the student with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("Id should be an integer !")
        self._students.removeS(id)
        op=self._Ud.pop()
        ops = self._grades.deleteGS(id)
        for o in ops:
            op.add(o)
        self._Ud.recordOperation(op)
    def service_removeA(self,id):
        '''

        :param id:
        :return: it removes from assignments list the assignment with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("Id should be an integer !")
        self._assign.removeA(id)
        self._grades.deleteGA(id)
    def service_updaten(self,id,name):
        '''

        :param id:
        :param name:
        :return: it updates the name of the student with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("Id should be an integer !")
        self._students.updaten(id,name)
    def service_updatedesc(self,id,desc):
        '''

        :param id:
        :param desc:
        :return: it updates the description of the assignment with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("Id should be an integer !")
        self._assign.updatedesc(id,desc)

    def service_updateg(self,id,group):
        '''

        :param id:
        :param group:
        :return: it updates the group of the student with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("Id should be an integer !")
        self._students.updateg(id,int(group))
    def service_updatedead(self,id,dead):
        '''

        :param id:
        :param dead:
        :return: it updates the deadline of the assignment with the given id
        '''
        try:
            id=int(id)
        except:
            raise ValueError("ID should be an integer !")
        self._assign.updatedead(id,dead)
    def givestud(self,id1,id2):

        try:
            id1=int(id1)
        except:
            raise ValidationError('The ID of the assignment should be an integer!')
        try:
            id2=int(id2)
        except:
            raise ValidationError('The ID of the student should be an integer!')
        ok=0
        for i in self._assign:
            if i.AId==id1:
                ok=1
                break
        if ok==0:
            raise ValidationError('The assignment ID does not exist')
        ok = 0
        for i in self._students:
            if i.SId == id2:
                ok = 1
                break
        if ok == 0:
            raise ValidationError('The student ID does not exist ')
        for j in self._grades:
            if j.SId==id2 and j.AId==id1:
                ok=0
                break
        if ok==1:
            g=Grade(id2,id1,0)
            self._grades.addG(g)
        else:
            raise AgainError('This student was already assigned this')
    def givegroup(self,id,gr):
        try:
            id=int(id)
        except:
            raise ValidationError('The ID of the assignment should be integer!')
        try:
            gr=int(gr)
        except:
            raise ValidationError('The group should be an integer!')
        ok=0
        for i in self._students:
            if i.Group==gr:
                ok=1
                break
        if ok==0 :
            raise  ValidationError("This group does not exist")
        for j in self._students:
            if j.Group==gr:
                self.givestud(id,j.SId)
    def service_gradestud(self,ids,ida,gr):
        try:
            ids=int(ids)
        except:
            raise ValidationError('The ID of the student should be integer!')
        try:
            ida=int(ida)
        except:
            raise ValidationError('The ID of the assignment should be integer!')
        try:
            gr=int(gr)
        except:
            raise ValidationError('The grade should be an integer!')
        if gr>10 or gr <0:
            raise ValidationError('The grade should be in the interval [0,10]')
        self._grades.gradestud(ids,ida,gr)
    def service_liststud(self,ida):
        try:
            ida=int(ida)
        except:
            raise ValidationError('The ID of the assignment should be an integer!')
        x=self._grades.getstud(ida)
        ids=[]
        gr=[]
        ok=0
        for i in x:
            if ok==0:
                ids.append(i)
                ok=1
            elif ok==1:
                gr.append(i)
                ok=0
        dto=[]
        for i in range(0,len(ids)):
            a=self._students.gividname(ids[i])
            b=gr[i]
            sgr=StudentGr(a,b)
            dto.append(sgr)
        dto.sort()
        return dto
    def service_late(self,week):
        try:
            week=int(week)
        except:
            raise ValidationError("Week should be an integer")
        v=[]
        ok=0
        for i in self._grades:
            if week>int(self._assign.givweek(i.AId)) and i.GradeV==0:
                if self._students.gividname(i.SId) not in v:
                    ok=1
                    v.append(self._students.gividname(i.SId))
        if ok==0:
            raise StudentException("All the students are up to date with their assignment")
        else:
            return v

    def service_best(self):
        v=self._grades
        x=[]
        f=[]
        for i in range(len(v)):
            if v[i].GradeV !=0:
                ids=v[i].SId
                c=1
                s=v[i].GradeV
                if ids not in f:
                    for j in range(i,len(v)):
                        if v[j].SId==ids:
                            s+=v[j].GradeV
                            c+=1
                    x.append(s/c)
                    f.append(ids)

        if len(x)==0:
            raise GradeException("No assignment given")
        else:
            dto = []
            for i in range(len(f)):
                a = (self._students.gividname(f[i]))
                b = x[i]
                savg = StudentAvg(a,b)
                dto.append(savg)
        dto.sort()
        return dto

'''
    def service_avg(self):
        g=self._grades
        a=self._assign
        s=self._students
        for i in range(911,917):
'''


class StudentGr:
    def __init__(self,student,grade):
        self._student=student
        self.__grade=grade
    @property
    def student(self):
        return self._student
    def getgrade(self):

        return self.__grade
    def __lt__(self, other):
        return self.getgrade()>other.getgrade()
    def __str__(self):
        return self.student + ' with the grade: ' + str(self.getgrade())



class  StudentAvg:
    def __init__(self,student,average):
        self._student=student
        self.__avg=average
    @property
    def student(self):
        return self._student
    def __lt__(self, other):
        return self.getavg()>other.getavg()
    def __str__(self):
        return self.student+' with the grade: '+str(self.getavg())
    def getavg(self):
        return self.__avg








