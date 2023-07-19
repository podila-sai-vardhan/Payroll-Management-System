import sqlite3


class Employee:

    def emp_insert(self,**k):
        conn=sqlite3.connect('PMS.DB')
        cur = conn.cursor()
        cur.execute(f'''insert into employee_details values({k['eid']},"{k['ename']}",
                    {k['dptid']},"{k['designation']}",
                    "{k['email']}",{k['contact_no']},"{k['add_y']}")

                    ''')
        conn.commit()
    
    def show_employees(self):
        conn=sqlite3.connect('PMS.DB')
        cur=conn.cursor()
        cur.execute("select * from employee_details")
        data =[]
        for i in cur.fetchall():
            context={}
            context['eid']=i[0]
            context['ename']=i[1]
            context['dptid']=i[2]
            context['designation']=i[3]
            context['email']=i[4]
            context['contact_no']=i[5]
            context['add_y']=i[6]
            data.append(context)
        return data
    
    def attendance(self,**k):
        conn=sqlite3.connect('PMS.DB')
        cur = conn.cursor()
        cur.execute(f'''insert into attendance values({k['dptid']},"{k['dptname']}",
                    {k['eid']},"{k['ename']}",
                    "{k['date']}","{k['time_in']}","{k['time_out']}")

                    ''')
        conn.commit()

    def salaryinsert(self,**k):
        conn=sqlite3.connect('PMS.DB')
        cur = conn.cursor()
        cur.execute(f'''insert into salary_details values({k['eid']},{k['dptid']},
                    {k['account_number']},"{k['pan']}",{k['base_salary']})
                    ''')
        conn.commit()


class salarycalculator:

    def salarycalculation(self,eid):
        Conn=sqlite3.connect('PMS.DB')
        cur=Conn.cursor()
        cur.execute(f"select base_salary from salary_details where EID={eid}")
        base_salary=cur.fetchall()[0][0]
        cur.execute(f"select date,time_in,time_out from attendance where EID={eid}")
        gt= cur.fetchall()
        print(base_salary)
        print(gt)
        hrs=base_salary/(22*8)
        su=0
        for i in gt:
            g=(int(i[2][:2])-int(i[1][:2]))*hrs
            su=su*g
        return su

