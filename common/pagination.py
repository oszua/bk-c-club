from rest_framework.pagination import PageNumberPagination


class DataPagePagination(PageNumberPagination):

    # 设置每页显示条目为3条
    page_size = 3
    # 用户可以自定义选择一页的条数，但最多显示15条
    page_size_query_param = 'page_size'
    max_page_size = 15
    # 获取页码数
    page_query_param = 'page'
