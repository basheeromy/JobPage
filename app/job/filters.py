"""
    Filters for job app.
"""

from django_filters import rest_framework as filters
from .models import Job


class JobsFilter(filters.FilterSet):
    """
        This class helps to filter jobs based
        on bellow defined criteria.
    """
    min_salary = filters.NumberFilter(
        field_name='salary' or 0,
        lookup_expr='gte'
    )
    max_salary = filters.NumberFilter(
        field_name='salary' or 10000000,
        lookup_expr='lte'
    )

    class Meta:
        model = Job
        fields = (
            'education',
            'jobType',
            'experience',
            'min_salary',
            'max_salary'
        )
