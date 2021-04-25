
from django.urls import path
from .views import postview, postcreate, subjectview, ContactView, postView, postDetailView, postEditView, postDeleteView
from .forms import ContactForm2
app_name='education'

urlpatterns = [
    # path('contact/', contact, name="contact"),
    path('contact/', ContactView.as_view(), name="contact"),
    # path('contact2/', ContactView.as_view(form_class=ContactForm2, template_name="contact copy.html"), name="contact"),
    path('postlist/', postView.as_view() , name="postlist"),
    path('postdetail/<int:pk>/', postDetailView.as_view() , name="postdetail"),
    path('edit/<int:pk>/', postEditView.as_view() , name="edit"),
    path('delete/<int:pk>/', postDeleteView.as_view() , name="delete"),
    path('post/', postview , name="post"),
    path('create/', postcreate , name="create"),
    path('subject/', subjectview , name="subject"),
]
