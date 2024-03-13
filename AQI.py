city=input("What city do you live in ")
air=int(input("What is the AQI in your city :"))
if air >=5:
  print("good, you can go outside")
elif air>=1:
  print("You can go outside")
elif air >=51:
  print("Satisfactory, nothing bad will happen")
elif air>=101:
  print("Wear a mask AQI is moderate")
elif air>=201:
  print("Turn on the air purifier AQI is Poor")
elif air>=301:
  print("Stay indoors AQI is very poor")
elif air>=401:
  print("STAY INDOORS AQI IS SEVERE")
