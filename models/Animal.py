from abc import ABC, abstractmethod
import datetime

import random

class Animal(ABC) :

  def __init__(self, nom, poids, taille, sexe, date_naissance, chance_deces):
    self.__nom = nom
    self.__poids = poids
    self.__taille = taille
    self.__sexe = sexe if sexe is not None else "X"
    self.__date_naissance = date_naissance
    self.__chance_deces = chance_deces
    self.__date_arrivee = datetime.date.today()
    self.__est_vivant = True
  
  # Accesseurs & Mutateurs

  #region Accesseurs
  @property
  def nom(self):
    return self.__nom
  
  @property
  def poids(self):
    return self.__poids
  
  @property
  def taille(self):
    return self.__taille
  
  @property
  def sexe(self):
    return self.__sexe
  
  @property
  def date_naissance(self):
    return self.__date_naissance
  
  @property
  def chance_deces(self):
    return self.__chance_deces
  
  @property
  def date_arrivee(self):
    return self.__date_arrivee
  
  @property
  def age(self):
    today = datetime.date.today()

    age = today.year - self.date_naissance.year
    if today.month < self.date_naissance.month \
      or (today.month == self.date_naissance.month \
        and today.day < self.date_naissance.day):
      age -= 1
    
    return age

  @property
  def est_vivant(self):
    return self.__est_vivant
  
  @property
  @abstractmethod
  def age_humain(self):
    pass
  
  #endregion

  #region Mutateurs
  @nom.setter
  def nom(self, value):
    self.__nom = value
  
  @poids.setter
  def poids(self, value):
    self.__poids = value
  
  @taille.setter
  def taille(self, value):
    self.__taille = value
  
  @sexe.setter
  def sexe(self, value):
    self.__sexe = value

  #endregion

  #region Méthodes

  @abstractmethod
  def crier(self):
    pass

  def __str__(self):
    return f"{self.nom} {self.sexe} {self.age} ans"

  def passer_nuit(self):
    chance_survie = random.random() * 100
    if chance_survie <= self.__chance_deces:
      print(f"{self.__nom} est mort.")
      self.__est_vivant = False
    else:
      print(f"{self.__nom} a bien dormi.")

  #endregion