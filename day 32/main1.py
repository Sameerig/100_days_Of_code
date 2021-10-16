import smtplib

import datetime as dt
import random
now = dt.datetime.now()


my_email = ""
password =""



weekday = now.weekday()
if weekday==0:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)

    print(quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email
        ,to_addrs=my_email,
        msg=f"Subject:Tuesday Motivation\n\n {quote}")
