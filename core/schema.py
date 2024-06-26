import graphene

import quiz.schema
import books.schema


class Query(quiz.schema.Query, books.schema.Query, graphene.ObjectType):
    pass


class Mutation(books.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
