
#README
#Copy / Paste this script

import re
def checkmail(x):
    if re.search("^[a-zA-Z0-9\\._]+@[a-z0-9]+.[a-z]+$", x):
        print("Valid adress")
    else:
        print("Invalid adress")

#README
#Type checkmail(X) and replace 'X' with the mail whose syntax you want to check.
# You must put the mail adress in quotation marks ('' or "")

#Exemples:

checkmail('tommybananes234@hotmail.fr')      #
checkmail('louise.sandiego39012@gmail.com')  # Should return valid
checkmail('CAROLINA.database_666@proton.me') #



checkmail('RATATAC^@yahoo.fr') #Should return invalid due to '^' character
checkmail('MisterRavioles-pro@enterprise.com') #Should return invalid due to '-' character