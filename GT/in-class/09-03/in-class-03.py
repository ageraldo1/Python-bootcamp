person =  {
    "name": "Alexandre Geraldo",
    "age": 40,
    "hobbies": ['Run', 'Workout', 'Play video game'],
    "wake_up": {
        "Sunday": "09:00 AM",
        "Monday": "07:00 AM",
        "Tuesday": "07:00 AM",
        "Wednesday": "07:00 AM",
        "Thrusday": "07:00 AM",
        "Friday": "07:00 AM",
        "Saturday": "07:00 AM"
    }
}


print (f"Name           : {person['name']}")
print (f"Hobbies        : {', '.join(person['hobbies'])}")
print (f"Monday wake up : {person['wake_up']['Monday']}")