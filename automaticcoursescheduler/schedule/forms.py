from django.forms import ModelForm
from. models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        labels = {
            "room_number": "Room ID",
            "seating_capacity": "Capacity"
        }
        fields = [
            'room_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        labels = {
            "ins_id": "Teacher ID",
            "name": "Full Name"
        }
        fields = [
            'ins_id',
            'name',
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }
        labels = {
            "pid": "Meeting ID",
            "time": "Time",
            "day": "Day of the Week"
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'max_numb_students', 'instructors']
        labels = {
            "course_number": "Course ID",
            "course_name": "Course Name",
            "max_numb_students": "Course Capacity",
            "instructors": "Course Teachers"
        }
        widgets = {
            'instructors': forms.CheckboxSelectMultiple,
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']
        labels = {
            "dept_name": "Department Name",
            "courses": "Corresponding Courses"
        }


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week']
        labels = {
            "section_id": "Section ID",
            "department": "Corresponding Department",
            "num_class_in_week": "Classes Per Week"
        }

#upload to save in db
class ScheduleForm(forms.ModelForm):
    class Meta:
        model = GeneratedSchedule
        fields = ['pdf_file']

#testing file upload
class ScheduleUploadForm(forms.Form):
    schedule_file = forms.FileField(label='Select a CSV file')

#Sorting for generated schedule
class CSVUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['csv_file']