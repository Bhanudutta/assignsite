from django.urls import register_converter,path

from . import  views

class SignedIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value

register_converter(SignedIntConverter, 'signint')

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:name>/<int:parent_id>',views.add,name='add'),
    path('delete/<signint:id>',views.delete,name='delete'),
    path('view/<signint:parent_id>',views.view,name='view')
]
