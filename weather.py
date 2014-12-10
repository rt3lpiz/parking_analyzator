__author__ = 'rt3lpiz'

import pywapi



iargara=pywapi.get_weather_from_weather_com('MDXX0983','imperial')

for element in iargara:
    print element


temp_f=int(iargara['current_conditions']['temperature'])
temp_c=(float(temp_f-32)*float(5.0/9.0))
print iargara['current_conditions']['temperature'],'',iargara['units']['temperature'], temp_c,' C'
print iargara['location']['name'],' ',iargara['location']['lat'],' latitudine N', iargara['location']['lon'],' longitudine E'