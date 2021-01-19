from django.views import generic

from repository.models import Repository


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

