""" import graphene

import carlist.schema


class Query(carlist.schema.Query, graphene.ObjectType):
    # Esta clase heredara de multiples consultas
    # segun vayamos agregando aplicaciones a nuestro proyecto
    pass

schema = graphene.Schema(query=Query) """
import graphene
from graphene_django import DjangoObjectType
#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")
from carlist.models import Category, Car

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "cars")

class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "name", "line", "color","transmition","model" , "category")

class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_cars(root, info):
        # We can easily optimize query count in the resolve method
        return Car.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
schema = graphene.Schema(query=Query)