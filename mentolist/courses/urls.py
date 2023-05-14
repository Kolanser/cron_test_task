from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import OfflineApplicationViewSet, QuestionViewSet

# app_name = 'api'

router = DefaultRouter()


router.register('submit-applications', OfflineApplicationViewSet, basename='submit-application')
# router.register('categories/(?P<category_id>\\d+)/products',
#                 ProductViewSet,
#                 basename='products')
router.register('questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
    # path('send_mail/', MailView.as_view()),
    # path('brands/', BrandList.as_view()),
    # path('categories/', CategoryList.as_view()),
    # path('product_banners/', ProductBannerList.as_view()),
    # re_path('info_page/(?P<id>\\d+)/', InfoPageRetrieve.as_view()),
]
