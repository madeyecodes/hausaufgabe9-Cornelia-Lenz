from fastapi import APIRouter, HTTPException, Depends, Path
from sqlalchemy import func, select
from typing import Annotated

from hausaufgabe9.schemas import BookingSummary
from tag7.models import Booking, Course, Student
from tag9.dependencies import DbSession, require_staff
from tag9.models import User, AccessToken

router = APIRouter(prefix="/students", tags=["Buchungsübersicht"])

@router.get("/{student_id}/booking-summary", response_model=BookingSummary, dependencies=[Depends(require_staff)])
def booking_summary(student_id: Annotated[int, Path(ge=1)], db: DbSession):
    student = db.get(Student, student_id)
    if student is None:
        raise HTTPException(404, "Schüler nicht gefunden")
    bookin_count = db.scalar(select(func.count()).select_from(Booking).where(Booking.student_id==student_id))
    return {"student_id": student_id, "student_name": f"{student.first_name} {student.last_name}", "booking_count": bookin_count}
    # Aufgabe: Dependency, Rollenprüfung, Schema, Abfrage und Fehlerfälle.
    #raise HTTPException(501, "Noch nicht implementiert.")


#KI Verwendung: vor allem für Syntaxthemen, bzw um mir Dinge nochmal erklären zu lassen