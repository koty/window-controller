import binascii
from bluepy.btle import Scanner, DefaultDelegate
from environment import get_values


class ScanDelegate( DefaultDelegate ):
  def __init__( self ):
    DefaultDelegate.__init__( self )
    envs = get_values()
    self.macaddr = envs['THERMO_METER_MAC_ADDRESS']
  macaddr = ''
  temperature = 0
  humidity = 0
  battery = 0
  def handleDiscovery( self, dev, isNewDev, isNewData ):
    if dev.addr == self.macaddr:
      for ( adtype, desc, value ) in dev.getScanData():
        if ( adtype == 22 ):
          servicedata = binascii.unhexlify( value[4:] )

          battery = servicedata[2] & 0b01111111
          isTemperatureAboveFreezing = servicedata[4] & 0b10000000
          temperature = ( servicedata[3] & 0b00001111 ) / 10 + ( servicedata[4] & 0b01111111 )
          if not isTemperatureAboveFreezing:
            temperature = -temperature
          humidity = servicedata[5] & 0b01111111

          isEncrypted            = ( servicedata[0] & 0b10000000 ) >> 7
          isDualStateMode        = ( servicedata[1] & 0b10000000 ) >> 7
          isStatusOff            = ( servicedata[1] & 0b01000000 ) >> 6
          isTemperatureHighAlert = ( servicedata[3] & 0b10000000 ) >> 7
          isTemperatureLowAlert  = ( servicedata[3] & 0b01000000 ) >> 6
          isHumidityHighAlert    = ( servicedata[3] & 0b00100000 ) >> 5
          isHumidityLowAlert     = ( servicedata[3] & 0b00010000 ) >> 4
          isTemperatureUnitF     = ( servicedata[5] & 0b10000000 ) >> 7

          self.temperature = temperature
          self.humidity = humidity
          self.battery = battery
"""
          print( '----' )
          print( 'battery: '     + str( battery ) )
          print( 'temperature: ' + str( temperature ) )
          print( 'humidity: '    + str( humidity ) )
          print( '' )
          print( 'isEncrypted: '            + str( bool( isEncrypted ) ) )
          print( 'isDualStateMode: '        + str( bool( isDualStateMode ) ) )
          print( 'isStatusOff: '            + str( bool( isStatusOff ) ) )
          print( 'isTemperatureHighAlert: ' + str( bool( isTemperatureHighAlert ) ) )
          print( 'isTemperatureLowAlert: '  + str( bool( isTemperatureLowAlert ) ) )
          print( 'isHumidityHighAlert: '    + str( bool( isHumidityHighAlert ) ) )
          print( 'isHumidityLowAlert: '     + str( bool( isHumidityLowAlert ) ) )
          print( 'isTemperatureUnitF: '     + str( bool( isTemperatureUnitF ) ) )
          print( '----' )
"""

def getData():
    scanner = Scanner().withDelegate( ScanDelegate() )
    scanner.scan( timeout=5 )
    return { 'temperature': scanner.delegate.temperature, 'humidity': scanner.delegate.humidity, 'battery': scanner.delegate.battery }

if __name__ == '__main__':
    data = getData()
    print(f'{data["temperature"]},{data["humidity"]}')
