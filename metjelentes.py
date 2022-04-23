#http://informatika.fazekas.hu/wp-content/uploads/2015/10/Meteorol%C3%B3giai-jelent%C3%A9s.pdf

"""
BP 0000 VRB02 23
DC 0015 15005 23
SM 0015 01013 21
PA 0015 34016 20
SN 0015 17004 24
PR 0015 31018 21
BP 0030 VRB02 22
SN 0045 19006 24
PA 0045 34016 20
"""
class Ido_jaras:
  def __init__(self,sor):
    telepules,ido,szel_irany,homerseklet = sor.strip().split(" ")
    self.telepules = telepules
    self.ido = ido
    self.szel_irany = szel_irany
    self.homerseklet = int(homerseklet)
    self.erőség = szel_irany[3:]

with open("tavirathu13.txt","r",encoding="UTF-8") as f:
  lista = [Ido_jaras(sor) for sor in f]

#2
print("2. feladat")
bekeres = input("Adja meg egy település kódját! Település: ")

utolso_meres = max([sor.ido for sor in lista if bekeres == sor.telepules])

print(f"Az utolsó mérési adat a megadott településről {utolso_meres[0:2]}:{utolso_meres[2:]}-kor érkezett.")
#---------------------------------------------
#3
#nagy_________________________________
telepules_neve = ""
ido_pont = ""
nagy = 0

for sor in lista:
  if sor.homerseklet > nagy:
    nagy = sor.homerseklet
    telepules_neve = sor.telepules 
    ido_pont = sor.ido

#kicsi__________________________
homik = [sor.homerseklet for sor in lista]
kicsi = homik[0]
telepules_neve2 = ""
ido_pont2 = ""

for sor in lista:
  if sor.homerseklet < kicsi:
    kicsi = sor.homerseklet
    telepules_neve2 = sor.telepules 
    ido_pont2 = sor.ido

print(f"""3. feladat
A legalacsonyabb hőmérséklet: {telepules_neve2} {ido_pont2[0:2]}:{ido_pont2[2:]} {kicsi} fok.
A legmagasabb hőmérséklet: {telepules_neve} {ido_pont[0:2]}:{ido_pont[2:]} {nagy} fok.""")


#4_________________________________

szelcsend = [sor for sor in lista if sor.szel_irany == "00000"]

print("4. feladat")
if len(szelcsend) > 0:
  [print(f"{sor.telepules} {sor.ido[0:2]}:{sor.ido[2:]}") for sor in szelcsend]

else:
  print("Nem volt szélcsend a mérések idején.")

#5_________________________________

#kozep = [(sor.homerseklet,sor.ido) for sor in lista if sor.ido == "0100" and sor.ido == "0700" and sor.ido == "1300" and sor.ido == "1900"]
  
bp_kozep = []

for sor in lista:
  if sor.ido == "0100" and sor.telepules == "BP":
    bp_kozep.append(sor.homerseklet)
  if sor.ido == "0700" and sor.telepules == "BP":
    bp_kozep.append(sor.homerseklet)
  if sor.ido == "1300" and sor.telepules == "BP":
    bp_kozep.append(sor.homerseklet)
  if sor.ido == "1900" and sor.telepules == "BP":
    bp_kozep.append(sor.homerseklet)


osz = sum(bp_kozep)
atlag = osz / len(bp_kozep)
kerek = round(atlag)

ingadozas = max(bp_kozep) - min(bp_kozep)
print(ingadozas)
print(bp_kozep)
