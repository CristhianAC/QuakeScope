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
    events_df = pd.read_csv(f"{self.data_dir}/resultados_sismos_marte.csv")

    return self.loadData(self.MARS, f"{self.mars_data}/test/data")

    print("Cargando datos de Entrenamiento de Marte")

  def loadMoonData (self):
    print("Cargando datos de Testeo de la Luna")
    folder_list = os.listdir(f"{self.lunar_data}/test/data")

    events_df = pd.read_csv(f"{self.data_dir}/sismos_detectados.csv")
    print(events_df)
    
    for folder in folder_list:
      self.loadData(self.MOON, f"{self.lunar_data}/test/data/{folder}", events_df)

    print("Cargando datos de Entrenamiento de la Luna")

  def loadData (self, body: str, data_folder, events_df):
    data_files = [file for file in os.listdir(data_folder) if file.split(".")[-1] == 'csv']
    folder_name = data_folder.split("/")[-1]
    print(folder_name)
    output_folder = f'{self.data_dir}/data-jsons/{folder_name}/'
    os.makedirs(output_folder, exist_ok=True)
    print(f"Carpeta de salida: {output_folder}")
    print(f"Existe: {os.path.exists(output_folder)}")

    for j, file in enumerate(data_files):
      file_name = file[:-4]
      
      sismo_start = events_df[events_df['test_file']==file_name]['sismo_start'].values[0]
      sismo_end = events_df[events_df['test_file']==file_name]['sismo_end'].values[0]

      df = pd.read_csv(f"{data_folder}/{file}")
      
      time =  []
      velocity = []
      for i in df.index:
        time.append(df.at[i, 'time_rel(sec)'])
        velocity.append(df.at[i, 'velocity(m/s)'])

      data = {'sismo_start': sismo_start,
              'sismo_end': sismo_end,
              'time': time,
              'vel': velocity}
        
      json_file_path = os.path.join(output_folder, f'{file[:-4]}.json')
      with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
      
      print(file[:-4])
      print(f"Saved on {json_file_path}")

db = Database()
# db.loadMoonData()
db.loadMarsData()

# db.loadMoonData()