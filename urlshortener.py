import ast
import string
import secrets
import webbrowser

lst = []

with open("storage.txt","r") as f:
    lst1 = f.readline()
    if lst1 != "" :
        lst = ast.literal_eval(lst1)
    elif lst1 == "" :
        lst = []


class url_input:
    def __init__(self,url,nickname,code):
        self.url = url
        self.nickname = nickname
        self.code = code
    def input1(self):
        self.dit = {}
        for val in lst:
            if self.url == val["url"] :
                return f"The url is already stored with the nickname {val["nickname"]}"
        else:
            self.dit["nickname"] = self.nickname
            self.dit["code"] = self.code
            self.dit["url"] = self.url
            lst.append(self.dit)
            return f"The new url is added as the nickname {self.nickname}"

class url_remove:
    def __init__(self,nickname):
        self.nickname = nickname
    def remove(self):
        for val in lst:
            if self.nickname == val["nickname"] :
                lst.remove(val)
                return f"The url is removed!"
        else:
            return f"{self.nickname} didn't found!"


class nickname_change:
    def __init__(self,old,new):
        self.old = old
        self.new = new
    def change(self):
        for val in lst:
            if self.old == val["nickname"] :
                val["nickname"] = self.new
                return f"{self.old} changed to {self.new}"
        else:
            return f"There isn't {self.old}"



#adding or removing the url
ans1 = input("Do you want to enter a url or remove one?(add/remove)")
ans_1 = ans1.lower()
if ans_1 == "add" :
    ans_11 = "y"
    while ans_11 == "y" :
        url_name = input("Enter the url")
        nickname = input("Enter the nickname")
        characters = string.ascii_letters + string.digits
        code = ""
        for _ in range(6) :
            code += secrets.choice(characters)
        url1 = url_input(url_name,nickname,code)
        print(url1.input1())
        anss = input("Do you want to enter a new url?(y/n)")
        ans_11 = anss.lower()
elif ans_1 == "remove" :
    ans_22 = "y"
    while ans_22 == "y" :
        nickname = input("Enter the nickname of the url")
        url2= url_remove(nickname)
        print(url2.remove())
        anss = input("Do you want to remove another url too?*(y/n)")
        ans_22 = anss.lower()


#changing the nickname
ans2 = input("Do you want to change the nickname?(y/n)")
ans_2 = ans2.lower()
while ans2 == "y" :
    in1 = input("Enter the nickname you want to change :")
    in2 = input("Enter the new nickname :")
    ch = nickname_change(in1,in2)
    print(ch.change())
    ans2 = input("Do you want to change the nickname again?(y/n)")
    ans_2 = ans2.lower()

#finding the code by nickname