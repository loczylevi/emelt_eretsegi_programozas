   #0 20190326-0700 4170861 NYB 20190404
# megallo sorszam,
#a felszállás dátuma és időpontja,
#a kártya egyedi azonosítója,
#a jegy vagy bérlet típusa,
#a bérlet érvényességi ideje,
#________________________________________________________



#0 20190326-0700 4170861 NYB 20190404

class Bus:
  def __init__(self,sor):
    hely, datum, kartya, tipus, medig = sor.strip().split(" ")
    self.hely = hely
    self.datum = datum
    self.kartya = kartya
    self.tipus = tipus 
    self.medig = int(medig)
    self.datum_nap = int(datum[0:8])
    self.datum_ora = str(datum[9:14])

"""
Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
	h1 = (h1 + 9) % 12
	e1 = e1 - h1 / 10
	d1= 365*e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1*306 + 5) / 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 / 10
	d2= 365*e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2*306 + 5) / 10 + n2 - 1
	napokszama:= d2-d1
Függvény vége

"""
  

# 2019.01.01 ; 2019.01.25
def napokszama(datum1,datum2):

  e1 = int(datum1[0:4])
  
  e2 = int(datum2[0:4])
  
  h1 = int(datum1[4:6])
  
  h2 = int(datum2[4:6])
  
  n1 = int(datum1[6:8])
  
  n2 = int(datum2[6:8])
  
  
  h1 = (h1 + 9) % 12
  e1 = e1 - h1 / 10
  d1= 365*e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1*306 + 5) / 10 + n1 - 1
  h2 = (h2 + 9) % 12
  e2 = e2 - h2 / 10
  d2= 365*e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2*306 + 5) / 10 + n2 - 1
  napokszama = d2-d1
  
  return napokszama
  
  

datum1 = "20190110"
datum2 = "20190125"
print(napokszama(datum1,datum2))
  
  
with open("utasadat.txt","r",encoding="utf-8") as f:
  lista = [Bus(sor) for sor in f]

#2

print(f"""2. feladat
A buszra {len(lista)} utas akart felszállni.""")

#felszalas = len([sor for sor in lista if sor.datum_nap > sor.medig and sor.medig == 0])
#3
darab = 0


for sor in lista:
  if sor.datum_nap > sor.medig and sor.tipus != "JGY":
    darab += 1
  elif sor.tipus == "JGY" and sor.medig == 0:
    darab += 1
    
print(f"""3. feladat
A buszra {darab} utas nem szálhatott fel.""")

stat = dict()

for sor in lista:
  hely = sor.hely
  stat[hely] = stat.get(hely,0) + 1

hely1 = 0
darab1 = 0

for hely,darab in stat.items():
  #print(f"{hely} - {darab} -orszag ")
  if darab > darab1:
    darab1 = darab
    hely1 = hely


print(f"""4. feladat
A legtöbb utas ({darab1} fő) a {hely1}. megállóban próbált felszállni.""")

#5


darab_kedvezmeny = 0
darab_ingyes = 0

for sor in lista: # érvényes
  if sor.tipus in {"TAB","NYB"} and sor.datum_nap <= sor.medig: 
    darab_kedvezmeny += 1
  if sor.tipus in {"NYP","RVS","GYK"} and sor.datum_nap <= sor.medig:
    darab_ingyes += 1



kedvezmenyes_tab = len([sor for sor in lista if sor.datum_nap <= sor.medig and sor.tipus == "TAB"])

kedvezmenyes_nyb = len([sor for sor in lista if sor.datum_nap <= sor.medig and sor.tipus == "NYB"])

ingyenes = len([sor for sor in lista if sor.datum_nap <= sor.medig and sor.tipus in {"NYP","RVS","GYK"}])


c = kedvezmenyes_tab + kedvezmenyes_nyb

print(f"""5. feladat
Ingyenesen utazók száma: {ingyenes} fő 
Kedvezményesen utazók száma: {c} fő""")

#7


for sor in lista:
  if sor.tipus != "JGY":
    datum1 = str(sor.datum_nap)
    datum2 = str(sor.medig)
    if napokszama(datum1,datum2) == 3:
      with open("figyelmeztetes.txt","w","utf-8") as f2:
        
        f2.write(str(sor.kartya),str(sor.medig))
        #print(sor.kartya,sor.medig)

