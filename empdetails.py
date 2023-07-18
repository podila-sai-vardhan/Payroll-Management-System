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


