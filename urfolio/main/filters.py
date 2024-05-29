import django_filters
from .models import Project
from django import forms

class ProjectFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(
        choices = Project.Category.choices,
        widget=forms.CheckboxSelectMultiple()
    )
    course_number = django_filters.MultipleChoiceFilter(
        choices=Project.CourseNumber.choices,
        widget=forms.CheckboxSelectMultiple()
    )
    year = django_filters.MultipleChoiceFilter(
        choices=Project.Year.choices,
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Project
        fields = {
            'author': ['exact'],
            #'category': ['exact'],
            #'course_number': ['exact'],
            #'year': ['exact'],
        }
