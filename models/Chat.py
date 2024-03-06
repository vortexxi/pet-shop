from models.Animal import Animal

class Chat (Animal):
  
  def __init__(self, nom, poids, taille, sexe, date_naissance, poils_long, caractere):
    super().__init__(nom, poids, taille, sexe, date_naissance, 0.5)
    self.__poils_long = poils_long
    self.__caractere = caractere
    self.__taille_griffe = 0
    self.__taille_griffe_max = 3
  
  @property
  def poils_long(self):
    return self.__poils_long
  
  @property
  def caractere(self):
    return self.__caractere
  
  @property
  def taille_griffe(self):
    return self.__taille_griffe

  @property
  def age_humain(self):
      return self.age * 5

  @property
  def griffes_longues(self):
    return self.__taille_griffe >= self.__taille_griffe_max

  # Méthodes

  def crier(self):
      return f"{self.nom} miaule"

  def couper_griffes(self):
    self.__taille_griffe = 0

  def passer_nuit(self):
    super().passer_nuit();
    self.__taille_griffe += 1