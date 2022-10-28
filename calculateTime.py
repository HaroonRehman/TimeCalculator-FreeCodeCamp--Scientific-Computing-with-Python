import re

## Starting Time

def calculateTime(Sth,Stm,M,Tdh,Tdm,Oparm=False):

    sth = int(Sth)
    stm = int(Stm)
    m = M
    
    
    ## Time Duration
    tdh = int(Tdh)
    
    tdm = int(Tdm)
    
    
    
    oparm = Oparm
    #print('Printing from Line 19 Oparm:',oparm)
    MilitaryTime = 0
    if int(sth) > 12 :
        print('Enter Hours in 12h Format')
        exit()
    
    
    
    if sth == 12 and m == 'pm':
        sth == 00
    elif sth > 12 and m == 'pm':
        sth = 12 - sth
    
    
    
    

    TotalHours = int(sth+tdh)
    #print('Printing Fresh Total Hours from Line 32',TotalHours)
    ## Refining Minutes and Hours to avoid Errors
    
    
    if str(stm).startswith('0'):
        stm = int(stm)
    if str(tdm).startswith('0'):
        tdm = int(tdm)
    if str(sth).startswith('0'):
        sth = int(sth)
    if str(tdh).startswith('0'):
        tdh = int(tdh)
    
    
    
    
    ### Time to add MInutes and get hours from it 
    
    #try:
        
    
    
    add_minutes = stm + tdm
    
    #print('Printing added_minutes from Line 53',add_minutes)
        
    ## Converting Added Minutes to Hours
    if int(add_minutes // 60) > 0:
        ExtractedHours = add_minutes // 60
    if int(add_minutes // 60) == 0:
        ExtractedHours = 00
    
    if int(add_minutes % 60) > 0:
        ExtractedMinutes = add_minutes % 60
    elif int(add_minutes % 60) == 0:
        ExtractedMinutes = 00
    
    try:
        ExtractedHours
        TotalHours = TotalHours+ExtractedHours
        #print('Printing Total Hours from Line 69', TotalHours)
        newHours = TotalHours
        #if TotalHours == 12 and ExtractedMinutes > 0 :
        #    if m == 'pm':
        #        newM = 'am'
        #        newHours = TotalHours
        #    elif m == 'am':
        #        newHours = TotalHours
        #        newM = 'pm'
            
    except:
        TotalHours = int(sth+tdh)
        #print('Printing TotalHours from Line 80',TotalHours)
        newHours = TotalHours 
        ExtractedMinutes = int(stm+tdm)
        if TotalHours == 12 and int(stm+tdm) > 0 :
            if m == 'pm':
                newM = 'am'
                newHours = TotalHours
            elif m == 'am':
                newHours = TotalHours
                newM = 'pm'
    
        
    ## Converting 12 Hours to 24 Hours
    TimeRange = (1,12)
    if TotalHours > 12 and m == 'pm':
        for R in TimeRange:
            if TotalHours == R:
                TotalHours =12+int(R)
                MilitaryTime = TotalHours
    #except:
    #
    #    TotalHours = int(sth+tdh)
    # 2
    
    ##print('#printing from Line 102 Total Hours:', TotalHours)
    
    
    ## Converting Hours into Days 
    #try:
    if int(TotalHours // 24) >= 1:
        Days = int(TotalHours // 24)
        #print('#printing',Days)
        HoursAfterDays = int(TotalHours % 24)
        newHours =HoursAfterDays
        ##print('#printing from line 111 HoursAfterDays',HoursAfterDays)
    
    
    if int(TotalHours % 24) < 12:
        HoursAfterDays = int(TotalHours) % 24
        newM = 'am'
        newHours = HoursAfterDays 
        ##print('#printing line 118 and newHours', newHours)
        if int(TotalHours % 24) == 0:
            HoursAfterDays = 12
            newM = 'am'
            newHours = HoursAfterDays
            ##print('#printing line 124 and HoursAfterDays',newHours)
            ExtractedMinutes = ExtractedMinutes
    
    
    elif int(TotalHours % 24) == 12:
        HoursAfterDays = int(TotalHours % 24)
        newM = 'pm'
        newHours = HoursAfterDays
    elif int(TotalHours % 24) > 12:
        #print(int(TotalHours % 24))
        HoursAfterDays = int(TotalHours % 24)
        newM = 'pm'
        newHours = HoursAfterDays -12
    
    else:
        HoursAfterDays = TotalHours
        ##print('Checkint for 137 Lines Conditin Hours After Days:',HoursAfterDays)
        newHours = HoursAfterDays
        
        
    #except: 
    #
    ## Converting 24 Hours into Hours
    #    HoursAfterDays = TotalHours
    #    if HoursAfterDays > 12:
    #        NewHours = 12-HoursAfterDays
    #        newM = 'pm'
    #    elif HoursAfterDays < 12:
    #        HoursAfterDays = HoursAfterDays
    #        newM = m
    #        NewHours = HoursAfterDays
    
    #try:
    
    ##### Converting 24 Hours into Hours
    ###if HoursAfterDays > 12:
    ###    NewHours = 12-HoursAfterDays
    ###    newM = 'pm'
    ###
    ###
    ###
    ###elif HoursAfterDays < 12:
    ###    HoursAfterDays = HoursAfterDays
    ###    newM = 'am'
    ###    NewHours = HoursAfterDays
    ####except:
    #    pass        
    #
    
    ##print('Testing Days before Line 174 Days:',Days)
    
    try:
        
        if str(oparm).lower() == 'monday':
            d = 1
        elif str(oparm).lower() == 'tuesday':
            d = 2
        elif str(oparm).lower() == 'wednesday':
            d = 3
        elif str(oparm).lower() == 'thursday':
            d = 4
        elif str(oparm).lower() == 'friday':
            d = 5
        elif str(oparm).lower() == 'saturday':
            d = 6
        elif str(oparm).lower() == 'sunday':
            d = 7
        ##print('Now Testing Days in while in Line 190 Days:',Days,d)
        if Days == 1:
            FinalDay = 'next day'
        elif Days > 1:
            DayofWeek = int(Days+d) % 7
            if DayofWeek == 1:
                FinalDay = 'Monday'
            elif DayofWeek == 2:
                FinalDay = 'Tuesday'
            elif DayofWeek == 3:
                FinalDay = 'Wednesday'
            elif DayofWeek == 4:
                FinalDay = 'Thursday'
            elif DayofWeek == 5:
                FinalDay = 'Friday'
            elif DayofWeek == 6:
                FinalDay = 'Saturday'
            elif DayofWeek == 7:
                FinalDay = 'Sunday'
            #print(DayofWeek,d,FinalDay)
    except:
        try:
            if Days == 1:
                FinalDay = 'next day'
            if Days > 1:
                DayofWeek = int(Days) % 7
            if DayofWeek == 1:
                FinalDay = 'Monday'
            elif DayofWeek == 2:
                FinalDay = 'Tuesday'
            elif DayofWeek == 3:
                FinalDay = 'Wednesday'
            elif DayofWeek == 4:
                FinalDay = 'Thursday'
            elif DayofWeek == 5:
                FinalDay = 'Friday'
            elif DayofWeek == 6:
                FinalDay = 'Saturday'
            elif DayofWeek ==7:
                FinalDay = 'Sunday'
        except:
            try:
                if len(oparm) > 1:
                    if str(oparm).lower() == 'monday':
                        d = 1
                    elif str(oparm).lower() == 'tuesday':
                        d = 2
                    elif str(oparm).lower() == 'wednesday':
                        d = 3
                    elif str(oparm).lower() == 'thursday':
                        d = 4
                    elif str(oparm).lower() == 'friday':
                        d = 5
                    elif str(oparm).lower() == 'saturday':
                        d = 6
                    elif str(oparm).lower() == 'sunday':
                        d = 7

                DayofWeek = d

                if DayofWeek == 1:
                    FinalDay = 'Monday'
                elif DayofWeek == 2:
                    FinalDay = 'Tuesday'
                elif DayofWeek == 3:
                    FinalDay = 'Wednesday'
                elif DayofWeek == 4:
                    FinalDay = 'Thursday'
                elif DayofWeek == 5:
                    FinalDay = 'Friday'
                elif DayofWeek == 6:
                    FinalDay = 'Saturday'
                elif DayofWeek ==7:
                    FinalDay = 'Sunday'

            except:
                pass
    try:
        newM
    except:
        newM = m
    
    #print(newHours,TotalHours,ExtractedMinutes)
    try:
        if len(str(ExtractedMinutes))== 1:
            ExtractedMinutes = '0'+str(ExtractedMinutes)
        r = (str(newHours)+':'+str(ExtractedMinutes),newM,str(Days),'Day Of Week:',str(FinalDay))
        
        print('Time:',str(newHours)+':'+str(ExtractedMinutes),newM,'Day:',str(Days),'Day Of Week:',str(FinalDay))
        return r
    except:
        try:
            if len(str(ExtractedMinutes))== 1:
                ExtractedMinutes = '0'+str(ExtractedMinutes)
            print(str(newHours)+':'+str(ExtractedMinutes),newM,'Day Of Week:',str(FinalDay))
            r = (str(newHours)+':'+str(ExtractedMinutes),newM,'Day Of Week:',str(FinalDay))
            return r
        except:
            try:
                if len(str(ExtractedMinutes))== 1:
                    ExtractedMinutes = '0'+str(ExtractedMinutes)
                r = (str(newHours)+':'+str(ExtractedMinutes),newM)

                print(str(newHours)+':'+str(ExtractedMinutes),newM)
                return r
            except:
                r = (str(newHours)+':'+str(ExtractedMinutes),newM)

                if len(str(ExtractedMinutes))== 1:
                    ExtractedMinutes = '0'+str(ExtractedMinutes)
                print(str(newHours)+':'+str(ExtractedMinutes),newM)
                return r
    
    