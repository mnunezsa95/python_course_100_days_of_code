# ------------------------------------------------------------------------------------------------ #
#                                        Birthday Wisher App                                       #
# ------------------------------------------------------------------------------------------------ #
import datetime as dt
import smtplib
import pandas as pd
import random

with open("sensitive_info/day_32_credentials.txt") as credentials:
    credentialsArray = credentials.readlines()
    MY_EMAIL = str(credentialsArray[0])
    MY_PASSWORD = str(credentialsArray[1])


today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pd.read_csv("day_32/day_32_project/birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(
        f"day_32/day_32_project/letter_templates/letter_{random.randint(1, 3)}.txt"
    ) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}",
        )
