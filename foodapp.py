import json
import datetime
from json import JSONDecodeError

#user register method

def register_user(user_json, name, password, age, phn):
    user = {
        "id":1,
        "name":name,
        "password":password,
        "age":age,
        "phone number": phn,
        "order history": {}
    }

    try:
        file=open(user_json,"r+")
        content = json.load(file)
        for i in range(len(content)):
            if content[i]["phone number"] == phn:
                file.close()
                return "User already Exitsts"
        else:
            user["id"] = len(content) + 1
            content.append(user)
    except JSONDecodeError:
        content = []
        content.append(user)
    file.seek(0)
    file.truncate()
    json.dump(content,file,indent =4)
    file.close()
    return "Success"

#update profile

def update_profile(user_json,user_id,name1,password1,age1,phn1):
    file = open("user.json","r+")
    content = json.load(file)

    for i in range(len(content)):
        if (content[i]["id"] == user_id):
            content[i]["name"] == name1
            content[i]["password"] == password1
            content[i]["age"] == age1
            content[i]["phone number"] == phn1
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "Success"


#user order history method

def user_order_history(user_json,user_id):
    file = open(user_json,"r+")
    content = json.load(file)
    for i in range(len(content)):
        #i is index
            print("Order History")
            print("Date | Order")
            for i,j in content[i]["order history"].items():
                print(f"{i} | {j}")
            file.close()
            return True
    file.close()
    return False

#place order method 
def user_place_order(user_json, food_json, user_id, food_name, quantity):
    date = datetime.datetime.today().strftime('%m-%d-%Y')
   # date = "05-22-2022"
    file = open(user_json,"r+")
    content = json.load(file)
    file1 = open(food_json,"r+")
    content1 = json.load(file1)

    for i in range(len(content1)):
        if content1[i]["name"] == food_name:
            if content1[i]["no of plates"] >= quantity:
                for j in range(len(content)):
                    if content[j]["id"] == user_id:
                        content1[i]["no of plates"] -= quantity
                        if date not in content[j]["order history"]:
                            content1[j]["order history"][date] = [content1[i]["name"]]
                        else:
                            content[j]["order history"][date].append(content1[i]["name"])
            else:
                print("please enter less quantity")
                break
        else:
            print("food not available")
            break
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent = 4)
    file.close()

    file.seek(0)
    file.truncate()
    json.dump(content1, file1, indent = 4)
    file1.close()




#add food method

def add_food(food_json, food_name, no_plates = 1):
    food = {
        "id":1,
        "name":food_name,
        "no of plates": no_plates
    }

    try:
        fp = open(food_json,"r+")
        content = json.load(fp)
        for i in range(len(content)):
            if content[i]["name"] == food_name:
                fp.close()
                return "Food Already Available"
        food["id"]=len(content)+1
        content.append(food)
    except JSONDecodeError:
        content = []
        content.append(food)
    fp.seek(0)
    fp.truncate()
    json.dump(content, fp, indent=4)
    fp.close()
    return "Success"

#update food menu method

def update_food(food_json, food_id, no_plates=1):
    file = open(food_json,"r+")
    content = json.load(file)

    for i in range(len(content)):
        if (content[i]["id"] == food_id):
            content[i]["no of plates"] += no_plates
    file.seek(0)
    file.truncate()
    json.dump(content, file, indent=4)
    file.close()
    return "Success"




#remove food

def remove_food(food_json, food_id):
    file = open(food_json,"r+")
    content = json.load(file)

    for i in range(len(content)):
        if content[i]["id"] == food_id:
            del content[i]
            file.seek(0)
            file.truncate()
            json.dump(content, file, indent = 4)
            file.close()
            return "Success"
    return "Pls enter a valid id"

# read food

def read_food(food_json):
    file = open(food_json)
    content = json.load(file)
    print("Menu:")
    for i in range(len(content)):
        print("Id: ", content[i]["id"])
        print(f"---> Name: {content[i]['name']}")
        print(f"---> Number of plates: {content[i]['no of plates']}")

    file.close()
    return True

# login input functionality and Menu

val = input("Do you Want to order Food Y/n: ")
while val.lower() == "y":
    print("Menu: ")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
    val1 = input("Choose one value from the above: ")
    if val1 == "1":
#--------------Register----------------#
        print()
        name = input("Enter the name: ")
        password = input("Enter the password: ")
        age = int(input("Enter your Age"))
        phn = input("Enter the Phn number")
        register_user("user.json", name, password, age, phn)
        
    elif val1 == "2":
#--------------Login-------------------#
        print()
        while True:
            print("1) User")
            print("2) Admin")
            print("3) Exit")
            val2 = input("Choose on value from above: ")
            if val2 == "1":
                print("---------USER--------")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("user.json", "r+")
                content = json.load(file)
                for i in range(len(content)):
                    if content[i]["name"] == user:
                        if content[i]["password"] == password:
                            while True:
                                print()
                                print("1) View Menu")
                                print("2) Place New Order")
                                print("3) Show History of order")
                                print("4) Update Profile")
                                print("5) Exit")
                                val3 = input("Enter your Choice User!! ")
                                if val3 == "1":
                                    read_food("food.json")
                                elif val3 == "2":
                                    user_id = input("Enter User Id:")
                                    food_name = input("Enter the Food You want to Eat")
                                    quantity = int(input("Enter the quantity of food"))
                                    user_place_order("user.json", "food.json", user_id, food_name, quantity)
                                elif val3 == "3":
                                    user_id = input("Enter User Id:")

                                    user_order_history("user.json",user_id)
                                elif val3 == "4":
                                    user_id = input("Enter your User Id:")
                                    name1 = input("Change your name to : ")
                                    password1 = input("Change your password to : ")
                                    age1 = input("Change your age to : ")
                                    phn1 = input("Change your phone number to : ")

                                    update_profile("user.json",user_id,name1,password1,age1,phn1)
                                    
                                else:
                                    print("Thanks FOr Your Visit (Because it was free and you don't have money)")
                                    break
                        else:
                            print("Wrong Password!!")
                    else:
                        print("Wrong Username!!")                            
                
            elif val2 == "2":
                print("$--------Admin------$")
                user = input("Enter name: ")
                password = input("Enter Password: ")
                file = open("admin.json", "r+")
                content = json.load(file)
                if content["name"] == user:
                    if content["password"] == password:
                        while True:
                            print()
                            print("1) Add New Food")
                            print("2) Edit Food")
                            print("3) View Food")
                            print("4) Remove Food") 
                            print("5) Exit")
                            val3 = input("Enter Your Choice Admin!!")
                            if val3 == "1":
                                food_name = input("Enter Food Name: ")
                                no_plates = int(input("Enter the Stock Value: "))
                                add_food("food.json", food_name, no_plates)
                            elif val3 == "2":
                                food_id = input("Enter Food ID: ")
                                no_plates = int(input("Enter the Stock Value: "))
                                update_food("food.json", food_id, no_plates)
                            # Implement ViewFood and Remove Food
                            elif val3 == "3":
                                read_food("food.json")
                            elif val3 == "4":
                                food_id = input("Enter food id to delet : ")
                                remove_food("food.json", food_id)
                            else:
                                break
                                
                    else:
                        print("Wrong Password!!")
                else:
                    print("Wrong Username!!")
            else:
                break
    else:
#--------------Exit--------------------#
        print("Have a great day!!")
        break
