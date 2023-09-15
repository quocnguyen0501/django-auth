from authentication.services.impl.HomeService import HomeService

from rest_framework import viewsets


class HomeView(viewsets.ViewSet):
  def __init__(self, *args, **kwargs):
    self.home_service = HomeService()
    super().__init__(*args, **kwargs)

  def home(self, request):
    return self.home_service.home(request=request)

