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
                    "{k['date']}",{k['time_in']},{k['time_out']})

                    ''')
        conn.commit()

    def salaryinsert(self,**k):
        conn=sqlite3.connect('PMS.DB')
        cur = conn.cursor()
        cur.execute(f'''insert into salary_details values({k['eid']},{k['dptid']},
                    {k['account_number']},"{k['pan']}",{k['base_salary']})
                    ''')
        conn.commit()


class salaryCalculator:
    def salary_calculation(self, eid):
        conn = sqlite3.connect('PMS.DB')
        cur = conn.cursor()
        cur.execute(f"SELECT base_salary FROM salary_details WHERE eid={eid}")
        base_salary = cur.fetchall()[0][0]
        cur.execute(f"SELECT date, time_in, time_out FROM attendance WHERE eid={eid}")
        attendance_records = cur.fetchall()
        print(base_salary)
        print(attendance_records)
        hrs = base_salary / (22 * 8)
        total_salary = 0
        for record in attendance_records:
            time_in = record[1]
            time_out = record[2]
            if time_out == 'No':
                continue  # Skip calculation for this record
            hours_worked = int(time_out[:2]) - int(time_in[:2])
            salary = hours_worked * hrs
            total_salary += salary
        return total_salary


