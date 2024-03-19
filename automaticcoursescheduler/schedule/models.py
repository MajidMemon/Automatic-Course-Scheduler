from django.db import models
import math
import random as rnd
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from datetime import timedelta, date
from account.models import Profile
from django.utils import timezone


time_slots = (
    ('8:30 - 11:30', '8:30 - 11:30'),
    ('11:45 - 2:45', '11:45 - 2:45'),
    ('3:00 - 6:00', '3:00 - 6:00'),
    ('6:30 - 9:30', '6:30 - 9:30'),

)

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


class Room(models.Model):
    room_number = models.CharField(max_length=6)
    seating_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.room_number


class Instructor(models.Model):
    ins_id = models.CharField(max_length=6)
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.ins_id} {self.name}'


class MeetingTime(models.Model):
    pid = models.CharField(max_length=4, primary_key=True)
    time = models.CharField(max_length=50, choices=time_slots, default='8:30 - 11:45')
    day = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self):
        return f'{self.pid} {self.day} {self.time}'


class Course(models.Model):
    course_number = models.CharField(max_length=5, primary_key=True)
    course_name = models.CharField(max_length=40)
    max_numb_students = models.CharField(max_length=65)
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return f'{self.course_number} {self.course_name}'


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)

    @property
    def get_courses(self):
        return self.courses

    def __str__(self):
        return self.dept_name


class Section(models.Model):
    section_id = models.CharField(max_length=25, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    num_class_in_week = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    meeting_time = models.ForeignKey(MeetingTime, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, blank=True, null=True)

    def set_room(self, room):
        section = Section.objects.get(pk = self.section_id)
        section.room = room
        section.save()

    def set_meetingTime(self, meetingTime):
        section = Section.objects.get(pk = self.section_id)
        section.meeting_time = meetingTime
        section.save()

    def set_instructor(self, instructor):
        section = Section.objects.get(pk=self.section_id)
        section.instructor = instructor
        section.save()



#save the generated schedule into the database:
        
class GeneratedSchedule(models.Model):
    pdf_file = models.FileField(upload_to='generated_pdfs/')
    upload_date = models.DateField(default=timezone.now)
    upload_time = models.TimeField(default=timezone.now)

    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        if self.uploaded_by:
            return f"Uploaded by {self.uploaded_by.user} on {self.upload_date} at {self.upload_time}"
        else:
            return f"Uploaded on {self.upload_date} at {self.upload_time}"

#upload csv file and view and sort it
class UploadedFile(models.Model):
    csv_file = models.FileField(upload_to='csv_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.csv_file.name