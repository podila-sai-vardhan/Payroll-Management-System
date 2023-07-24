from empdetails import Employee
from flask import Flask,render_template,jsonify,request
from empdetails import Employee,salaryCalculator
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

@app.route('/salary',methods=['GET','POST'])
def salary():
    if request.method=='POST':
        eid = request.form.get('eid')
        dptid = request.form.get('dptid')
        account_number = request.form.get('account_number')
        pan = request.form.get('pan')
        base_salary = request.form.get('base_salary')
        print(eid,dptid,account_number)
        emp= Employee()
        emp.salaryinsert(eid=eid,dptid=dptid,account_number=account_number,pan=pan,base_salary=base_salary)
        return render_template('message.html')
    
    return render_template('salary.html')

@app.route('/payroll-release',methods=['GET','POST'])
def payrollrelease():
    if request.method=='POST':
        eid = request.form.get("empid")
        sc = salaryCalculator()
        total_salary= sc.salarycalculation(eid=int(eid))
        context={'employeeid':eid,'Totalsalary':total_salary}
        return render_template('showsalary.html',data=context)
    else:
        return render_template('empid.html')



if __name__=='__main__':
    app.run(host='0.0.0.0',port='5050')




