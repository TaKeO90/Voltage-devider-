

import time 
import sys

print '''----------------------------------------------'''


print 'Welcome '
time.sleep(1)
print "Voltage divider"
time.sleep(1)
print "vcc's value is between 0 and 24"
time.sleep(1)
print "R1's value is between 0 and 1 million"
time.sleep(1) 
print "R2's value is between 0 and 1 million"
time.sleep(1)
 
print """-----------------------------------------------"""

    
vcc = raw_input("Enter VCC:  ")
for i in range(1) :
    if float (vcc)> 24 :
        print 'TRY AGAIN'
        vcc = raw_input("Enter VCC:  ")
        if float (vcc)> 24 :
            sys.exit()
  
R1 = raw_input("Enter R1: ")
for i in range(1):
    if float(R1)> 1000000 :
        print 'TRY AGAIN'
        R1 = raw_input("Enter R1: ")
        if float(R1)> 1000000 :
            sys.exit
 

R2 = raw_input("Enter R2: ")
for i in range (1) :
    if float(R2)> 1000000 :
        print 'TRY AGAIN'
        R2 = raw_input("Enter R2: ")
        if float(R2)> 1000000 :
            sys.exit()




 


print """----------------------------------------------------"""
US = (float(R2)/(float(R2)+float(R1)))* float(vcc)
print 'US = ' , US 
   





     

  
 


    




    
        
     
         
    


 


    

    
    
