from django.contrib import admin

admin.site.site_header = 'Rischool Management'

# Register your models here.
from .models import Student
from .models import Teacher
from .models import Subject
from .models import Level
from .models import Course
from .models import Class

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject_id', 'level_id', 'duration',
        'max_unit_load', 'min_unit_load']
    search_fields = ['name__contains', 'subject_id__name']

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id', 'teacher_id', 'schedule',
        'start_date', 'end_date']
    search_fields = ['name__contains', 'course_id__name', 'teacher_id__name']


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Level)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
