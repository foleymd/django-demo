from django.shortcuts import render
from django.views.generic.base import TemplateView
from plotly.offline import plot
from plotly.graph_objs import Scatter
from moneytracker.models import PersonMonth

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context

def plotly(request):
    person_months= PersonMonth.objects.all()
    x_data = []
    y_data = []
    for person_month in person_months:
        month = person_month.get_month_display()
        year = person_month.get_year_display()
        x_data.append(month + ' ' + year)
        y_data.append(person_month.investments)

    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "plotly.html", context={'plot_div': plot_div})
