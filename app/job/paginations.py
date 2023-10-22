"""
    Custom pagination classes.
"""

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pa'
