import phonenumbers
from phonenumbers import geocoder,carrier,timezone
from phonenumbers.phonenumberutil import number_type

#number = "+522381043760"
number=input("Ingresa un numero de telefono con lada")
ch_nmber=phonenumbers.parse(number,"CH")

#pais del telefono
print("Pais",geocoder.description_for_number(ch_nmber,"en"))#pais en ingles

#compañia del telefono
print("Compañia",carrier.name_for_number(ch_nmber,"en"))#compañia

#horario
print("Horario",timezone.time_zone_for_number(ch_nmber))#horario

