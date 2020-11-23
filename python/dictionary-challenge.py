courses = [
    {"course": "How to Learn a new Language", "lecturer": "Matt", "rep": "Daniel Barnett"},
    {"course": "Foundations of Professional Software Engineering", "lecturer": "Derek", "rep": "Daniel Barnett"},
    {"course": "GA Programming Summer School", "lecturer": "Derek", "rep": "N/A"},
    {"course": "GA Foundation Maths Summer School", "lecturer": "Waqar", "rep": "N/A"}
]

newcourses = courses.copy()

newcourses[0]["lecturer"] = "Goudham"

print(newcourses)
print(courses)