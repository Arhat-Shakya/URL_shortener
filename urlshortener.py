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

class url_fetch:
    def __init__(self,code):
        self.code = code
    def fetch(self):
        for val in lst:
            if self.code == val["code"]:
                webbrowser.open(val["url"])
                return f"url opened!"
        else:
            return f"{self.code} was not found!"


#adding or removing the url
ans1 = input("Do you want to enter a url or remove one?(add/remove/none)")
ans_1 = ans1.lower()
if ans_1 == "add" :
    ans_11 = "y"
    while ans_11 == "y" :
        url_name = input("Enter the url")
        nickname = input("Enter the nickname").lower()
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
        nickname = input("Enter the nickname of the url").lower()
        url2= url_remove(nickname)
        print(url2.remove())
        anss = input("Do you want to remove another url too?*(y/n)")
        ans_22 = anss.lower()
elif ans_1 == "none" :
    print("neither added nor removed!")


#changing the nickname
ans2 = input("Do you want to change the nickname?(y/n)")
ans_2 = ans2.lower()
while ans_2 == "y" :
    in1 = input("Enter the nickname you want to change :").lower()
    in2 = input("Enter the new nickname :").lower()
    ch = nickname_change(in1,in2)
    print(ch.change())
    ans2 = input("Do you want to change the nickname again?(y/n)")
    ans_2 = ans2.lower()

#fetching the code by nickname
ans3 = input("Do you want to fetch the code?(y/n)")
ans_3 = ans3.lower()
while ans_3 == "y" :
    in1 = input("Enter the nickname :").lower()
    for val in lst:
        if in1 == val["nickname"] :
            print("The code for your url is :",val["code"])
            in2 = input("Do you want to open the url?(y/n)").lower()
            if in2 == "y" :
                in3 = input("Enter your code here please :")
                url_f = url_fetch(in3)
                print(url_f.fetch())
            else:
                print("url not opened!")
            break
    else:
        print("Nickname not found!")
    ans3 = input("Do you want to fetch another code?(y/n)")
    ans_3 = ans3.lower()


with open("storage.txt","w") as f:
    f.write(str(lst))

with open("show.txt","w") as f :
    f.write(f"{'':<50}{'YOUR CODE LIBRARY'}"+"\n")
    f.write("\n")
    f.write(f"{'S.No.':<8}{'Names':<35}{'Codes':<40}{'URL'}"+"\n")
    i = 1
    for val in lst:
        f.write(f"{i:<8}{val['nickname']:<35}{val['code']:<40}{val['url']}"+"\n")
        i += 1
    f.write("\n")
    f.write(f"{'':<50}{'Library ended here.'}"+"\n")