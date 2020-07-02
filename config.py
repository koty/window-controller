from configparser import ConfigParser

def _read_config():
  config_parser = ConfigParser()
  config_parser.read(APP_STATE_FILE_NAME)
  return config_parser

def get_window_state():
  config_parser = _read_config()
  return config_parser['default']['window_state']

APP_STATE_FILE_NAME = 'app_state.ini'

def save_window_state(state):
  config_parser = _read_config()
  config_parser['default']['window_state'] = state
  with open(APP_STATE_FILE_NAME, 'w') as file:
    config_parser.write(file)

def get_th_to_be_closed():
  config_parser = _read_config()
  return int(config_parser['default']['th_to_be_closed'])

def get_th_to_be_opened():
  config_parser = _read_config()
  return int(config_parser['default']['th_to_be_opened'])
