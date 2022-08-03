#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 23:19:18 2022

@author: kunyu
"""

import graphene
from graphene_django import DjangoObjectType, DjangoConnectionField
from .models import Category, TradeInfo
import decimal
from django_filters import FilterSet, OrderingFilter
from graphene import ObjectType, Schema, relay
from graphene_django.filter import DjangoFilterConnectionField

class CategoryType(DjangoObjectType):
    class Meta: 
        model = Category
        fields = ('id','title')
    

class InfoType(DjangoObjectType):
    class Meta:
        model = TradeInfo
        fields = (
            'Name',
            'Date',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
        )
        interfaces = (graphene.relay.Node,)
        filter_fields = {'Name': ['exact', 'icontains', 'istartswith', 'in'],
                         'Date': ['exact', 'range', 'in'],
                         'Open': ['exact', 'range', 'in'], 
                         'High': ['exact', 'range', 'in'], 
                         'Low': ['exact', 'range', 'in'], 
                         'Close':['exact', 'range', 'in'], 
                         'Volume': ['exact', 'range', 'in'],
                         }

class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
     
    #trades = graphene.List(InfoType)
    trades = relay.Node.Field(InfoType)
    all_trades = DjangoFilterConnectionField(InfoType)

    def resolve_trades(root, info, **kwargs):
        # Querying a list
        return TradeInfo.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()

schema = graphene.Schema(query=Query)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        title = graphene.String(required=True)
        id = graphene.ID()


    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()
        
        return UpdateCategory(category=category)



class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    # Class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()
        
        return CreateCategory(category=category)

class TradeInfoInput(graphene.InputObjectType):
    Name = graphene.String()
    Date = graphene.Date()
    Open = graphene.Decimal()
    High = graphene.Decimal()
    Low = graphene.Decimal()
    Close = graphene.Decimal()
    Volume = graphene.Int()
    
class CreateTradeInfo(graphene.Mutation):
    class Arguments:
        input = TradeInfoInput(required=True)

    tradeinfo = graphene.Field(InfoType)
    
    @classmethod
    def mutate(cls, root, info, input):
        tradeinfo = TradeInfo()
        tradeinfo.Name = input.Name
        tradeinfo.Date = input.Date
        tradeinfo.Open = input.Open
        tradeinfo.High = input.High
        tradeinfo.Low = input.Low
        tradeinfo.Close = input.Close
        tradeinfo.Volume = input.Volume
        
        tradeinfo.save()
        return CreateTradeInfo(tradeinfo=tradeinfo)

class UpdateTradeInfo(graphene.Mutation):
    class Arguments:
        input = TradeInfoInput(required=True)
        id = graphene.ID()

    tradeinfo = graphene.Field(InfoType)
    
    @classmethod
    def mutate(cls, root, info, input, id):
        tradeinfo = TradeInfo.objects.get(pk=id)
        tradeinfo.Name = input.Name
        tradeinfo.Date = input.Date
        tradeinfo.Open = input.Open
        tradeinfo.High = input.High
        tradeinfo.Low = input.Low
        tradeinfo.Close = input.Close
        tradeinfo.Volume = input.Volume
        
        tradeinfo.save()
        
        return UpdateTradeInfo(tradeinfo=tradeinfo)

class Mutation(graphene.ObjectType):
    update_category = UpdateCategory.Field()
    create_category = CreateCategory.Field()
    create_tradeinfo = CreateTradeInfo.Field()
    update_tradeinfo = UpdateTradeInfo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)