def send_email_when_ok():
    pass
   

def send_email_when_fail():
    pass

def get_proper_sender(operator):
    if operator == "+":
        return send_email_when_ok
    elif operator == "-":
        return send_email_when_fail
    else:
        raise ValueError("operator is not supported")
    
func = get_proper_sender("-")
print(func)
