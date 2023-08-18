from site_setup import models



#funcao nao precisa ter o mesmo nome da chave do diconario
def site_setup(request):
    data = models.SiteSetup.objects.order_by('-id').first()
    
    return {
        'site_setup': data,
    }