# import smtplib
#
# my_email = 'pradeepkumarbc138@gmail.com'
# password = 'wmlslxqxdxnpunnd'
#
# with smtplib.SMTP("smtp.gmail.com") as connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pradeepkumarbc716@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of the email.")
#     connection.close()
#
# import datetime as dt
# import smtplib
#
# my_email = 'pradeepkumarbc138@gmail.com'
# password = 'wmlslxqxdxnpunnd'
#
# list_of_quotes = open('quotes.txt', 'r')
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pradeepkumarbc716@gmail.com",
#         msg=f"Subject:Monday\n\nMonday Motivation : {list_of_quotes}")
#     connection.close()

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=2006, month=10, day=20, hour=2, minute=30, second=44)
# print(date_of_birth)



import smtplib
import datetime as dt
import random

MY_EMAIL = 'pradeepkumarbc138@gmail.com'
MY_PASSWORD = 'pradeep@2006'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", ) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n"
        )
