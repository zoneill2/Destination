import os

base = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.dirname(base)
msg_template = os.path.join(base,"email.txt")

content = ""

with open(msg_template,'r') as f:
    content=f.read()

def format_msg(my_name="Zach", my_website="google.com"):
    my_msg = content.format(name=my_name, website=my_website)
    return my_msg