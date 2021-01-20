from django.urls import path

from repository import views

urlpatterns = [
    path('', views.CatalogueView.as_view(), name='catalogue'),
    path('metrics/<int:pk>/categories', views.MetricCategoriesView.as_view(), name='metricCategories'),
    path('metrics/<int:metric_id>/categories/add', views.add_category, name='addCategory'),
    path('metrics/<int:metric_id>/categories/<int:category_id>/edit', views.edit_category, name='editCategory'),
    path('metrics/<int:pk>/indicators', views.MetricIndicatorsView.as_view(), name='metricIndicators'),
    path('assessments', views.AssessmentView.as_view(), name='assessment'),
    # path('assessments/<int:pk>', views.AssessmentFormView.as_view(), name='assessmentForm'),
    # path('assessments/<int:repository_id>/save', views.assessment, name='assessmentSave'),
]