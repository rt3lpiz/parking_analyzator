__author__ = 'rt3lpiz'
#!/usr/bin/python


import twitter

api=twitter.Api(consumer_key='oCFVGKU1YQY4JfZsawOFo24lU',
                consumer_secret='upgH5TlR16z1biy5htZDdK2jMkBiPyOF163MzH13Vm9PAd3ML0',
                access_token_key='149062105-TwiixYWhPj5gOCFQsjaW55T5EaYVkwOQ950rENH8',
                access_token_secret='ObkxP5m4XE0PlYhgEUoJ24n2ML14jWiGXO8Qk4dgklJvG')

status=api.GetStatus()
print status