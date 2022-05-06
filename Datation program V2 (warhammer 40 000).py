# # # # # # # # # # # # # # #
#                           #
#  Datation Warhammer 40K   #
#                           #
#  Crépuscral de Frôlombre  #
#                           #
# # # # # # # # # # # # # # #
#This program will convert imperial date to gregorian date and vice versa
# # # # # # # # #
#               #
#   parameters  #
#               #
# # # # # # # # #
start=["Welcome to the Warhammer 40K dating program",
       "This program can turn your gregorian date to imperial",
       "And vice-versa",
       "If it's your first time here,read the infos (type 'p')",
       "If you want to convert gregorian to imperial, type 'g'",
       "If you want to convert imperial to gregorian, type 'i'",
       "If you want to quit, type 'quit'",
       "Note that the imperial to gregorian conversion as a",
       "marging error of 5 hours due to the fact that the year",
       "fraction is round down and not precise"]
information=["gregorian date format:",
             "day/month/year-hour/minute/second",
             "exemple: 23 january 2002 at 23H44 and 12 seconds",
             "23/01/2002-23/44/12",
             "imperial date format:",
             "source year fraction . year of millenium . M millenium",
             "exemple: Earth, year fraction 663 (around september) in 2004",
             "0663.004.M3 or 1663.004.M3",
             "Precisions about imperial dating system:",
             "source is between 0 and 9:",
             "01 -> direct source (linked to Terra)(0 or 1)",
             "02 -> in the solar system",
             "03 -> undirect source (contact with source 2 but not 0-1)",
             "04 -> substantiated source (contact with at least source 3 or above)",
             "05 -> under-substantiated source (contact with at least source 4 or above)",
             "06 -> date with a 1 year variation",
             "07 -> date with a 10 year variation",
             "08 -> date with more than 10 year variation",
             "09 -> specifique date to a dating system, unclear date and/or place",
             "year fraction is the date and hour scaled down between 000 and 999",
             "the year fraction is calculated by the day, month and hour of the date"]
sourcing=["Evenement occured on Terra", #01
          "Evenement occured within Sol system", #02
          "Event occurred while someone present for the event was in direct psychic contact with Terra or the Sol system (direct source)", #03
          "An individual or organization present was in psychic contact with a 2 source while the event occurred (undirect source)", #04
          "Individual or organization was in contact with a 3 OR 2 source (substantiated source)", #05
          "Individual or organization was in contact with a 4 source (under-substantiated source)", #06
          "Event in question occurred within 1 years of the date listed in the rest of the Imperial date", #07
          "Event in question occurred within 10 years of the date listed in the rest of the Imperial date", #08
          "Approximated date eg: Warp travel or not an Imperial system"] #09
listmonth=["january",
           "february",
           "march",
           "april",
           "may",
           "june",
           "july",
           "august",
           "september",
           "october",
           "november",
           "december"]
normalyear=[31,28,31,30,31,30,31,31,30,31,30,31] #counting days in a year
leapyear=[31,29,31,30,31,30,31,31,30,31,30,31]
# # # # #
#       #
#  Def  #
#       #
# # # # #
def infos (a):
    for i in range(int(len(information))-1):
        print(information[i])
    x=information[-1]
    return(x)
# # # # #
def gTOi (a):
    #step 01: take the gregorian date
    print("give your date (day/month/year-hour/minute/second-source)")
    b=input()
    #step 02: split all the informations
    b=b.split(sep="-")
    date=b[0]
    moment=b[1]
    source=b[2]
    date=date.split(sep="/")
    moment=moment.split(sep="/")
    #step 03: take appart every informations
    day=date[0]
    month=date[1]
    year=date[2]
    hour=moment[0]
    minute=moment[1]
    second=moment[2]
    #step 04: millenium conversion
    millenium=str(int(year[0:-3])+1)
    year=year[-3:]
    #step 05: convert months into days
    monthTOday=0
    if month!="0":
        #if the date is on january, this part is useless
        #otherwhise, we add the number of days in previous month together
        #but we need to know if it's a leap or normal year (february is 28 or 29 days long)
        if (int(year)%4)==0: #leap year
            for i in range(int(month)-1):
                monthTOday=monthTOday+leapyear[i]
        if (int(year)%4)!=0: #normal year
            for i in range(int(month)-1):
                monthTOday=monthTOday+normalyear[i]
    #step 06: add days of current month tot total days
    monthTOday=monthTOday+int(day)
    #step 07: convert total days int hours
    dayTOhour=monthTOday*24
    #step 08: add hours of current day to total hours
    totalhours=dayTOhour+int(hour)
    #step 09: convert minute to hundredth
    minuteTO100=int(minute)/60
    #step 10: add minute hundredth to total hours
    totalhours=totalhours+minuteTO100
    #step 11: convert second to hundredth
    secondTO100=int(second)/6000
    #step 12: add second hundredth to total hours
    totalhours=totalhours+secondTO100
    #step 13: multiply total hours by 0.11407955
    yearfraction=totalhours*0.11407955
    #step 14: round down year fraction
    yearfraction=int(yearfraction)
    #step 15: rewrite correctly yearfraction
    if int(yearfraction)>=0 and int(yearfraction)<10:
        yearfraction="00"+str(yearfraction)
    if int(yearfraction)>=10 and int(yearfraction)<100:
        yearfraction="0"+str(yearfraction)
    #step 16: create imperial date
    imperialdate=str(source)+str(yearfraction)+"."+str(year)+".M"+str(millenium)
    #step 17: print imperial date
    return(imperialdate)
# # # # #
def iTOg (a):
    #step 01: take the imperial date
    print("give your date (source yearfraction . year .M millenium)")
    b=input()
    #step 02: split all the informations
    b=b.split(sep=".")
    moment=b[0]
    year=b[1]
    millenium=b[2]
    #step 03: take appart every informations
    source=moment[0]
    yearfraction=moment[1:]
    #step 04: millenium conversion
    millenium=str(int(millenium[1:])-1)
    #step 05: create the actual year
    year=millenium+year
    #step 06: divide year fraction by 0.11407955
    totalhours=int(yearfraction)/0.11407955
    #step 07: divide total hours by 24 to get totaldays
    totaldays=totalhours/24
    #step 08: convert total days into day
    days=totaldays
    month=0
    if (int(year)%4)==0:
        while days>=0:
            days=days-leapyear[month]
            month=month+1
        days=days+leapyear[month+1]
    if (int(year)%4)!=0:
        while days>0:
            days=days-normalyear[month]
            month=month+1
        days=days+normalyear[month+1]
    #step 09: convert total days into month
    nummonth=month
    month=listmonth[month-1]
    #step 10: take hour
    monthTOday=0
    malpha=0
    if nummonth!=0:
        if (int(year)%4)==0: #leap year
            for i in range(int(nummonth)-1):
                monthTOday=monthTOday+leapyear[i]
        if (int(year)%4)!=0: #normal year
            for i in range(int(nummonth)-1):
                monthTOday=monthTOday+normalyear[i]
    hour=int(totalhours)-((int(monthTOday)+int(days))*24)
    #step 11: take minute hundredth and second hundredth
    minute=(days-int(days))*100
    second=int((minute-int(minute))*100)
    minute=int(minute)
    #step 12: calculate minute
    minute=int(minute*(6/10))
    #step 13: calculate second
    second=int(second*(6/10))
    #step 14: source conversion
    numsource=source
    source=int(source)
    if source==0:
        source=1
    source=sourcing[source-1]
    #step 15: round up things
    day=int(days)
    if day==0:
        day=day+1
    if day<10:
        day="0"+str(day)
    if hour<10:
        hour="0"+str(hour)
    if minute<10:
        minute="0"+str(minute)
    if second<10:
        second="0"+str(second)
    #step 16: create gregorian date
    gregoriandate0=source+" On the "+str(day)+" "+str(month)+" "+str(year)
    gregoriandate1="At "+str(hour)+"H"+str(minute)+" and "+str(second)+" second"
    gregoriandate=str(day)+"/"+str(nummonth)+"/"+str(year)+"-"+str(hour)+"/"+str(minute)+"/"+str(second)+"-"+str(numsource)
    #step 17: print gregorian date
    print(gregoriandate0)
    print(gregoriandate1)
    return(gregoriandate)
# # # # # # #
#           #
# Program   #
#           #
# # # # # # #
for i in range(len(start)):
    print(start[i])
while True:
    a=input()
    if a=="quit":
        break
    if a=="p":
        print(infos(a))
    if a=="g":
        print(gTOi(a))
    if a=="i":
        print(iTOg(a))
# # # # # # #
#           #
# Appendice #
#           #
# # # # # # #
#exemple of gregorian dates:
#29/08/1993-23/55/00-0
#23/01/2002-17H45/37-2
#exemple of imperial date:
#1662.993.M2
#1092.002.M3
