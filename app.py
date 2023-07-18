from empdetails import Employee
from flask import Flask,render_template,jsonify,request
from empdetails import Employee
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee-signup',methods=['GET','POST'])
def  emp_signup():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        dptid = request.form.get('dptid')
        designation = request.form.get('designaion')
        email = request.form.get('email')
        contact = request.form.get('contact_no')
        address = request.form.get('add_y')
        print(eid,ename,dptid)
        emp= Employee()
        emp.emp_insert(eid=eid,ename=ename,dptid=dptid,designation=designation,email=email,contact_no=contact,add_y=address)
        return render_template('message.html')

    else:
        return render_template('signup.html')
    

@app.route('/show-employees',methods=['GET','POST'])
def show_employees():
    emp=Employee()
    data = emp.show_employees()
    return render_template('showemployee.html',employees=data)

@app.route('/attendance',methods=['GET','POST'])
def attendance():
    if request.method=='POST':
        dptid = request.form.get('dptid')
        dptname = request.form.get('dptname')
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        date = request.form.get('date')
        time_in = request.form.get('time_in')
        time_out = request.form.get('time_out')
        print(dptid,dptname,eid)
        emp= Employee()
        emp.attendance(dptid=dptid,dptname=dptname,eid=eid,ename=ename,date=date,time_in=time_in,time_out=time_out)
        return render_template('message.html')
    
    return render_template('attendance.html')



if __name__=='__main__':
    app.run()



emp=Employee()

emp.emp_insert(eid=1,ename='vardhan',dptid=200,designation='Data_Analyst',email='psvardhan@gmail.com',contact_no=6284395326,add_y='hyderabad')