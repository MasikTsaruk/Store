from django.views.generic.edit import CreateView
from .forms import OrderForm
from .models import Order
from django.urls import reverse_lazy



class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:create_order')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)



