#etape 1
prenom = "carole"
nom= "ciemny"
age= 100
taille = 1,66
presentation = "je fais la formation pour devenir developpeur web./nje pourrai faire de beaux sites web!"
print(prenom)

#Etape 2
#EX1
mystery1 = 8 + 6
mystery2 = 8 - 6
print(mystery2)

#EX2
zebrasInZoo = 8
giraffesInZoo = 4

animalsInZoo= zebrasInZoo + giraffesInZoo
print(animalsInZoo)

#EX3
prixInitial = 1500
tva = 0.20

prix_final= prixInitial+(prixInitial*tva)
print(prix_final)

#EX4
#1

nb_oeufs_par_boite = 6
nb_oeufs_total = 145

nb_boites = nb_oeufs_total // nb_oeufs_par_boite
nb_oeufs_restants = nb_oeufs_total%nb_oeufs_par_boite

print(nb_boites)
print(nb_oeufs_restants)

#2
numero_carte_mystere = 28


#EX5
budget = 2000
budget_suffisant = (budget >= (prixInitial+(prixInitial*tva)))
print("le budget est suffisant: " + str(budget_suffisant))

#EX6

songs_a = 9
songs_b = 9
album_length_a = 41
album_length_b = 53

same_songs = (songs_a == songs_b)
same_album_length = (album_length_a == album_length_b)
print("il y a le même nombre de chansons : " + str(same_songs))
print("il y a la même longueur d'album: " + str (same_album_length))

#EX7

formateur = 'Jules'
langage = 'java'
version = 1.8

description = formateur + " est fan de " + langage + ", surtout depuis la version " + str(version)+ "!!"
print(description)

#ETAPE3
periode = "a definir"
heure = 35

if heure <0 or heure > 24:
    print ("c'est une erreur de saisie")

elif heure < 10:
    periode = "matinée"
    print ("bonne " + periode)

elif heure < 18:
    periode = "après-midi"
    print ("bonne " + periode)
else:
    periode = "soirée"
    print ("bonne " + periode)

#Etape4
#fonction calcul aire triangle
def  calcul_aire (base,hauteur):
    aire = base*hauteur/2
    return aire  
#fonction calcul aire triangle autre solution
# def  calcul_aire (base,hauteur):
#     return base*hauteur/2     

print (calcul_aire(3,4))
#affichage avec string interpolation
print(f'aire du triangle : {calcul_aire(3,4)}')

#fonction calcul volume sphere
import math
def  calcul_volume_sphere (rayon):
    return 4/3 * math.pi * (rayon**3)

# #fonction calcul volume sphere
# def  calcul_volume_sphere (rayon):
#     volume = 4/3 * 3.14* (rayon**3)
#     return volume      

print (calcul_volume_sphere(2)) 

#fonction calcul IMC
def  calcul_imc (prenom,poids,taille):
    taillecm = taille/100
    imc = poids/(taillecm **2)
    return imc  

#on met round pour arrondir
print (round (calcul_imc("test",52,155),1)) 





