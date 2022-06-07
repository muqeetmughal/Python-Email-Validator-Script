
from multiprocessing.dummy import Pool as ThreadPool 
import requests
import pandas as pd

import pandas as pd
from email_validator_main import email_validator_function
def validate_current_email(email):
    is_valid = email_validator_function(email)
    return {'Email': email, "is_valid": is_valid}
    
df = pd.read_csv("input_file.csv")
email_list = df["Email"].to_list()
print(email_list)
pool = ThreadPool(100) 

# # called by each thread


results = pool.map(validate_current_email, email_list)


print(results)
print(pd.DataFrame(results))

out = pd.DataFrame(results)

out.to_csv("output.csv", index=False)