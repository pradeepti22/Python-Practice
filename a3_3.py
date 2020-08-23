try:
 score = input("Enter Score: ")
 score = float(score)
except:
 print('Value out of range, enter a valid value.')
 quit()
if score>1.0:
 print("Value out of range, enter a valid value.")
elif score<0.0:
 print ("Value out of range, enter a valid value.")
elif score>=0.9:
 print("A")
elif score>=0.8:
 print ("B")
elif score>=0.7:
 print ("C")
elif score>=0.6:
 print ("D")
elif score<0.6:
 print ("F")