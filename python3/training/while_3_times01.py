"""定义一种数据类型user_info"""

user_info={
    "alax":{"age":"19", "address":"beijing","password":"123456"},
    "bob":{"age":"30", "address":"shangghai","password":"123456"}
}

def welcome():
    print("*"*40)
    print("\n",
          "add       #add a new user\n",
          "delete    #delete a exsit user\n",
          "update    #Update a user's info\n",
          "find      #find a user is't exsit\n",
          "list      #list all user\n",
          "exit      #exit program\n",
          "\n"
    )
    print("*"*40)


def login():
    n = 3
    r = 0
    while n != 0:
        login_name = input("Please input login name:>>>").strip()
        if login_name in user_info.keys():
            login_pwd = input("Please input password:>>>").strip()
            user=user_info.get(login_name)
            pwd=user.get("password")
            if login_pwd == pwd:
                print("welcome")
                work()
                break
            else:
                print("Passord is wrong")
                r += 1
                n -= 1
                print("rest {} times".format(3 - r))
        else:
            print("Username is wrong")
            n -= 1
            r += 1
            print("rest {} times".format(3 - r))

def add(name,age,address,password):
    if name in user_info.keys():
        print("The name are exsit,Please input another name\n")
    else:
        user_info[name]={"age":age,"address":address,"password":password}

def delete(name):
    """check the name exist or not"""
    if name in user_info.keys():
        del user_info[name]
        print("User {} is deleted".format(name))
    else:
        print("The name is not exist\n")

def update(name,age,address,password):
    if name in user_info.keys():
        user_info[name]={"age":age,"address":address,"password":password}
    else:
        print("This username is not find\n")

def find(name):
    if name in user_info.keys():
        value=user_info.get(name)
        age=value.get("age")
        address=value.get("address")
        password=value.get("password")

        print("{} age is {} and address is {},password is {}".format(name,age,address,"*"*len(password)))
    else:
        print("The name is not found\n")

def list():
    print("name    age   address       password")
    for k in user_info:
        value=user_info.get(k)
        age=value.get("age")
        address=value.get("address")
        password=value.get("password")
        print("{:<8}{:<6}{:<14}{:<8}".format(k,age,address,"*"*len(password)))

def work():
    while True:
        choice = input("\nPlease choice \nadd | delete | update | find | list | exit  \n >>>")
        if choice =="add":
            name = input("name:>>>")
            age = input("age:>>>").strip()
            address = input("address:>>>")
            password = input("password:>>>")
            add(name,age,address,password)
            continue
        elif choice == "delete":
            name = input("name:>>>")
            delete(name)
            continue
        elif choice == "update":
            name = input("name:>>>")
            age = input("age:>>>")
            address = input("address:>>>")
            password = input("password:>>>")
            update(name,age,address,password)
            continue
        elif choice == "find":
            name = input("name:>>>")
            find(name)
            continue
        elif choice == "list":
            list()
            continue
        elif choice == "exit":
            print("bye")
            break


if __name__ == '__main__':
    login()