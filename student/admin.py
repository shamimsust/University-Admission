from django.contrib import admin
from student.models import Student, AppliedScienceDepartment,\
    PhysicalScienceDepartment, SocialScienceDepartment, LifeScienceDepartment,\
    BBADepartment


# Register your models here.

admin.site.register(Student)
admin.site.register(AppliedScienceDepartment)
admin.site.register(PhysicalScienceDepartment)
admin.site.register(SocialScienceDepartment)
admin.site.register(LifeScienceDepartment)
admin.site.register(BBADepartment)
