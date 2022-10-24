from logging.handlers import WatchedFileHandler
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
invoer = open("3600_S8_S4_fleximflow.txt")
for i in range(2):
    invoer.readline()
lijn = invoer.readline()
for i in range(4):
    invoer.readline()

eenheden = lijn.split(";")
print(eenheden)
if "barke" in eenheden:
    P = eenheden.index("barke")
    print(P)
    print(eenheden[P])
tel = 0

x = []
y = []
z = []
Qin = 1000000

for lijn in invoer:
    waarden = lijn.split(";")

    temp = waarden[1]
    temperatuur = float(temp.replace(",", "."))
    temperatuur += 273.15

    temp = waarden[2]
    druk = float(temp.replace(",", "."))

    temp = waarden[3]
    flow = float(temp.replace(",", "."))
    tel +=1
    
    #print(temperatuur,druk)
    fluid = 'water'
    h = CP.PropsSI("H",'P',druk,"T",temperatuur,fluid)

    d = CP.PropsSI("D",'P',druk,"T",temperatuur,fluid)
    #print(h,d)

    Qout = h * d * flow/3600 
    #print(Qout)

    efficientie = Qout/Qin

  #x.append(temp)
    x.append(tel)
    y.append(Qout)
    z.append(efficientie)

plt.plot(x, z, label="Q")
# naming the x axis
plt.xlabel('Tijd(uur)')
# naming the y axis
plt.ylabel('Q')
# giving a title to my graph
plt.title('Uitgaande warmte HEX1')
  
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()




