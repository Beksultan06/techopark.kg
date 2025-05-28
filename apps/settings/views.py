from django.shortcuts import render, redirect
from apps.settings.models import BaseBanner, Settings, Services, Statistic, News, Contact
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    settings_id = Settings.objects.latest("id")
    services_all = Services.objects.all()
    statistic_all = Statistic.objects.all()
    news_all = News.objects.all()
    banners = BaseBanner.objects.latest("id")

    if request.method == 'POST':
        full_name = request.POST.get('username')
        email = request.POST.get('email')
        type_info = request.POST.get('info')
        message = request.POST.get('message')

        if full_name and email and type_info:
            Contact.objects.create(
                full_name=full_name,
                email=email,
                type_info=type_info,
                message=message
            )

            subject = f'Новое сообщение с сайта от {full_name}'
            body = f"""
            Имя: {full_name}
            Email: {email}
            Тип информации: {type_info}
            Сообщение:
            {message}
            """
            recipient = ['nurlanuuulubeksultan@gmail.com']
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, recipient)
            except Exception as e:
                print("Ошибка отправки email:", e)

            return redirect('index')
        else:
            error = "Пожалуйста, заполните все поля."
            context = {
                'banners': banners,
                'settings_id': settings_id,
                'services_all': services_all,
                'statistic_all': statistic_all,
                'news_all': news_all,
                'error': error
            }
            return render(request, 'base/index.html', context)

    return render(request, 'base/index.html', locals())


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('username')
        email = request.POST.get('email')
        type_info = request.POST.get('info')
        message = request.POST.get('message')

        if full_name and email and type_info:
            Contact.objects.create(
                full_name=full_name,
                email=email,
                type_info=type_info,
                message=message
            )

            subject = f'Новое сообщение с сайта от {full_name}'
            body = f"""
            Имя: {full_name}
            Email: {email}
            Тип информации: {type_info}
            Сообщение:
            {message}
            """
            recipient = ['nurlanuuulubeksultan@gmail.com']
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, recipient)
            except Exception as e:
                print("Ошибка отправки email:", e)

            return redirect('index')
        else:
            error = "Пожалуйста, заполните все поля."
            context = {
                'base_all': base_all,
                'settings_id': settings_id,
                'services_all': services_all,
                'statistic_all': statistic_all,
                'news_all': news_all,
                'error': error
            }
            return render(request, 'base/index.html', context)
    return render(request, 'base/contact.html', locals())


def testimonials(request):
    contacts = Contact.objects.order_by('-id')[:10]  # последние 10 отзывов
    first_five = contacts[:5]
    last_five = contacts[5:]
    return render(request, 'base/testimonials.html', {
        'first_five': first_five,
        'last_five': last_five
    })