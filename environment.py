import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GOOGOLE_SHEET_URL = os.environ.get("GOOGOLE_SHEET_URL")
THERMO_METER_MAC_ADDRESS = os.environ.get("THERMO_METER_MAC_ADDRESS")
TUYA_ID = os.environ.get("TUYA_ID")
TUYA_KEY = os.environ.get("TUYA_KEY")

def get_values():
  return {
    'GOOGOLE_SHEET_URL': GOOGOLE_SHEET_URL,
    'THERMO_METER_MAC_ADDRESS': THERMO_METER_MAC_ADDRESS,
    'TUYA_ID': TUYA_ID,
    'TUYA_KEY': TUYA_KEY,
  }
  