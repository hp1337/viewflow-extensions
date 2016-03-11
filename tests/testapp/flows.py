from viewflow import flow
from viewflow.base import Flow, this
from viewflow.views import StartProcessView

from .models import SavableProcess
from .views import SavableProcessView


class SavableFlow(Flow):
    process_cls = SavableProcess
    start = flow.Start(StartProcessView, fields=[]).Next(this.savable_task)
    savable_task = flow.View(SavableProcessView) \
        .Assign(username='admin') \
        .Next(this.end)
    end = flow.End()
