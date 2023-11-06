"""
    Custom pagination classes.
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'resPerPage': self.page.paginator.per_page,
            'count': self.page.paginator.count,
            'jobs': data
        })