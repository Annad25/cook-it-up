
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myapp.views import SearchResultsView

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("django.contrib.auth.urls")),
    path('', views.index,name="index"),
    path('index.html', views.index,name="index"),
    path('contact.html', views.contact_us,name="contact"),
    path('recipe.html', views.recipe,name="recipe"),
    path('about.html', views.about,name="about"),
    path('blog.html', views.blog,name="blog"),
    path('feature.html', views.feature,name="feature"),  
    path('view.html', views.view,name="view"),
    
    path('login.html', views.login,name="login"),
    path("search/", SearchResultsView.as_view(), name="search_results"),

    


   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)