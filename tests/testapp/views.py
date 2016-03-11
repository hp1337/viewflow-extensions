from viewflow.views import ProcessView

from viewflow_extensions.views import SavableViewActivationMixin


class SavableProcessView(SavableViewActivationMixin, ProcessView):
    fields = ['text']
