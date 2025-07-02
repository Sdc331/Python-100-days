import smtplib, datetime, random, pandas, os


REC_MAIL = "##########"
PASSWORD = "###########"
ADDR_MAIL = "##########"

today = datetime.datetime.now()


# Check if someone in birthdays list has birthday today

def randomize_letter(recipient):
    rand_file = random.choice(os.listdir("letter_templates"))
    print(rand_file)
    with open(f"letter_templates/{rand_file}") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", recipient)
        return letter
    

def send_letter(recipient, output):
     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(ADDR_MAIL, PASSWORD)
            connection.sendmail(from_addr=ADDR_MAIL, to_addrs=recipient, msg=f"Subject:Happy Birthday!\n\n{output}")



birthdays = pandas.read_csv("birthdays.csv")
for each in range(len(birthdays)):
        data_month = birthdays.iloc[each]['month']
        data_day = birthdays.iloc[each]['day']
        data_name = birthdays.iloc[each]['name']
        data_mail = birthdays.iloc[each]['email']
        today = datetime.datetime.now()
        if today.day == data_day and today.month == data_month:
            output = randomize_letter(data_name)
            send_letter(data_mail, output)
        else:
            pass
