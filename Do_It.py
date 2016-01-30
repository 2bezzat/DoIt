#!/usr/bin/python2.7
import time
import sys 
import progressbar 
import os 
import csv 
# import termcolor
import datetime

if os.path.isfile('Statistics.csv'):
	pass
else:
	# print colored("file doesn't exist ",'red')
	open('Statistics.csv','a')


def CreateTask():
	taskname =	raw_input("Please enter the Task name:")
	timer =	raw_input("Please enter the Duration in minutes: ")


	while timer.isdigit() == False:
		print "please enter an integr"
		timer = raw_input("Please enter the Duration in minutes: ")


	timer = int(timer)
	timer = timer * 60 
	bar = progressbar.ProgressBar()
	bar.start()


	for i in range(timer):
	   	os.system('clear')
	   	value = (float(i)/ timer )*100
		bar.update(value),
		mins, secs = divmod(i, 60)
	   	timeformat = '{:02d}:{:02d}'.format(mins, secs)
	   	print '\n\n','		Elpased :	',timeformat,'		Remaining  ',timer  -i,'\n'
	   	print "stay focused ....you're working on",taskname
	   	time.sleep(1)



	bar.finish()
	target	=	open('Statistics.csv','a')
	now = datetime.datetime.now()
	num_lines = sum(1 for line in open('Statistics.csv'))
	target.write(str(num_lines)	+','+now.strftime("%d-%m-%Y")+','+now.strftime(" %H:%M")+','+str(timer/60)+','+taskname+'\n')

	print "Goodbye\n"
	
##################End of CreateTask Function######################

def ShowData():

	examplefile = open('Statistics.csv')
	exampleReader = csv.reader(examplefile)
	exampleData = list(exampleReader)
	x = 0 
	y = 0
	z = 0 
	list1= []
	

	for row in exampleData:
		list1.append(row[4])

	list1= set(list1)
	print "Your Tasks \n"
	for row in list1:
		z = z+1 
		print z,"-",row

	matter = raw_input("\nplease enter the matter name:  ")

	print "\n#####Details about ",matter,"######\n"
	for row in exampleData:

		if row[4] == matter :
			y = y+1
			print y,"-","Date:",row[1],"Duration",row[3]
			x = x+ int(row[3]) 
			

	print "\n#you stuided ",matter,y,"Time" 
	print "#You stuided ",matter, float(x) / 60 ,"hours"
############################ End of show data Function###################


print "Welcome To DO_It App :D\n this app easilt let you manage your work and show your progress :D \n hope you enjoy it\n "

print "1-Start new task"
print "2-Show stasticts "

choice = raw_input("\nplease enter your choice:")

while choice.isdigit() == False:
	print "\nplease chooce a choise "
	choice = raw_input("\nplease enter your choice:")




if choice == "1":
	CreateTask()
elif choice == "2": 
	ShowData()






































##################################3 TEST COde #####################
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print timeformat ,'\r'

#         time.sleep(1)
#         # sys.stdout.write(str(timeformat)+' ')
#     	# sys.stdout.flush()
#         t -= 1
#     print('Goodbye!\n\n')

# countdown(timer)

# while timer > 0 :
# 	print timer /60
# 	timer = timer-1
# 	time.sleep(1)

