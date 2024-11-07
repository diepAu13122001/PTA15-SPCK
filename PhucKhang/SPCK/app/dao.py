from models.user import User

users = [
    User("alice@example.com", "alice123"),
    User("bob@example.com", "bob456"),
    User("charlie@example.com", "charlie789"),
    User("dave@example.com", "dave1011"),
    User("eve@example.com", "eve1213"),
]

from models.course import Course

courses = [
    Course(course_id=1, icon="SPCK/app/assets/course1.png", name="IELTS band 8"),
    Course(course_id=2, icon="SPCK/app/assets/course2.png", name="Communication"),
    Course(course_id=3, icon="SPCK/app/assets/course1.png", name="English Grade 12"),
    Course(course_id=4, icon="SPCK/app/assets/course2.png", name="TOEIC Listening and Reading"),
    Course(course_id=5, icon="SPCK/app/assets/course1.png", name="English for Careers"),
]

# Set progress for each course
courses[0].set_user_progress("alice@example.com", 85)
courses[0].set_user_progress("bob@example.com", 90)
courses[0].set_user_progress("charlie@example.com", 75)

courses[1].set_user_progress("bob@example.com", 60)
courses[1].set_user_progress("dave@example.com", 40)
courses[1].set_user_progress("eve@example.com", 50)

courses[2].set_user_progress("charlie@example.com", 95)
courses[2].set_user_progress("alice@example.com", 70)
courses[2].set_user_progress("dave@example.com", 80)

courses[3].set_user_progress("eve@example.com", 65)
courses[3].set_user_progress("bob@example.com", 55)
courses[3].set_user_progress("charlie@example.com", 85)

courses[4].set_user_progress("alice@example.com", 60)
courses[4].set_user_progress("eve@example.com", 75)
courses[4].set_user_progress("dave@example.com", 90)
