from models.user import User
from models.motor import Motor
# Create a list of 5 user objects
users = [
    User("alice", "alice@example.com", "alice123"),
    User("bob", "bob@example.com", "bob456"),
    User("charlie", "charlie@example.com", "charlie789"),
    User("dave", "dave@example.com", "dave1011"),
    User("eve", "eve@example.com", "eve1213")
]
motors = [
    Motor(
        id="1",
        name="Yamaha R1",
        img="SPCK/app/assets/xe1.jpg",
        publish_year=2020,
        motor_type="Sport",
    ),
    Motor(
        id="2",
        name="Honda CBR500R",
        img="SPCK/app/assets/xe2.jpg",
        publish_year=2021,
        motor_type="Sport",
    ),
    Motor(
        id="3",
        name="Kawasaki Ninja 400",
        img="SPCK/app/assets/xe3.jpg",
        publish_year=2019,
        motor_type="Sport",
    ),
    Motor(
        id="4",
        name="Harley-Davidson Street 750",
        img="SPCK/app/assets/xe4.jpg",
        publish_year=2018,
        motor_type="Cruiser",
    ),
    Motor(
        id="5",
        name="Ducati Monster 821",
        img="SPCK/app/assets/xe5.jpg",
        publish_year=2022,
        motor_type="Naked",
    ),
]