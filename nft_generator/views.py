from django.views import generic
from .models import NoneFungibleToken
from .tasks import create_nft
from .forms import NFTForm

class HomeView(generic.TemplateView):
    template_name = "nft_generator/index.html"

class NFTGeneratorView(generic.FormView):
    form_class = NFTForm
    template_name = "nft_generator/nft_generator.html"
    success_url = '/nfts'
    
    def form_valid(self, form):
        quantity = form.cleaned_data.get('quantity')
        #this is a celery task
        create_nft.delay(quantity)
        return super().form_valid(form)
        
class NFTView(generic.DetailView):
    template_name = "nft_generator/nft.html"
    model = NoneFungibleToken

class NFTSView(generic.ListView):
    template_name = "nft_generator/nfts.html"
    model = NoneFungibleToken
    paginate_by = 50

    def get_queryset(self):
        
        object_list = sorted(self.model.objects.all(), key = lambda r: r.overall_rarity)
        return object_list

