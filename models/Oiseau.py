from models.Animal import Animal

class Oiseau (Animal):
  
  def __init__(self, nom, poids, taille, sexe, date_naissance, couleur, voliere):
    super().__init__(nom, poids, taille, sexe, date_naissance, 3)
    self.__couleur = couleur
    self.__voliere = voliere
  
  @property
  def couleur(self):
    return self.__couleur
  
  @property
  def voliere(self):
    return self.__voliere

  @property
  def age_humain(self):
      return self.age * 10

  # Méthodes

  def crier(self):
      return f"{self.nom} piaille"
