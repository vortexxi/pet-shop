class Adresse:

  # Constructeur
  def __init__(self, rue, numero, ville, code_postal) -> None:
    self.__rue = rue
    self.__numero = numero
    self.__ville = ville
    self.__code_postal = code_postal

  # Accesseurs & Mutateurs

  @property
  def rue(self):
    return self.__rue

  @property
  def numero(self):
    return self.__numero

  @property
  def ville(self):
    return self.__ville

  @property
  def code_postal(self):
    return self.__code_postal

  @rue.setter
  def rue(self, value):
    self.__rue = value

  @numero.setter
  def numero(self, value):
    self.__numero = value

  @code_postal.setter
  def code_postal(self, value):
    self.__code_postal = value

  @ville.setter
  def ville(self, value):
    self.__ville = value


  # Méthodes
  def format(self):
    return f"{self.__rue} {self.__numero}, {self.__code_postal} {self.__ville}"
  
