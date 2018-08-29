# coding: UTF-8
str ="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = str.replace(',',"")
str = str.replace('.',"")
str = str.split(" ")

list = [len(i) for i in str]


print list
