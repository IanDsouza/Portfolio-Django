from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import AdminFileWidget

class ProjectImageInline(admin.TabularInline):
	model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
	inlines = [ProjectImageInline]
	list_display = ('id','title','start_date','end_date',)
	list_display_links = ('id','title','start_date','end_date',)
	search_fields = ('title',)

admin.site.register(Project,ProjectAdmin)








admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(ProjectImage)
admin.site.register(Academic)










