
def add_time(start, duration,day=""):


    #Splitting and storing the input as a list
    start_Gen = start.split() #based on spaces
    startTime = start_Gen[0].split(":") #the time based on colon
    #start_Gen[1] is holding either AM or PM
    #print(startTime) #Holding the starting time supplied
    duration=duration.split(":") #based on colon
    #print(duration)

    startMinutes = int(startTime[0])*60 + int(startTime[1]) #Start time in minutes
    #print("Total minutes " +str(startMinutes))
    durationMinutes = int(duration[0])*60 + int(duration[1]) #Given duration time in minutes
    #print(durationMinutes)

    totalDurationMinutes = startMinutes + durationMinutes #Total minutes with us
    #print(totalDurationMinutes)

    #Getting total time in hours and minutes
    hoursTotal = totalDurationMinutes//60
    #print(hoursTotal)
    x = round((totalDurationMinutes/60)%1,2) * 60 
    y = round(x)
    
    minsTotal = y
    #print(minsTotal)
    #print(hoursTotal)
    #print(minsTotal)
    #Counting days
    dayC = ((totalDurationMinutes/60) - (startMinutes/60))/24
    #print(dayC)
    dayrem = round((dayC)%1,2)
    #print(dayrem)
    hourrem = dayrem*24
    startDay = (int(startTime[0]) + (int(startTime[1]) / 60 ))
    #print(startDay)
    dayCount = round(dayC)
    extrahours = hourrem+startDay
    extrahours = round(extrahours)
    #print(extrahours)

    if extrahours >= 12 and start_Gen[1]=="PM":
        dayCount+=1
    
    #Deciding AM or PM
    amPMTrack = start_Gen[1]
    if extrahours>=12:
        if start_Gen[1]=="PM":
            amPMTrack = "AM"
        else:
            amPMTrack="PM"
    #print("Days: "+str(dayCount))

    hoursTotalFormatted = hoursTotal
    
    hoursTotalFormatted = hoursTotal%12
    #print(hoursTotalFormatted)
    if hoursTotalFormatted == 0:
        hoursTotalFormatted=12
    
    minsTotalformatted = '%02d' % minsTotal
    #dayTotal = hoursTotal//12
    #print(dayTotal)

    if day: 
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        #index holds which day is sent in the argument
        ind = 0
        for i,myday in enumerate(days):
            if myday.lower()==day.lower():
                ind=i
                break
        #print(index)
        #print(days[index])
        newDay = ""
        if dayCount==0:
            newDay=day
        else:
            ind = (ind+1)%7
            for i in range(1,dayCount+1):
                newDay = days[ind]
                i=i+1
                ind = (ind+1) % 7
        #print(newDay)


    if day:
        if (dayCount==1):
            return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack}, {newDay} (next day)')
        if (dayCount>1):
            return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack}, {newDay} ({dayCount} days later)')
            
        return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack}, {newDay}')

    else:
        if (dayCount==1):
            return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack} (next day)')
        if (dayCount>1):
            return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack} ({dayCount} days later)')
            
        return (f'{hoursTotalFormatted}:{minsTotalformatted} {amPMTrack}')