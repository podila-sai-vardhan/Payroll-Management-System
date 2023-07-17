import sqlite3
conn=sqlite3.connect('PMS.DB')

cur=conn.cursor()

cur.execute("create table employee_details(eid,'ename',dptid,'designation','email',contact_no,'add_y')")
cur.execute("create table salary_details(eid,dptid,account_number,'pan',base_salary)")
cur.execute("create table attendance(dptid,'dptname',eid,'ename',date,time_in,time_out)")
conn.commit()
conn.close()
