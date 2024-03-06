class AnimalerieError(Exception):
  def __init__(self, message) -> None:
      self.__message = message

  @property
  def message(self):
    return self.__message