from django.urls import path, re_path
from .views import CompanyListAPIView,VacancyListAPIView, VacancyDetailAPIView, CompanyDetailAPIView,company_list,company_vacancies,vacancy_list,vacancy_detail,top_ten_vacancies,company_detail
urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies/', company_vacancies, name='company_vacancies'),
    path('vacancies/', vacancy_list, name='vacancy_list'),
    path('vacancies/<int:id>/', vacancy_detail, name='vacancy_detail'),
    path('vacancies/top_ten/', top_ten_vacancies, name='top_ten_vacancies'),
#     path('companies/', company_list),
#     path('companies/<int:id>/', company_detail),
#     path('vacancies/', VacancyListAPIView.as_view()),
#     path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),

]
