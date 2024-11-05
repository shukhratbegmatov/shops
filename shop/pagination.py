from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'per_page': self.page_size,
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            # 'page_items': len(self.page),
            'total': self.page.paginator.count,
            'results': data
        })


class Short(CustomPagination):
    page_size = 4


class DoubleShort(CustomPagination):
    page_size = 8


class MidShort(CustomPagination):
    page_size = 6


class ExtraShort(CustomPagination):
    page_size = 10


class ExtremeShort(CustomPagination):
    page_size = 3


class Middle(CustomPagination):
    page_size = 12


class ExtraMiddle(CustomPagination):
    page_size = 15

class MidLarge(CustomPagination):
    page_size = 21
    
class Large(CustomPagination):
    page_size = 28