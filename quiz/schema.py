import graphene
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType
from .models import Question, Answer, Quiz, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ("id", "name", "category", "questions", "date_created")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "quiz", "title", "difficulty", "date_created", "is_active")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer")


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    quizzes = graphene.List(QuizType)
    questions = graphene.List(QuestionType)
    answers = graphene.List(AnswerType)

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_quizzes(self, info):
        return Quiz.objects.all()

    def resolve_questions(self, info):
        return Question.objects.all()

    def resolve_answers(self, info):
        return Answer.objects.all()
