from django.contrib import admin
from .models import SLTLoan,SlT_Payment_summary


# class SLTSurveyAdmin(admin.ModelAdmin):
#     list_display = ('surveyid', 'SLTID', 'survey_questions_id')
    

# Register your models here.
# admin.site.register(Survey_questions)
admin.site.register(SLTLoan)
admin.site.register(SlT_Payment_summary)