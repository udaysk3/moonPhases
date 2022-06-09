def getPhaseno(num_of_days,phase,illumination):
    illumination = int(illumination)
    if num_of_days == 31:
            if phase == 'Dark Moon':
                phase_no = 0
            elif phase == 'New Moon':
                phase_no = 0
            elif(phase == 'Waxing Crescent'):
                if illumination <=2:
                    phase_no = 1
                elif illumination>2 and illumination<7:
                    phase_no = 2
                elif illumination>=7 and illumination<18:
                    phase_no = 3
                elif illumination>=18 and illumination<29:
                    phase_no = 4
                elif illumination>=29 and illumination<39:
                    phase_no = 5
                elif illumination>=39 and illumination<49:
                    phase_no = 6
                elif illumination>=49:
                    phase_no = 7
            elif phase=='1st Quarter':
                if illumination>=50 and illumination<=55:
                    phase_no = 8
                else:
                    phase_no = 9
            elif(phase == 'Waxing Gibbous'):
                if illumination <=70:
                    phase_no = 10
                elif illumination>70 and illumination<=80:
                    phase_no = 11
                elif illumination>80 and illumination<=89:
                    phase_no = 12
                elif illumination>89 and illumination<=95:
                    phase_no = 13
                elif illumination>95 and illumination<=98:
                    phase_no = 14
                elif illumination>98 and illumination<=99:
                    phase_no = 15
            elif phase=='Full Moon':
                if illumination==100:
                    phase_no = 16
                else:
                    phase_no = 17           
            elif(phase == 'Waning Gibbous'):
                if illumination >96:
                    phase_no = 18
                elif illumination<98 and illumination>=93:
                    phase_no = 19
                elif illumination<93 and illumination>=86:
                    phase_no = 20
                elif illumination<86 and illumination>=77:
                    phase_no = 21
                elif illumination<77 and illumination>=67:
                    phase_no = 22
                elif illumination<67 and illumination>=50:
                    phase_no = 23    
            elif phase== '3rd Quarter':
                if illumination>50:
                    phase_no = 24
                else:
                    phase_no = 25
            elif(phase == 'Waning Crescent'):
                if illumination>=37:
                    phase_no = 26
                elif illumination<37 and illumination>=29:
                    phase_no = 27
                elif illumination<29 and illumination>=20:
                    phase_no = 28
                elif illumination<20 and illumination>=7:
                    phase_no = 29
                elif illumination<7 and illumination>=1:
                    phase_no = 30 
            elif phase== 'Dark Moon':
                   phase_no = 31
    elif num_of_days == 30:
            if phase == 'Dark Moon':
                phase_no = 0
            elif phase == 'New Moon':
                phase_no = 0
            elif(phase == 'Waxing Crescent'):
                if illumination <=2:
                    phase_no = 1
                elif illumination>2 and illumination<7:
                    phase_no = 2
                elif illumination>=7 and illumination<18:
                    phase_no = 3
                elif illumination>=18 and illumination<29:
                    phase_no = 4
                elif illumination>=29 and illumination<39:
                    phase_no = 5
                elif illumination>=39 and illumination<49:
                    phase_no = 6
                elif illumination>=49:
                    phase_no = 7
            elif phase == 'First Quarter':
                if illumination>=50 and illumination<=55:
                    phase_no = 8
                else:
                    phase_no = 9
            elif(phase == 'Waxing Gibbous'):
                if illumination <=70:
                    phase_no = 10
                elif illumination>70 and illumination<=80:
                    phase_no = 11
                elif illumination>80 and illumination<=89:
                    phase_no = 12
                elif illumination>89 and illumination<=95:
                    phase_no = 13
                elif illumination>95 and illumination<=98:
                    phase_no = 14
                elif illumination>98 and illumination<=99:
                    phase_no = 15
            elif phase=='Full Moon':
                if illumination==100:
                    phase_no = 16
                else:
                    phase_no = 17           
            elif(phase == 'Waning Gibbous'):
                if illumination >96:
                    phase_no = 18
                elif illumination<98 and illumination>=93:
                    phase_no = 19
                elif illumination<93 and illumination>=86:
                    phase_no = 20
                elif illumination<86 and illumination>=77:
                    phase_no = 21
                elif illumination<77 and illumination>=67:
                    phase_no = 22
                elif illumination<67 and illumination>=50:
                    phase_no = 23    
            elif phase== '3rd Quarter':
                if illumination>50:
                    phase_no = 24
                else:
                    phase_no = 25
            elif(phase == 'Waning Crescent'):
                if illumination>=37:
                    phase_no = 26
                elif illumination<37 and illumination>=29:
                    phase_no = 27
                elif illumination<29 and illumination>=20:
                    phase_no = 28
                elif illumination<20 and illumination>=13:
                    phase_no = 29
                elif illumination<13 and illumination>=7:
                    phase_no = 30 
                elif illumination<7 and illumination>=1:
                    phase_no = 31
    elif num_of_days == 28 or num_of_days==29:
            if phase == 'Dark Moon':
                phase_no = 0
            elif phase == 'New Moon':
                phase_no = 0
            elif(phase == 'Waxing Crescent'):
                if illumination <=2:
                    phase_no = 1
                elif illumination>2 and illumination<7:
                    phase_no = 2
                elif illumination>=7 and illumination<18:
                    phase_no = 3
                elif illumination>=18 and illumination<29:
                    phase_no = 4
                elif illumination>=29 and illumination<39:
                    phase_no = 5
                elif illumination>=39 and illumination<49:
                    phase_no = 6
                elif illumination>=49:
                    phase_no = 7
            elif phase=='First Quarter':
                if illumination>=50 and illumination<=55:
                    phase_no = 8
                else:
                    phase_no = 9
            elif(phase == 'Waxing Gibbous'):
                if illumination <=70:
                    phase_no = 10
                elif illumination>70 and illumination<=80:
                    phase_no = 11
                elif illumination>80 and illumination<=89:
                    phase_no = 12
                elif illumination>89 and illumination<=95:
                    phase_no = 13
                elif illumination>95 and illumination<=98:
                    phase_no = 14
                elif illumination>98 and illumination<=99:
                    phase_no = 15
            elif phase=='Full Moon':
                if illumination==100:
                    phase_no = 16
                else:
                    phase_no = 17           
            elif(phase == 'Waning Gibbous'):
                if illumination >96:
                    phase_no = 18
                elif illumination<98 and illumination>=93:
                    phase_no = 19
                elif illumination<93 and illumination>=86:
                    phase_no = 20
                elif illumination<86 and illumination>=77:
                    phase_no = 21
                elif illumination<77 and illumination>=67:
                    phase_no = 22
                elif illumination<67 and illumination>=50:
                    phase_no = 23    
            elif phase== '3rd Quarter':
                if illumination>50:
                    phase_no = 24
                else:
                    phase_no = 25
            elif(phase == 'Waning Crescent'):
                if illumination>=37:
                    phase_no = 26
                elif illumination<37 and illumination>=29:
                    phase_no = 27
                elif illumination<29 and illumination>=20:
                    phase_no = 28
                elif illumination<20 and illumination>=13:
                    phase_no = 29
                elif illumination<13 and illumination>=7:
                    phase_no = 30 
                elif illumination<7 and illumination>=1:
                    phase_no = 31
    return phase_no

def numberOfDays(y, m):
      y = int(y)
      m = int(m)
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30

# a = getPhaseno(31,'Waxing Gibbous', 99)
# print(a)
