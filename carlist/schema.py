import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from carlist.models import Category, Car


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'cars']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class CarNode(DjangoObjectType):
    class Meta:
        model = Car
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'line': ['exact', 'icontains', 'istartswith'],
            'color': ['exact', 'icontains'],
            'transmition': ['exact', 'icontains'],
            'model': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    cars = relay.Node.Field(CarNode)
    all_cars = DjangoFilterConnectionField(CarNode)
