from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Shop app 
    path('', include("shop.urls")),
    # Cart app
    path('cart/', include("cart.urls")),
    # Account app
    path('account/', include("account.urls")),
    # Payment app
    path('payment/', include("payment.urls")),
] 

# Media files config.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
