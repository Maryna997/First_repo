users_count = 0

def send_emails_when_fail():
    global users_count
    users_count = 2

send_emails_when_fail()
print(users_count)
