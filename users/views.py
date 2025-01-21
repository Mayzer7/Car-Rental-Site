from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, TemplateView
from users.forms import UserLoginForm ,UserRegistrationForm
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')

    def get_success_url(self):
        # Проверка на наличие параметра `next`
        redirect_page = self.request.POST.get('next') or self.request.GET.get('next')
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def form_valid(self, form):
        """
        Выполняется, если форма валидна.
        """
        user = form.get_user()
        if user:
            auth.login(self.request, user)  # Аутентификация пользователя
            messages.success(self.request, f"{user.username}, вы успешно вошли!")
            return HttpResponseRedirect(self.get_success_url())

        # Если пользователь не найден, редирект на страницу логина
        messages.error(self.request, "Ошибка входа. Пользователь не найден.")
        return HttpResponseRedirect(reverse_lazy('user:login'))

    def form_invalid(self, form):
        """
        Выполняется, если форма недействительна.
        """
        messages.error(self.request, "Ошибка входа. Проверьте введённые данные.")
        return self.render_to_response(self.get_context_data(form=form))


class UserRegistationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.save()

        # Указываем backend для аутентификации
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth.login(self.request, user)

        # if session_key:
        #     Cart.objects.filter(session_key=session_key).update(user=user)

        messages.success(self.request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")

        return HttpResponseRedirect(self.success_url)
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context    
    

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))