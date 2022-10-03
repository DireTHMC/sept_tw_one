"""#pip install vininfo"""

from vininfo import Vin

vin = Vin("WAUZZZ8K6CA041199")
print(vin.annotate())
code = vin.country_code
valid = vin.verify_checksum()
