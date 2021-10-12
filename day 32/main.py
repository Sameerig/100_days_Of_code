import smtplib
import datetime as dt
now = dt.datetime.now()
import pandas
import random
today =(now.month,now.day)
##################### Hard Starting Project ######################


my_email = "sameersamig@yahoo.com"
password ="ebswhplgrpshgzef"



data = pandas.read_csv("birthdays.csv")
# print(data)


birthdays_dict ={(data_row["month"],data_row["day"]): data_row for (index ,data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path =f"letter_templates\letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        contents =letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(my_email,password)

        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday\n\n{contents}")

