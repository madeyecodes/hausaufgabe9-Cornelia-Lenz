"""Aufgabe 4: Anforderungen aus test_course_list.py ableiten."""
## /students/{student_id}/courses fehl, nur Staff darf sie verwenden ()
#test_without_login und test_reader_is_forbidden
# Status code erfolgreich: 200
#response.json(): {"student_id": sample[key], "courses": expected_courses}
# bsp Harry: {"student_id": 11, "courses": [
    #     {"course_id": 103, "title": "Kräuterkunde"},
    #     {"course_id": 101, "title": "Verwandlung"},
    #     {"course_id": 102, "title": "Zauberkunst"},
    # ]}
#Reihenfolge der Kurse nach alphabetisch test_changed_database_title_is_returned_in_sorted_position
# Student, Course und Booking müssen aus mysql kommen 





from fastapi import APIRouter, HTTPException, Depends, Path
from sqlalchemy import func, select
from typing import Annotated

from hausaufgabe9.schemas import BookingSummary, CoursesList
from tag7.models import Booking, Course, Student
from tag9.dependencies import DbSession, require_staff
from tag9.models import User, AccessToken

router = APIRouter(prefix="/students", tags=["Kursliste"])

@router.get("/{student_id}/courses", response_model=CoursesList, dependencies=[Depends(require_staff)])
def course_listing(student_id: Annotated[int, Path(ge=1)], db: DbSession):
    student = db.get(Student, student_id)
    if student is None:
        raise HTTPException(404, "Schüler nicht gefunden")
    student_booking = db.scalars(select(Booking).join(Course, Course.id == Booking.course_id).where(Booking.student_id==student.id).order_by(Course.title)).all()
    #print("HIER IST DEIN PRINT!!!!!")
    courses = []
    for row in student_booking:
        courses.append({
            "course_id": row.course_id,
            "title": row.course.title
        })
    return {
        "student_id": student.id,
        "courses": courses
    }

# Aufgabe: Die durch die Tests beschriebene Route hier implementieren.
# Die Einbindung des Routers in main.py ist bereits vorbereitet.
