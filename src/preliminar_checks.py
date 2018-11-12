# Press CTRL + B to launch the Script from SublimeText
# Practice 1. Web Scraping from the website loteriasyapuestasdelestado.es

# Previous tasks.

import sys
import whois
import builtwith

# python version?
print(sys.version) # 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)]

# python modules installed?

help('modules')

# who is the owner of the damain?
print(whois.whois('loteriasyapuestas.com')) # Registar: Entorno Digital, S.A., org: SOCIEDAD ESTATAL LOTERIAS Y APUESTAS DEL ESTADO

# which is the technology of the page
print(builtwith.builtwith('https://www.loteriasyapuestas.es/es/la-primitiva')) # javascript, jquery
