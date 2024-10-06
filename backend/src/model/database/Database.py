import pymysql, os
import pandas as pd
import json

class Database:

  def __init__ (self):
    self.timeout = 10
    self.data_dir = f"{os.path.dirname(os.path.dirname(__file__))}/database/data"
    self.mars_data = f"{self.data_dir}/mars"
    self.lunar_data = f"{self.data_dir}/lunar"

    self.MARS = "MARS"
    self.MOON = "MOON"
    self.TEST = "TEST"
    self.TRAIN = "TRAIN"

  def loadMarsData (self):
    print("Cargando datos de Testeo de Marte")
    return self.loadData(self.MARS, f"{self.mars_data}/test/data")

    print("Cargando datos de Entrenamiento de Marte")

  def loadMoonData (self):
    print("Cargando datos de Testeo de la Luna")
    folder_list = os.listdir(f"{self.lunar_data}/test/data")
    
    for folder in folder_list[-1:]:
      self.loadData(self.MOON, f"{self.lunar_data}/test/data/{folder}")

    print("Cargando datos de Entrenamiento de la Luna")

  def loadData (self, body: str, data_folder):
    data_files = [file for file in os.listdir(data_folder) if file.split(".")[-1] == 'csv']
    folder_name = data_folder.split("/")[-1]
    print(folder_name)
    output_folder = f'{self.data_dir}/data-jsons/{folder_name}/'
    os.makedirs(output_folder, exist_ok=True)
    print(f"Carpeta de salida: {output_folder}")
    print(f"Existe: {os.path.exists(output_folder)}")

    for j, file in enumerate(data_files):
      
      df = pd.read_csv(f"{data_folder}/{file}")
    
    
      data =  []
      for i in df.index:
        data.append({'time': df.at[i, 'rel_time(sec)'],
                    'vel': df.at[i, 'velocity(c/s)']})
        
      json_file_path = os.path.join(output_folder, f'data-{body}-{j}.json')
      with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

db = Database()
db.loadMarsData()

# db.loadMoonData()