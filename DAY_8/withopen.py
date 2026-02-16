
# with open("index.html", 'r') as html_file:
#     for line in html_file:
#         print(line.strip())

"""=> append user input"""


# data_to_append=[

#     "footer>",
#     "<p>Copyright 2026</p>",
#     "</footer>"
# ]
# with open("index.html","a") as html_file:
#     for line in data_to_append:
#         html_file.write(line+"\n")


"""=>append user input """


# user_input=input("html data")
# with open("index.html", "a") as html_file:
#     html_file.write(user_input)

"""=>check whether file exist in directory or not """

import os
check=os.path.exists("hellooo.txt")
print(check)


        