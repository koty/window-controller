from data_sender import send
from thermo import getData
from window_opener import open_or_close_window

def entry_point():
  # 気温取得
  data = getData()

  # SpreadSheetに送信
  result_json = send(data)

  # 結果に応じて窓を開け締めする
  open_or_close_window(result_json['rows'])

if __name__ == '__main__':
    entry_point()
