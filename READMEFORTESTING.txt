
FOR NOW REGISTER DIRECTLY THROUGH API - /api/users/register

POST JSON DATA WITH NAME, EMAIL, PASSWORD FIELDS -> SUCH AS -

{

	"name" : "John Smith",
	"email" : "z@z.com",
	"password" : "z"

}



THEN CAN LOGIN THROUGH /login/    <- this is how registering will also be implemented in the future- basically a front end that makes the api call.

========================================================

restaurant pages 

/   -> home

/menu  -> menu items

/bookings -> to see bookings

========================================================


apis


/api/restaurant/bookings  -> use this to make bookings with following json data -

{

	"name": "John Doe",
	"no_of_guests": 4,
	"booking_date": "2024-03-21T18:30:00"

}




/api/restaurant/menu  -> use this to create new menu items with following json data -

{

	"title": "Cheeseburger", 
	"price": 8.99, 
	"inventory": 50

}