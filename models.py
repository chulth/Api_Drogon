#aqui vamos a modelar nuestra aplicacion

import uuid

class Conexion_api:
    def __init__(self, id_api, pass_api, uid= None):
        super().__init__()
        self.id_api = id_api
        self.pass_api= pass_api
        self.uid = uid or uuid.uuid4()

    
    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema_of_connection():
        return['id_api', 'pass_api', 'uid']
        

