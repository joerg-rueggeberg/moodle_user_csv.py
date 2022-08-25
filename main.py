import os

FILEPATH = os.environ.get("FILEPATH")

adding = True
data_mail = []
data = {
    "headline": "username,firstname,lastname,email,password",
    "user": [],
    "email_start": input("Wie lautet die letzt aktuelle E-Mail? "),
    "password": input("Welches Passwort? "),
}
umlaute = ["Ä", "Ö", "Ü", "ä", "ö", "ü"]
umlaute_neu = ["Ae", "Oe", "Ue", "ae", "oe", "ue"]


def mail_prep():
    global data_mail
    email = data["email_start"]
    data_mail.append(email.split("@")[0][:-3])
    data_mail.append(int(email.split("@")[0][-3:]))
    data_mail.append(email.split("@")[1])


def new_user():
    global data_mail
    global data

    data_mail[1] += 1

    if len(str(data_mail[1])) == 1:
        mail_num = f"00{data_mail[1]}"
    elif len(str(data_mail[1])) == 2:
        mail_num = f"0{data_mail[1]}"
    else:
        mail_num = data_mail[1]

    mail_new = f"{data_mail[0]}{mail_num}@{data_mail[2]}"
    firstname = input("Vorname? ")
    lastname = input("Nachname? ")

    lastname_edit = [umlaute_neu[umlaute.index(c)] if c in umlaute else c for c in lastname]
    lastname_edit = "".join(lastname_edit)

    username = f"{firstname[0]}{lastname_edit}".lower()
    data_user = [f"{username},{firstname.title()},{lastname.title()},{mail_new},{data['password']}"]
    data["user"].append(data_user)


def next_user():
    global adding
    adding_input = input("Weiteren Nutzer anlegen (j/n)? ").lower()
    if adding_input == "n":
        adding = False
    elif adding_input == "j":
        adding = True
    else:
        print("Falsche Eingabe. Vorgang abgebrochen.")


def write_data():
    for i in data["user"]:
        with open(FILEPATH, "a+") as file_user:
            file_user.write(f"{str(i[0])}\n")


# SCRIPT
with open(FILEPATH, "w") as file:
    file.write(f"{data['headline']}\n")

mail_prep()

while adding:
    new_user()
    next_user()

write_data()
