from django.conf.urls import include, url
from viewflow.views import ProcessDetailView

from . import flows

urlpatterns = [
    url(r'^savable-flow/', include([
        flows.SavableFlow.instance.urls,
        url('^(?P<process_pk>\d+)/$', ProcessDetailView.as_view(), name='details'),

    ], namespace=flows.SavableFlow.instance.namespace),
        {'flow_cls': flows.SavableFlow}),
]
