#Package and Modules

import string

class PasswordStrengthChecker():
    def __init__(self,fun_Pwd_input):
        self.fun_pwd_input = fun_Pwd_input

        self.specialchracterlist = {"!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", 
                                       "\\", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "`", "~"}
        self.numberlist = string.digits
        self.smallletter = string.ascii_lowercase
        self.capitalletter = string.ascii_uppercase
        
    def is_breached(self, breach_file="Breached_password_list.txt"):
        with open(breach_file, "r", encoding="utf-8", errors="ignore") as f:
            breached_passwords = set(line.strip() for line in f)
        return self.fun_pwd_input in breached_passwords

    def conditions_check(self):
        result =[]

        result.append(" \nLets check your password strength! \n")
        
        #Breach check

        if self.is_breached():
            result.append("This password has been found in a breach, Highly Vulnerable!\n ")
        
        else: 
     
            # Special character

            if any(ch in self.specialchracterlist for ch in self.fun_pwd_input):
                result.append("# - > Contains Special characters ✔")
                
            else:
                result.append("# - > Special character is missing!")

            # Capital letter
            if any(ch in self.capitalletter for ch in self.fun_pwd_input):
                result.append("# - > Contains Uppercase letters ✔")
                
            else:
                result.append("# - > Uppercase letter is missing!")

            # Small letter
            if any(ch in self.smallletter for ch in self.fun_pwd_input):
                result.append("# - > Contains Lowercase letters ✔")
                
            else:
                result.append("# - > Lowercase letter is missing!")

            # Number
            if any(ch in self.numberlist for ch in self.fun_pwd_input):
                result.append("# - > Contains digits ✔")
                
            else:
                result.append("# - > Digit is missing!")
            
            if len(self.fun_pwd_input)>=12:
                result.append(f"# - > Great your password is of length \"{len(self.fun_pwd_input)}\"")

            else:
                length = len(self.fun_pwd_input)

                if length == 1:
                    result.append("❌ Extremely weak password (1 character). It can be cracked instantly.")
                elif length == 2:
                    result.append("❌ Extremely weak password (2 characters). It offers almost no security.")
                elif length == 3:
                    result.append("❌ Very weak password (3 characters). Easily breakable within milliseconds.")
                elif length == 4:
                    result.append("❌ Very weak password (4 characters). Commonly used PIN length and highly insecure.")
                elif length == 5:
                    result.append("❌ Weak password (5 characters). Can be cracked very quickly.")
                elif length == 6:
                    result.append("⚠️ Weak password (6 characters). Vulnerable to brute-force attacks.")
                elif length == 7:
                    result.append("⚠️ Weak password (7 characters). Provides limited protection.")
                elif length == 8:
                   result.append("⚠️ Moderate password (8 characters). Meets minimum standards but still not secure.")
                elif length == 9:
                   result.append("⚠️ Moderate password (9 characters). Better, but still susceptible to attacks.")
                elif length == 10:
                    result.append("✅ Fair password (10 characters). Acceptable, but increasing length is recommended.")
                else:
                    result.append("✅ Strong password (11+ characters). Good level of security.")
        return "\n".join(result)
        
