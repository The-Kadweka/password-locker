import pyperclip

class User:
    #class to generate new instance of the users
    user_list = []
    Owner_credetial_list = []
    
    @classmethod
    def confirm_users(cls,email,password):
        old_user = ""
        for user in User.user_list:
               if user.email==email and  user.password == password:
                 old_user = user.email
        return old_user
    
    def __init__(self,first_name,second_name,user_name,email,password):
        self.first_name = first_name
        self.second_name = second_name
        self.user_name = user_name
        self.email = email
        self.password = password    
    
    def save_user(self): #saving objects of the user to the list
        User.user_list.append(self)
    
     
    
    
        
        
class Credetial:
    credetials_list = []
    def __init__(self,Accountname,loginname,accountpasssword):
        
        #docstring for simplicity.....
        
        self.Accountname = Accountname
        self.loginname = loginname
        self.accountpassword = accountpasssword
    
    
    def save_user_credetials(self):
        Credetial.credetials_list.append(self)
        
    def delete_credetials(self):
        Credetial.credetials_list.remove(self)
        
    # def display_credetials(self):
    #     Credetial.credetials_list.display(self)
        
        
@classmethod
def find_by_Accountname(cls,Accountname):
    for credetials in cls.credetial_list:
        if credetials.Accountname == Accountname:
            return credetials

@classmethod
def credetials_exists(cls,Accountname):
        for Accountname in cls.credetials_list:
            if Accountname.Accountname == "Accountname":
                return True
            else:
                return False

@classmethod
def display_credetials(cls):
    return cls.credetials_list