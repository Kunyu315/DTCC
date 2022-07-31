#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:19:18 2022

@author: kunyu
"""

import graphene
from graphene_django import DjangoObjectType
from .models import Category, TradeInfo

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ('id','title')
"""
  
class BookType(DjangoObjectType):
    class Meta: 
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'isbn',
            'pages', 
            'price',
            'quantity', 
            'description',
            'imageurl',
            'status',
            'date_created',
        )  

class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = (
            'product_tag',
            'name',
            'category',
            'price',
            'quantity',
            'imageurl',
            'status',
            'date_created',
        )
"""

class InfoType(DjangoObjectType):
    class Meta:
        model = TradeInfo
        fields = (
            'name',
            'Date',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
        )

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
     
    trades = graphene.List(InfoType)

    def resolve_trades(root, info, **kwargs):
        # Querying a list
        return TradeInfo.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()
"""
    def resolve_groceries(root, info, **kwargs):
        # Querying a list
        return Grocery.objects.all()
"""
schema = graphene.Schema(query=Query)