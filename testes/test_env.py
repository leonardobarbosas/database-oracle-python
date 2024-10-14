from dotenv import load_dotenv

import os

load_dotenv(override=True)

user_ = os.getenv('USER')
print(user_)

pass_ = os.getenv('PASSWORD')
print(pass_)