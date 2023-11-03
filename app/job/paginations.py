"""
    Custom pagination classes.
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'pa'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'resPerPage': self.page.paginator.per_page,
            'count': self.page.paginator.count,
            'jobs': data
        })