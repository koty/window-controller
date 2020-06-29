import configparser
from environment import get_values
import subprocess


"""
row ゼロ番目：温度、1番目湿度
"""
def open_or_close_window(rows):
  arr = [r[0] for r in rows]
  avg = _avg[arr]
  if avg >= 27:
    open_window()
  elif avg <= 25:
    close_window()
  else:
    pass

def _avg(arr):
  s = sum(arr)
  n = len(arr)
  return s/n

def open_window():
  # 既に開いていたら何もしない
  cmd_window('open')

def close_window():
  # 既に閉じていたら何もしない
  cmd_window('close')

def pause_window():
  cmd_window('pause')

def cmd_window(cmd):
  envs = get_values()
  args = ['tuya-cli', 'set', '--dps', '102', '--set', cmd, '--id', envs["TUYA_ID"], '--key', envs["TUYA_KEY"]]
  print(f'cmd: {cmd}')
  completed_process = subprocess.run(args, timeout=60, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  print(f'stdout: {completed_process.stdout}, stderr: {completed_process.stderr}', flush=True)

"""
{ devId: 'xxxx',
  dps:   {
      '6': false, <— アラームロック
      '101': 0, <- 1以上全開 0全閉
      '102': 'pause’, <-現在の状態。指定も可。open/close/pause
      '103': false, <- ロック（たぶん）
      '104': '6’, <- 動作速度（たぶん）
      '105': '7’, <- Anti clamp strength
      '106': 'left’, <- 窓を開く方向
      '107': 'cancel’, <-infared control
      '108': false, <- infered fortification
      '109': false <- Manual start（たぶん）
   }
}
"""

def get_window_state():
  config = configparser.ConfigParser()
  config.read('app_state.ini')
  return window_stateconfig['default']['window_state']
