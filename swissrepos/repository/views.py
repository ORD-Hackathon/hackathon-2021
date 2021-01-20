from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from repository.models import Repository, Category, MaturityLevel, Metric, Indicator, MetricCategory


class CatalogueView(generic.ListView):
    template_name = 'catalogue.html'
    context_object_name = 'repositories'

    def get_queryset(self):
        return Repository.objects.values()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        for object in context['object_list']:
            if object['maturity_level_id'] == 1:
                object['stars'] = ['text-danger']
            elif object['maturity_level_id'] == 2:
                object['stars'] = ['text-warning', 'text-warning']
            elif object['maturity_level_id'] == 3:
                object['stars'] = ['text-info', 'text-info', 'text-info']
            elif object['maturity_level_id'] == 4:
                object['stars'] = ['text-success', 'text-success', 'text-success', 'text-success']
        return context


class MetricCategoriesView(generic.DetailView):
    model = Metric
    template_name = 'metric_category_list.html'
    context_object_name = 'metric'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        metric = context['object']
        categories = Category.objects.filter(metriccategory__metric__id=metric.id)
        context['categories'] = categories
        return context


class MetricIndicatorsView(generic.DetailView):
    model = Metric
    template_name = 'metric_indicator_list.html'
    context_object_name = 'metric'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        metric = context['object']
        indicators = Indicator.objects.filter(indicatorcategory__category__metriccategory__metric__id=metric.id).values()
        for indicator in indicators:
            if indicator['weight_id'] == 1:
                indicator['arrowsdown'] = ['text-success', 'text-success']
            elif indicator['weight_id'] == 2:
                indicator['arrowsdown'] = ['text-info']
            elif indicator['weight_id'] == 3:
                indicator['arrowsup'] = ['text-warning']
            elif indicator['weight_id'] == 4:
                indicator['arrowsup'] = ['text-danger', 'text-danger']
        context['indicators'] = indicators
        return context


class AssessmentView(generic.ListView):
    template_name = 'assessment.html'
    context_object_name = 'repositories'

    def get_queryset(self):
        return Repository.objects.values()


def add_category(request, metric_id):
    if request.POST:
        new_category = Category(name=request.POST.get('categoryName', ""), description=request.POST.get('categoryDescription', ""))
        new_metric_category = MetricCategory(category=new_category, metric_id=metric_id, maturity_level_id=1)
        new_category.save()
        new_metric_category.save()
        return HttpResponseRedirect(reverse('metricCategories', args=(metric_id,)))
    else:
        return render(request, 'add_category.html', {
            'metric_id': metric_id
        })

def edit_category(request, metric_id, category_id):
    return None


    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'add_category.html', {
    #         'metric_id': metric_id,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# class AssessmentFormView(generic.DetailView):
#     model = Repository
#     template_name = 'assessment_form.html'
#     context_object_name = 'repository'
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         repository = context['object']
#         categories = Category.objects.filter(metriccategory__metric__repository__id=repository.id).prefetch_related('indicatorcategory_set__indicator')
#         levels = MaturityLevel.objects.all()
#         context['categories'] = categories
#         context['levels'] = levels
#         return context
#
#
# def assessment(request):
#     return None