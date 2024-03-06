from exceptions.animalerie_exception import AnimalerieError

from models.Adresse import Adresse
from models.Animal import Animal

from models.Chat import Chat
from models.Chien import Chien
from models.Oiseau import Oiseau

class Animalerie:

  def __init__(self, nom, capacite, rue, numero, ville, code_postal):
      self.__nom = nom
      self.__capacite = capacite
      self.__adresse = Adresse(rue, numero, ville, code_postal)
      self.__animaux = list()

  @property
  def nom(self):
    return self.__nom

  @nom.setter
  def nom(self, value):
    self.__nom = value

  @property
  def capacite(self):
    return self.__capacite

  @capacite.setter
  def capacite(self, value):
    if value > 0:
      self.__capacite = value
  
  @property
  def adresse(self):
    return self.__adresse

  @property
  def nb_chien(self):
    count = 0

    for animal in self.__animaux:
      if isinstance(animal, Chien):
        count += 1
    
    return count

  @property
  def nb_chat(self):
    count = 0

    for animal in self.__animaux:
      if isinstance(animal, Chat):
        count += 1
    
    return count

  @property
  def nb_oiseau(self):
    count = 0

    for animal in self.__animaux:
      if isinstance(animal, Oiseau):
        count += 1
    
    return count

  
  @property
  def nb_animaux(self):
    return len(self.__animaux)

  
  # Méthodes

  def ajouter_animal(self, animal):
    if not isinstance(animal, Animal):
      raise AnimalerieError("Ce n'est pas un animal.")

    # Vérifier la capacité de l'animalerie
    if  len(self.__animaux) == self.capacite:
      raise AnimalerieError("Capacité maximale atteinte.")
    
    if animal in self.__animaux:
      raise AnimalerieError("Animal déjà présent.")
    
    self.__animaux.append(animal)
  
  def __str__(self):
    desc = "Liste des animaux :\n"

    desc += f"Chat : ({self.nb_chat})\n"
    for animal in self.__animaux:
      if isinstance(animal, Chat):
        desc += f"\t - {animal} \n"

    desc += f"Chat : ({self.nb_chien})\n"
    for animal in self.__animaux:
      if isinstance(animal, Chien):
        desc += f"\t - {animal} \n"
    
    desc += f"Oiseau : ({self.nb_oiseau})\n"
    for animal in self.__animaux:
      if isinstance(animal, Oiseau):
        desc += f"\t - {animal} \n"
    
    return desc

  def simuler_journee(self):


    print("Évènement de la matinée :")

    self.verifier_vivant()    
    
    print(self)

    for animal in self.__animaux:

      if isinstance(animal, Chat) and animal.griffes_longues:
        animal.couper_griffes()
        print(f"Les griffes de {animal.nom} ont été coupées")
      
      animal.crier()

    print("Evenement de la nuit :")
    for animal in self.__animaux:
      animal.passer_nuit()

  def verifier_vivant(self):

    for animal in self.__animaux:

      if not animal.est_vivant:
        self.__animaux.remove(animal)