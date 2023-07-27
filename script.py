print("Outil pour calculer la règle des 500 en photographie pour les appareils à capteurs APS-C (x1.6 chez Canon, x1.5 chez Nikon) ou micro 4/3 (x2).")
print("Pour un capteur full-frame 24x36 ; facteur de conversion = x1.")

version = "0.0.3"

focal = float(input("longueur focale : "))
convert = float(input("facteur de conversion : "))

time = int((500/(focal*convert))) #pr calculer grâçe à la règle des 500

print(str(time) + " secondes")

'#affichage en fin de programme'
print(".")
print("v" + str(version) + " du programmme")
#créé par Clémz