import datetime

from exceptions.animalerie_exception import AnimalerieError

from models.Animalerie import Animalerie
from models.Chat import Chat
from models.Chien import Chien
from models.Oiseau import Oiseau

animalerie = Animalerie("Le pays des animaux", 20, "Jean Mermoz", 3, "Gosselies", 6044)

# Créer les animaux
chat1 = Chat("Ronron", 2, 45, "M", datetime.date(2019, 12, 12), False, "Calin")
chat2 = Chat("Ronronne", 3, 35, "F", datetime.date(2014, 5, 5), True, "Farouche")

chien1 = Chien("Robert", 20, 120, "M", datetime.date(2016, 2, 29), "Vert", False, "Labrador")

oiseau1 = Oiseau("Titi", 0.2, 5, "M", datetime.date(2021, 5, 6), "Jaune", False)

# Ajouter les animaux dans l'animalerie
try:
  animalerie.ajouter_animal(chat1)
  animalerie.ajouter_animal(chat2)
  animalerie.ajouter_animal(chien1)
  animalerie.ajouter_animal(oiseau1)
except AnimalerieError as e:
  print(e.message)

print(animalerie)

def demande_animal():
  
  choix = input("Choix de l'animal : (1. Chat, 2. Chien, 3. Oiseau :) ")

  nom = input("Nom : ")
  poids = input("Poids : ")
  taille = input("Taille : ")
  sexe = input("Sexe (M/F) : ")
  date_user = input("Date de naissance (YYYY-MM-DD) : ")
  date_naissance = datetime.date.fromisoformat(date_user)

  if choix == "1":
    # Chat
    caractere = input("Caractère :")
    type_poils = input('Poils long ? (True / False) :') == True

    animal = Chat(nom, poids, taille, sexe, date_naissance, type_poils, caractere)

  elif choix == "2":
    # Chien
    collier = input("Couleur collier : ")
    race = input('Race : ')
    dressage = input("Est dressé ? (True / False) :") == True

    animal = Chien(nom, poids, taille, sexe, date_naissance, collier, dressage, race)

  else:
    # Oiseau
    couleur = input("Couleur : ")
    voliere = input("En volière ? (True / False) : ") == True

    animal = Oiseau(nom, poids, taille, sexe, date_naissance, couleur, voliere)

  return animal
    

while (animalerie.nb_animaux > 0):

  # Demande nouveau arrivant
  nb = input("Nombre d'arrivants :")
  if nb.isdigit():
    nb = int(nb)

    while nb > 0:
      animal = demande_animal()
      animalerie.ajouter_animal(animal)
      nb -= 1

  animalerie.simuler_journee()