from pydantic import BaseModel, ConfigDict, Field

class BookingSummary(BaseModel):
    # Aufgabe: die drei öffentlichen Antwortfelder mit ihren Typen ergänzen.
    model_config = ConfigDict(from_attributes=True)
    student_id: int = Field(ge=1)
    student_name: str = Field(min_length=1, max_length= 101)
    booking_count: int = Field(ge=0)


class CoursesList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    student_id: int = Field(ge=1)
    courses: list 
