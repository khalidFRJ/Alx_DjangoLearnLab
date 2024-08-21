from django.shortcuts import render

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import MyModel

@permission_required('myapp.can_view', raise_exception=True)
def mymodel_list(request):
    objects = MyModel.objects.all()
    return render(request, 'myapp/mymodel_list.html', {'objects': objects})

@permission_required('myapp.can_edit', raise_exception=True)
def mymodel_edit(request, pk):
    obj = get_object_or_404(MyModel, pk=pk)
    # Handle the edit logic here
    return render(request, 'myapp/mymodel_edit.html', {'object': obj})

