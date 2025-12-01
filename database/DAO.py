from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.object import Object


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def read_objects(): #quando nel metodo c'è il self devo per forza istanziare la classe sennò no
        #il codice per sta roba è sempre standard
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)
        query = "SELECT * FROM objects"
        cursor.execute(query)
        for row in cursor:
            result.append(Object(row["object_id"], row["title"]))
            #result.append(Object(**row)) # ** fa l'unpacking del risultato, se mettiamo degli _ davanti potrebbe creare problemi

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def readConnessioni(objects_dict):  # quando nel metodo c'è il self devo per forza istanziare la classe sennò no
        # il codice per sta roba è sempre standard
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT eo1.object_id as o1, eo2.object_id as o2, COUNT(*) as peso  
                   FROM exhibition_objects eo1 , exhibition_objects eo2 
                   WHERE eo1.exhibition_id  = eo2.exhibition_id  and eo1.object_id < eo2.object_id 
                   GROUP BY eo1.object_id , eo2.object_id"""
        cursor.execute(query)
        for row in cursor:
            o1 = objects_dict[row["o1"]]
            o2 = objects_dict[row["o2"]]
            peso = row["peso"]
            result.append(Connessione(o1,o2,peso)) #costruisce una connessione

        cursor.close()
        conn.close()
        return result