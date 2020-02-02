import time

startDate = input("Exemplo de data a ser digitada 1 12 2000, que será o mesmo que 01\\12\\2000\nDigite a data inicial: ")
currentDate = input("Exemplo de data a ser digitada 1 12 2000, que será o mesmo que 01\\12\\2000\nDigite a data final: ")
startDate = startDate.replace(" ","")
startDate = int(startDate)
currentDate = currentDate.replace(" ","")
currentDate = int(currentDate)
startYear = startDate%10000
startDate = startDate//10000
startMonth = startDate%100
startDay = startDate//100
currentYear = currentDate%10000
currentDate = currentDate//10000
currentMonth = currentDate%100
currentDay = currentDate//100
startSeconds = (startYear,startMonth,startDay,0,0,0,0,0,0)
currentSeconds = (currentYear,currentMonth,currentDay,0,0,0,0,0,0)
startSeconds = time.mktime(startSeconds)
currentSeconds = time.mktime(currentSeconds)
seconds = currentSeconds - startSeconds
days = seconds//86400
print("Se passou %d dias entre : %d\\%d\\%d e %d\\%d\\%d."%(days,startDay,startMonth,startYear,currentDay,currentMonth,currentYear))