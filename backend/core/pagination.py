from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination
from rest_framework.response import Response


class PageNumberPagination(BasePageNumberPagination):
    page_size = 25
    max_page_size = 25
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'next': bool(self.get_next_link()),
            'prev': bool(self.get_previous_link()),
            'data': data
        })