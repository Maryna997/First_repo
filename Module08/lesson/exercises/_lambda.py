def send_email():
    return "Dear King!"
print(send_email())

# lambda function

send_email = lambda: "Dear King!"
print(send_email())

(lambda: print("Dear King!"))()   # the shortest way