from datetime import date, timedelta

class weekInfo:
	def __init__(self, date):
		self.weekNumber = 0
		self.monday = 0
		self.tuesday = 0
		self.wednesday = 0
		self.thursday = 0
		self.friday = 0
		self.saturday = 0
		self.sunday = 0
		self.firstDate = 0
		self.lastDate = 0
		self.allDays = []
		self.nbrOfDays = 0

		try:
			self.weekNumber = date[0].weekNumber
			self.firstDate = date[0]
			self.lastDate = date[-1]

		except:
			self.weekNumber = 0

		for n in date:
			#print("IN foor loop")
			#print(type(n))
			#print(n.present())
			match n.getWeekday():
				case "Monday":
					self.monday = n
					self.allDays.append(n)
				case "Tuesday":
					self.tuesday = n
					self.allDays.append(n)
				case "Wednesday":
					self.wednesday = n
					self.allDays.append(n)
				case "Thursday":
					self.thursday = n
					self.allDays.append(n)
				case "Friday":
					self.friday = n
					self.allDays.append(n)
				case "Saturday":
					self.saturday = n
					self.allDays.append(n)
				case "Sunday":
					self.sunday = n
					self.allDays.append(n)

		self.nbrOfDays = len(self.allDays)

	def presentWeek(self):
		t = 1
		print('\n')
		print("Presenting week ")
		self.weekNumber
		try:
			self.monday.present()
		except:
			t = 1
		try:
			self.tuesday.present()
		except:
			t = 1
		try:
			self.wednesday.present()
		except:
			t = 1
		try:
			self.thursday.present()
		except:
			t = 1
		try:
			self.friday.present()
		except:
			t = 1
		try:
			self.saturday.present()
		except:
			t = 1
		try:
			self.sunday.present()
		except:
			t = 1
		print('\n')



class dayInfo:
	def __init__(self, date):
		self.date = date
		self.weekDay = self.getWeekday()
		self.weekNumber = date.isocalendar().week

	def present(self):
		t = 1
		print("SELF.DATE:")
		print(self.date)
		print("SELF.WEEKDAY:")
		print(self.weekDay)
		print("SELF.WEEKNUMBER:")
		print(self.weekNumber)

	def getWeekday(self):
		match self.date.weekday():
			case 0:
				return "Monday"
			case 1:
				return "Tuesday"
			case 2:
				return "Wednesday"
			case 3:
				return "Thursday"
			case 4:
				return "Friday"
			case 5:
				return "Saturday"
			case 6:
				return "Sunday"

def generateLatexHead():
	f = open('latex_header.txt')
	temp = f.read()
	return temp


def generateLatexFoot():
	f = open('latex_footer.txt')
	temp = f.read()
	return temp


def generateLatexWeek():
	return null

start_date = date(2024, 1, 1) 
end_date = date(2024, 12, 31)   
delta = end_date - start_date 

dateList = []

#Add all days in the delta to the dateList
for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    dateList.append(day)

dayInfoList = []

#make a list of dayInfo objects usable for the generation of the calender of the datetime entrys in dateList - 
for n in dateList:
	temp = dayInfo(n)
	dayInfoList.append(temp)



print(generateLatexHead())

allWeeks =[] #A list of weeks
tempWeek = []#Temporary week to append to allWeeks

currentWeekNumber = 0

for n in dayInfoList:
	
	if currentWeekNumber == 0:
		currentWeekNumber = n.weekNumber
		#print("FIRST!")
	if currentWeekNumber == n.weekNumber:
		tempWeek.append(n)
		#print("Added " + str(n.date))
	else:
		temptempweek = weekInfo(tempWeek)
		allWeeks.append(temptempweek)
		#print("Adding week to list")
		tempWeek = []
		tempWeek.append(n)
		currentWeekNumber = n.weekNumber
		#print("New week nr" + str(currentWeekNumber))


#Generate .tex file with calendar info
for n in allWeeks:

	sectionLabel = str(n.weekNumber) + str(n.firstDate.date)
	sectionString = '\\section{Week '+ str(n.weekNumber) + ' ' + str(n.firstDate.date) + ' - ' + str(n.lastDate.date) + '}\\label{sec:'+ sectionLabel + '}'
	indentation = '\\setlength{\\parindent}{0mm}'
	print(indentation)
	print(sectionString)
	print('\emph{Planning}')
	print('\\newline')
	print('\\' + 'begin{formatpage}{}' + '\n' + '\\end{formatpage}')
	print('\pagebreak')



	print('\\vbox{')

	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')
	if n.monday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.monday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Monday ' + str(tempWN) + '  ' + str(tempDate) +'}')
	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('\n')
	print('\\nointerlineskip')
	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')
	print('\\vspace{0.1in}')
	if n.tuesday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.tuesday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Tuesday ' + str(tempWN) + '  ' + str(tempDate) +'}')
	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('}')
	print('\\newpage')

	print('\\vbox{')

	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')
	if n.wednesday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.wednesday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Wednesday ' + str(tempWN) + '  ' + str(tempDate) +'}')
	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('\n')
	print('\\nointerlineskip')
	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')
	print('\\vspace{0.1in}')

	if n.thursday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.thursday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Thursday ' + str(tempWN) + '  ' + str(tempDate) +'}')

	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('}')
	print('\\newpage')

	print('\\vbox{')

	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')

	if n.friday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.friday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Friday ' + str(tempWN) + '  ' + str(tempDate) +'}')

	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('\n')
	print('\\nointerlineskip')
	print('\\begin{minipage}[t][0.5\\textheight][t]{\\textwidth}')
	print('\\vspace{0.1in}')

	if n.saturday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.saturday.date
	else:
		tempWN = ''
		tempDate = ''

	print('\\emph{Saturday ' + str(tempWN) + '  ' + str(tempDate) +'}')
	print('\\newline')
	print('\\' + 'begin{formatday}{}' + '\n' + '\\end{formatday}')
	print('\\end{minipage}')
	print('}')
	print('\\newpage')

	if n.sunday != 0:
		tempWN = n.weekNumber
		tempWN = "- Week " + str(tempWN) + " : "
		tempDate = n.sunday.date
	else:
		tempWN = ''
		tempDate = ''


	print('\\emph{Sunday ' + str(tempWN) + '  ' + str(tempDate) +'}')
	print('\\newline')
	print('\\' + 'begin{formatpage}{}' + '\n' + '\\end{formatpage}')
	



	print('\\newpage')

	print('\\emph{Evaluation}')
	print('\\newline')
	print('\\' + 'begin{formatpage}{}' + '\n' + '\\end{formatpage}')
	


	print('\\newpage')


print(generateLatexFoot())