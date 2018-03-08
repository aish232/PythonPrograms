all_student=[
    {"name":"Naba","s_id":841635},
    {"name":"Komal","s_id":841634},
    {"name":"Harshit","s_id":841633}

]

print (all_student[2]["name"])
print (all_student[0]["s_id"])

for i in all_student:
    print("{}".format(i["s_id"]))

for i in all_student:
    print("Rollno of {} is {}".format(i["name"],i["s_id"]))