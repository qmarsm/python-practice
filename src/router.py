
def file_list(obj1):
    obj_read = obj1.read()
    obj_list = obj_read.splitlines()
    return obj_list


def list_dic(obj_list1):
    rout_dic = {}
    for i in obj_list1:
        j = i.split(":")
        rout_dic[j[0]] = j[1]
    return rout_dic


#Main Progarm
object_file = open("routetable.txt")
list1 = file_list(object_file)
route_dic = list_dic(list1)
des = input("Please enter your destination:")
next_des = route_dic[des]
print(next_des)
