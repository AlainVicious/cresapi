class ErrorResponse:
  '''
  Objeto para regresar errores
  '''
  def __init__(self, msg, ercode):
    self.message = msg
    self.ercode = ercode