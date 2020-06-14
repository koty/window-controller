from data_sender import send
from thermo import getData

def exec():
  data = getData()
  result = send(data)
  # 結果に応じて窓を開け締めする

if __name__ == '__main__':
    exec()
