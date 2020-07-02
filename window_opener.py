from config import get_window_state, save_window_state, get_th_to_be_closed, get_th_to_be_opened
from environment import get_values
import subprocess
from datetime import datetime as dt

"""
row ゼロ番目：温度、1番目湿度
"""
def open_or_close_window(rows):
  cmd = _get_cmd(rows)
  if cmd == 'open':
    open_window()
  elif cmd == 'close':
    close_window()
  else:
    pass

def _get_cmd(rows):
  arr = [r[0] for r in rows]
  avg = _avg[arr]
  to_be_opend = get_th_to_be_opened()
  to_be_closed = get_th_to_be_closed()
  if avg >= to_be_opend:
    return 'open'
  elif avg <= to_be_closed:
    return 'close'
  else:
    return None

def _avg(arr):
  s = sum(arr)
  n = len(arr)
  return s/n

def open_window(dry_run=False):
  # 既に開いていたら何もしない
  if get_window_state() == 'open':
    return
  cmd_window(cmd='open', dry_run=dry_run)

def close_window(dry_run=False):
  # 既に閉じていたら何もしない
  if get_window_state() == 'close':
    return
  cmd_window(cmd='close', dry_run=dry_run)

def pause_window(dry_run=False):
  cmd_window(cmd='pause', dry_run=dry_run)

def cmd_window(cmd, dry_run=False):
  envs = get_values()
  args = ['tuya-cli', 'set', '--dps', '102', '--set', cmd, '--id', envs["TUYA_ID"], '--key', envs["TUYA_KEY"]]
  print(f'cmd: {cmd}')
  print(f"args: {' '.join(args)}")
  if not dry_run:
    completed_process = subprocess.run(args, timeout=60, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'stdout: {completed_process.stdout}, stderr: {completed_process.stderr}', flush=True)
  if cmd == 'pause':
    return
  save_window_state(state=cmd)

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
