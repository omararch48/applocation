# Get vehicle METHOD GET
curl --request GET --location 'https://apilocation.omardanielesquivel.com/api/get_vehicle/1' \
--header 'username: omar' --header 'password: mesa.rojo_23' --header 'user-id: 1'


# Get all vechicles by user METHOD GET
curl --request GET --location 'https://apilocation.omardanielesquivel.com/api/get_all_vehicles/' \
--header 'username: omar' --header 'password: mesa.rojo_23' --header 'user-id: 1'


# Create vehicle METHOD POST
curl --request POST --location 'https://apilocation.omardanielesquivel.com/api/create_vehicle/' \
--data-urlencode 'username=omar' \
--data-urlencode 'password=mesa.rojo_23' \
--data-urlencode 'user_id=1' \
--data-urlencode 'user=1' \
--data-urlencode 'plates=QWE-789' \
--data-urlencode 'last_position={"lat": 0.000000, "lng": 0.000000}'


# Update vehicle METHOD PUT/PATCH
curl --request PUT --location 'https://apilocation.omardanielesquivel.com/api/update_vehicle/2/' \
--data-urlencode 'username=omar' \
--data-urlencode 'password=mesa.rojo_23' \
--data-urlencode 'user_id=1' \
--data-urlencode 'user=1' \
--data-urlencode 'plates=AAA-111' \
--data-urlencode 'last_position={"lat": 90.000001, "lng": 80.000002}'


# Delete vehicle METHOD DELETE
curl --request DELETE --location 'https://apilocation.omardanielesquivel.com/api/delete_vehicle/2/' \
--header 'username: omar' --header 'password: mesa.rojo_23' --header 'user-id: 1'