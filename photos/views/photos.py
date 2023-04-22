from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from photos.models.photo import Photo
from photos.models.favorite import Favorite
from photos.forms import PhotoForm, FavoriteForm


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_photo.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class PhotoUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photo

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('photos.update_photo')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDeleteView(UserPassesTestMixin,  DeleteView):
    template_name = 'photo_confirm_delete.html'
    model = Photo
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('photos.delete_photo')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class PhotoConfirmDeleteView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = get_object_or_404(Photo, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['pk'])
        photo.delete()
        return redirect('index')


class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Photo


class FavoriteView(LoginRequiredMixin, FormView):
    form_class = FavoriteForm

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        favorite_form = self.get_form_class()(request.POST)
        if favorite_form.is_valid():
            note = favorite_form.cleaned_data.get('note')
            user = request.user
            if not Favorite.objects.filter(user=user, photo=photo).exists():
                Favorite.objects.create(user=user, photo=photo, note=note)
                messages.success(request, 'Фото было добавлено в избранное')
        return redirect('index')


class FavoriteDeleteView(View):

    def post(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        user = request.user
        if user in photo.favorite.all():
            photo.favorite.remove(user)
            photo.save()
            return redirect('index')
        else:
            photo.favorite.add(user)
            photo.save()
            return redirect('index')
