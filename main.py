
a=int(input("unesi kordinatu="))
b=int(input("unesi kordinatu="))
if a<0 and b<0:
  print("prvi kvadrant")
elif a<0 and b>0:
  print("drugi kvadrant")
elif a>0 and b>0:
  print("treci kvadrant")
elif a>0 and b<0:
  print("cetvrti kvadrant")
else:
  print("nista tocno")