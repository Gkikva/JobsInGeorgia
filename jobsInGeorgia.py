from flask import Flask, jsonify, request,render_template, url_for, flash, redirect
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import send_from_directory

from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, IntegerField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from datetime import datetime



ADMIN_USER_ID = [1]
app = Flask(__name__, static_folder="build", static_url_path="")
CORS(app)
app.config["SECRET_KEY"] = "Aa!@123456"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app_context = app.app_context()
app_context.push()
"""Hash Paswords """
bcrypt= Bcrypt()
"""If user is not loged in then it will redirect into login function
this is the same as url_for , "login" is the name of function"""
login_manager = LoginManager(app)
login_manager.login_view = "login"


# hashed_password = bcrypt.generate_password_hash("123456789").decode('utf-8')
# print(bcrypt.check_password_hash(hashed_password, "123456789"))



class RegistrationForm(FlaskForm):
    username = StringField('მომხმარებელი', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('ელექტრონული ფოსტა', validators=[DataRequired(),Email() ])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    confirm_password = PasswordField('გაიმეორე პაროლი', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("დარეგისტრირდი")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('ამ მომხმარებლით უკვე დარეგისტრირებულია, გთხოვთ ცადოთ სხვა')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('ეს ელექტრონული ფოსტა უკვე დარეგისტრირებულია, გთხოვთ ცადოთ სხვა')


class LoginForm(FlaskForm):
    email = StringField('ელექტრონული ფოსტა', validators=[DataRequired(),Email() ])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("შესვლა")


class salaryRate(FlaskForm):
    vacancy_id = StringField('ვაკანსიის ID', validators=[DataRequired()])
    salary = IntegerField("ხელფასის ოდენობა, მიუთითეთ თვიური ხელფასი", validators=[DataRequired()])
    comment = TextAreaField("დამატებითი კომენტარი", validators=[DataRequired()])
    submit = SubmitField("შესვლა")


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    salary_rate = db.relationship("SalaryRate", backref='author', lazy=True)
    company_info = db.relationship("CompanyInfo", backref='author', lazy=True)

    def __repr__(self):
        return f"User  {self.username} {self.email} "

class CompanyInfo(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_announcer = db.Column(db.String)
    company_announcerPhone = db.Column(db.Integer)
    company_anouncerEmail = db.Column(db.String,)
    company_name = db.Column(db.String)
    company_logo = db.Column(db.String)
    company_ID = db.Column(db.Integer)
    company_mail = db.Column(db.String)
    company_Phonenumber = db.Column(db.Integer)
    company_jobtittle = db.Column(db.Text)
    company_jobplace = db.Column(db.Text)
    company_jobShortDesc = db.Column(db.Text)
    company_jobLongDesc = db.Column(db.Text)
    company_jobSalary = db.Column(db.Text)
    company_jobstartdate = db.Column(db.Text)
    company_jobenddate = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
            return f"Job Information {self.company_announcer} " \
                   f"{self.company_announcerPhone}" \
                   f" {self.company_anouncerEmail}" \


class SalaryRate(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    vacancy_id = db.Column(db.Integer)
    salary_amount = db.Column(db.Integer)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)






@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




""" ROUTES"""
"""==================================="""

"""home page where shown links and posts"""

@app.route('/home', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        print(f">>> {current_user} at home page")
        if request.method == "POST":
            vacancy_id = request.form['inputedValue']
            print(f">>> {vacancy_id} is DELETING the Post")
            """search vacancy by inputed id"""
            if vacancy_id:
                vacancy= CompanyInfo.query.get(vacancy_id)
                user_rates = SalaryRate.query.filter_by(vacancy_id=vacancy_id).all()
                print(f">>> {vacancy}   fount vacancy")
                print(f">>> {user_rates}  and related  rates")
                if vacancy or user_rates:
                    for rate in user_rates:
                        db.session.delete(rate)
                        print(f">>> Deleting rates")
                    db.session.delete(vacancy)
                    db.session.commit()
                    print(f">>> Deleted vacancy and rates")
                    flash("ვაკანსია წაშლილია","success")
                else:
                    print(f">>> {vacancy_id} there is nos this ID")
                    flash("ვაკანსია ვერ მოიძებნა", "danger")
            else:
                flash("ვაკანსიის ID შეიყვანეთ", "danger")
            return redirect(url_for("home"))
        vacancys = CompanyInfo.query.all()
        posts = SalaryRate.query.all()
        return render_template('home.html', posts=posts, ADMIN_USER_ID=ADMIN_USER_ID, vacancys=vacancys)
    else:
        return  f"<div> უნდა შეხვიდეთ სისტემაში რომ ჩაიტვირთოს ეს გვერდი </div><a href='{url_for('login')}'>სისტემაში შესვლა</a>"

"""User Registration route"""
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """if user is loged in redirect into home function"""
    print(f">>> {current_user} on register page")
    if current_user.is_authenticated:
        print(f">>> {current_user} redirected to home")
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user =User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"ექაუნთი შექმნილია {form.username.data}","success")
        print(f">>> {current_user} registered")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)



"""login route"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    """if user is loged in redirect into home function"""
    print(f">>> {current_user} is at login page")
    if current_user.is_authenticated:
        print(f">>> {current_user} already loged in")
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(f">>> {user} has loged in")
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.id in ADMIN_USER_ID:
                print(f"{current_user} you loged in as admins")
                login_user(user)
                flash('წარმატებით შეხვედით სისტემაში როგორც ადმინი', "success")
                return redirect(url_for("home"))
            else:
                print(f">>> {current_user} General user")
                login_user(user)
                flash('წარმატებით შეხვედით სისტემაში', "success")
                return redirect(url_for("home"))
        else:
            flash("ასეთი მონაცემები არ არსებობს", 'danger')
    return render_template('login.html', form=form)

"""LogOut rout"""
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


"""Upload vacancy route"""
@app.route("/uploadVacancy",  methods=['GET', 'POST'])
def uploadVacancy():
    if current_user.is_authenticated:
        user_id = User.query.filter_by(email=current_user.email).first()
        print(f"{current_user} in upload vacancy")
        if request.method == "POST":
            company_info = CompanyInfo( company_announcer= request.form["anonouncerFullN"],
                                        company_announcerPhone = request.form["announcerPhone"],
                                        company_anouncerEmail = request.form["anouncerPrivateEmail"],
                                        company_name = request.form["companyName"],
                                        company_logo = request.form["companylogo"],
                                        company_ID = request.form["companyCode"],
                                        company_mail = request.form["companyMail"],
                                        company_Phonenumber = request.form["companynumber"],
                                        company_jobtittle =  request.form["companyjobtittle"],
                                        company_jobplace = request.form["companyjobplace"],
                                        company_jobShortDesc =  request.form["companyjobshortdescription"],
                                        company_jobLongDesc =   request.form["companyjoblongtdescription"],
                                        company_jobSalary = request.form["jobSalary"],
                                        company_jobstartdate = request.form["jobstartDate"],
                                        company_jobenddate =  request.form["jobendDate"],
                                        user_id =user_id.id
                                       )
            db.session.add(company_info)
            db.session.commit()
            print(f">>> {current_user} uploaded vacancy")
            flash('წარმატებით აიტვირთა ვაკანსია', "success")
        return render_template('uploadVacancy.html')
    else:
        return  f"<div> უნდა შეხვიდეთ სისტემაში რომ ჩაიტვირთოს ეს გვერდი </div><a href='{url_for('login')}'>სისტემაში შესვლა</a>"

"""Register Vacancy into DB"""
@app.route('/salaryRate', methods=['GET', 'POST'])
@login_required
def salaryRate():
    if current_user.is_authenticated:
        print(f">>> {request.method} at salary rate page")
        if request.method == "POST":
            info = SalaryRate(
                vacancy_id = request.form["vacanyId"],
                salary_amount =request.form["salaryRate"],
                comment = request.form["comment_salary"],
                user_id = current_user.id
            )
            db.session.add(info)
            db.session.commit()
            print(f">>> {current_user} gave rate")
            flash("წარმატებით აიტვირთა მინიჭებული ხელფასის რაოდენობა","success")
        return render_template("salaryRate.html")
    else:
        return  f"<div> უნდა შეხვიდეთ სისტემაში რომ ჩაიტვირთოს ეს გვერდი </div><a href='{url_for('login')}'>სისტემაში შესვლა</a>"

"""Send Data"""
@app.route('/api/data', methods=['GET', 'POST'])
@cross_origin()
def send_data():
    def salary_rate(vacancy_id):
        found_vacancies = SalaryRate.query.filter_by(vacancy_id=vacancy_id).all()
        count = SalaryRate.query.filter_by(vacancy_id=vacancy_id).count()
        total = 0
        
        for vacancies in found_vacancies:
            total += vacancies.salary_amount
        """to take away error> divide zero error"""
        if count == 0:
            return total/1
        else:
            print(f"this is count  {count}")
            return total/count
            
    def salary_count(vacancy_id):
        return SalaryRate.query.filter_by(vacancy_id=vacancy_id).count()
    
    """We sending last Updated DB with 300 limit row"""
    items = CompanyInfo.query.order_by(CompanyInfo.id.desc()).limit(300).all()
    list_for_react = []
    for item in items:
        salary_amount = round(salary_rate(item.id))
        costumer_count = salary_count(item.id)
        print(f"this is average salary {salary_amount}")
        print(f"this is count {costumer_count}")
        company_ID = item.id
        company_name = item.company_name
        company_logo = item.company_logo
        company_mail = item.company_mail
        company_Phonenumber = item.company_Phonenumber
        company_jobtittle = item.company_jobtittle
        company_jobplace = item.company_jobplace
        company_jobShortDesc = item.company_jobShortDesc
        company_jobLongDesc = item.company_jobLongDesc
        company_jobSalary = item.company_jobSalary
        company_jobstartdate = item.company_jobstartdate
        company_jobenddate = item.company_jobenddate
        data_object ={
                    "id":company_ID,
                    "CompanyName":company_name,
                    "CompanyImage": company_logo,
                    "CompanyEmail":company_mail,
                    "companyPhone":company_Phonenumber,
                    "CompanyJobTitle":company_jobtittle,
                    "JobPlace":company_jobplace,
                    "CompanyJobShortDesciption":company_jobShortDesc,
                    "CompanyJobLongDesciption":company_jobLongDesc,
                    "CompanyJobSalary": company_jobSalary,
                    "companyJobStartDate": company_jobstartdate,
                    "companyJobEndDate":company_jobenddate,
                    "customSalary": salary_amount
        }
        list_for_react.append(data_object)

    return jsonify(list_for_react)

# send_data()


@app.route("/")
@cross_origin()
def serve():
    print(f">>> {current_user} is at index page")
    return send_from_directory(app.static_folder, "index.html")




if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
    app.run(debug=True)
