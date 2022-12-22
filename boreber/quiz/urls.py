
from django.urls import path
from bober.boreber.quiz.views import GetQuestion, QuestionAnswer

urlpatterns = [
    path('', GetQuestion.as_view()),
    path('answer/', QuestionAnswer.as_view()),
]