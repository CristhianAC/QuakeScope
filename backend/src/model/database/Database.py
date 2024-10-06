import pymysql
import pandas as pd

class Database:

  def __init__ (self):
    self.timeout = 10
    self.data_dir = r"QuakeScope/backend/src/model/database/data"
    self.mars_data = f"{self.data_dir}/mars"
    self.lunar_data = f"{self.data_dir}/lunar"

  def connect (self):
    self.connection = pymysql.connect(
      charset="utf8mb4",
      connect_timeout=self.timeout,
      cursorclass=pymysql.cursors.DictCursor,
      db="defaultdb",
      host="quakescope-sebastianmaldonado1945-eca1.h.aivencloud.com",
      password="AVNS_iznx7nwkwnaHqv7lPs7",
      read_timeout=self.timeout,
      port=28016,
      user="avnadmin",
      write_timeout=self.timeout,
    )

  def generateTable (self):
      try:
        cursor = self.connection.cursor()
        cursor.execute(
          '''CREATE TABLE mytest (
          id INTEGER PRIMARY KEY,
          body VARCHAR(50),
          purpous VARCHAR(50),
          folder VARCHAR(50),
          date VARCHAR(255),
          time DECIMAL(18, 15)
          velocity ()
          )'''
          )
        print(cursor.fetchall())
      except:
        print("ERROR en la creación de la Tabla")
      finally:
        self.connection.close()

    def loadData (self):
      data = pd.read_csv(f"{self.mars_dir}/test/data/XB.ELYSE.02.BHV.2019-05-23HR02_evid0041.csv")
      print(data)

db = Database()
db.connect()
db.loadData()

