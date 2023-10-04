import random
import smtplib

#dict of boardgame pool and respected weights based on how much we like them
boardgames = {
        "Mansions of Madness": 3,
        "Settlers of Catan": 2,
        "Wingspan": 5,
        "Blood Rage": 4,
        "Scythe": 6,
        "Caverna": 5,
        "Champions of Midgard":5,
        "Dominion": 2,
        "7 Wonders": 5,
        "Viticulture": 5,
        "Inis": 5,
        "Galaxy Trucker": 5,
        "Tokaido": 3,
        "Sheriff of Nottingham": 3,
        "Carcassone": 3,
        "Thunderstone": 4,
        "King of New York": 4,
        "Reavers of Midgard":4,
    }

# select a random boardgame from the dict
def randoBoardgame(boardgames):

    selected_boardgame = random.choices(list(boardgames.keys()), weights=list(boardgames.values()))[0]
    print(selected_boardgame.encode('utf-8'))
    return selected_boardgame

chosen_boardgame = randoBoardgame(boardgames)
sender_email = "iBoardgame@Ommitteddomain.com"
recipient_email = ["ommitted@emails.com"]

subject = "Friday's Boardgame"
body = f"Your boardgame for the week is: {chosen_boardgame}."

#make email and send email
def Email(sender_email, recipient_email, subject, body):
    server = smtplib.SMTP("ommitted")
    server.login(username, password) #these hopefully are stored in a yaml or json in a secure location
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, recipient_email, message.encode("utf-8"))
    server.quit()

#main
def main():
    try:
        Email(sender_email,recipient_email,subject,body)
    except Exception as e:
        print(e)
#dunder main
if __name__ == "__main__":
    main()
