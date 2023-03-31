# import sqlite3
# from flask_bcrypt import Bcrypt
# bcrypt= Bcrypt()
# hashed_password = bcrypt.generate_password_hash("giorgiadmin@giorgi.comgiorgiadmin@giorgi.com").decode('utf-8')
# print(hashed_password)
# print(bcrypt.check_password_hash(hashed_password, "giorgiadmin@giorgi.comgiorgiadmin@giorgi.com"))
# # # #
# #
#
# FILE_NAME = "JobsInGeorgia.db"
# TABLE_NAME_1 = 'company_information_jobsingeorgia'
# TABLE_NAME_2 = "salary_rate"
# TABLE_NAME_3 = "user_info"
# TABLE_NAME_4 = "admin_users"
# def createDB():
#
#
#
#     connection = sqlite3.connect(FILE_NAME)
#     db_jobs_in_georgia = connection.cursor()
#
#     db_jobs_in_georgia.execute(""" CREATE TABLE {TABLE_NAME_1} (
#                                                            company_announcer TEXT,
#                                                            company_announcerPhone INTEGER,
#                                                            company_anouncerEmail TEXT,
#                                                            company_name TEXT,
#                                                            company_logo TEXT,
#                                                            company_ID INTEGER,
#                                                            company_mail TEXT,
#                                                            company_Phonenumber INTEGER,
#                                                            company_jobtittle TEXT,
#                                                            company_jobplace TEXT,
#                                                            company_jobShortDesc TEXT,
#                                                            company_jobLongDesc TEXT,
#                                                            company_jobSalary TEXT,
#                                                            company_jobstartdate DATE,
#                                                            company_jobenddate DATE,
#                                                            date_posted DATE,
#                                                            user_id INTEGER)""".format(TABLE_NAME_1=TABLE_NAME_1))
#
#     db_jobs_in_georgia.execute(f" CREATE TABLE {TABLE_NAME_2} (voter_name TEXT,voter_email TEXT,voter_vacancySalary INTEGER,vacancy_id INTEGER,user_id INTEGER)")
#     db_jobs_in_georgia.execute(f" CREATE TABLE {TABLE_NAME_3} (username TEXT,email TEXT,password TEXT)")
#     db_jobs_in_georgia.execute(f" CREATE TABLE {TABLE_NAME_4} (username TEXT,email TEXT,password TEXT)")
#     connection.commit()
#     connection.close()
#
#
#
#
# def user_ckeck(user_email, user_password):
#     connection = sqlite3.connect(FILE_NAME)
#     db_jobs_in_georgia = connection.cursor()
#     db_jobs_in_georgia.execute(f"SELECT * FROM {TABLE_NAME_3} WHERE email='{user_email}' AND password='{user_password}'")
#     items = db_jobs_in_georgia.fetchall()
#     for item in items:
#         print(item[1])
#         print(item[2])
#         if user_email == item[1] and user_password == item[2]:
#             print("success")
#             return True
#         else:
#             print("fail")
#             return False
#
# user_ckeck("test@test.com", "test@test.comtest@test.com")
#
# def deleteRow():
#     connection = sqlite3.connect("JobsInGeorgia.db")
#     db_jobs_in_georgia = connection.cursor()
#     question = input("do you want to delete? ")
#
#     if question == "yes":
#         which_row = int(input("Whhich row? "))
#         db_jobs_in_georgia.execute(f"DELETE FROM company_information_jobsingeorgia WHERE rowid ={which_row}")
#     else:
#         db_jobs_in_georgia.execute("SELECT rowid, * FROM company_information_jobsingeorgia ORDER BY rowid DESC LIMIT 100")
#         items = db_jobs_in_georgia.fetchall()
#         for item in items:
#             print(item)
#
#     connection.commit()
#     connection.close()
#
#
# def createCompanyInfoDB(company_announcer,
#                        company_announcerPhone,
#                        company_anouncerEmail,
#                        company_name,
#                        company_logo,
#                        company_ID,
#                        company_mail,
#                        company_Phonenumber,
#                        company_jobtittle,
#                        company_jobplace,
#                        company_jobShortDesc,
#                        company_jobLongDesc,
#                        company_salary,
#                        company_jobstartdate,
#                        company_jobenddate):
#     connection = sqlite3.connect(FILE_NAME)
#     db_jobs_in_georgia = connection.cursor()
#
#     db_jobs_in_georgia.execute(f"INSERT INTO {TABLE_NAME_1} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
#                                                                                        company_announcer,
#                                                                                        company_announcerPhone,
#                                                                                        company_anouncerEmail,
#                                                                                        company_name,
#                                                                                        company_logo,
#                                                                                        company_ID,
#                                                                                        company_mail,
#                                                                                        company_Phonenumber,
#                                                                                        company_jobtittle,
#                                                                                        company_jobplace,
#                                                                                        company_jobShortDesc,
#                                                                                        company_jobLongDesc,
#                                                                                        company_salary,
#                                                                                        company_jobstartdate,
#                                                                                        company_jobenddate
#                                                                                         ))
#     connection.commit()
#     connection.close()
#
# def showAllDB():
#     connection = sqlite3.connect(FILE_NAME)
#     db_jobs_in_georgia = connection.cursor()
#
#     db_jobs_in_georgia.execute(f"SELECT rowid, * FROM {TABLE_NAME_1} ORDER BY rowid DESC LIMIT 100")
#     items = db_jobs_in_georgia.fetchall()
#     for item in items:
#         print(item)
#
#     connection.commit()
#     connection.close()
#
