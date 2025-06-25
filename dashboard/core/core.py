import phonenumbers
from phonenumbers import timezone , geocoder , carrier

def fetch_data(phoneNo):
	phno = phonenumbers.parse(phoneNo)
	timeZone = timezone.time_zones_for_number(phno)
	Carrier = carrier.name_for_number(phno,'en')
	Region = geocoder.description_for_number(phno,'en')
	valid = phonenumbers.is_valid_number(phno)
	possible = phonenumbers.is_possible_number(phno)

	return {
		'Core':phoneNo,
		'Phno':phno,
		'Timezone':timeZone[0],
		'Carrier':Carrier,
		'Region':Region,
		'Valid':valid,
		'Possible':possible,
	}

