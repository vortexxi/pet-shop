from models.Animal import Animal

class Chien (Animal):
  
  def __init__(self, nom, poids, taille, sexe, date_naissance, couleur_collier, est_dresse, race):
    super().__init__(nom, poids, taille, sexe, date_naissance, 1)
    self.__couleur_collier = couleur_collier
    self.__est_dresse = est_dresse
    self.__race = race
  
  @property
  def couleur_collier(self):
    return self.__couleur_collier
  
  @property
  def est_dresse(self):
    return self.__est_dresse
  
  @property
  def race(self):
    return self.__race

  @property
  def age_humain(self):
      return self.age * 7

  # Méthodes

  def crier(self):
      return f"{self.nom} aboie"
