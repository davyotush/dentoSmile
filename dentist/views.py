from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def index(request):
    return render(request, 'home.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Message from ' + message_name,  # subject name
            message,  # message
            message_email,  # email
            ['davidorare7@gmail.com', 'otundodavid72@gmail.com']  # recipients
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def about(request):
    return render(request, 'about.html', {})


def appointment(request):
    if request.method == "POST":

        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        appointment = "Name:" + your_name + "" + "Phone No:" + your_phone + "" + "Email:" + your_email + "" + \
                      "Address:" + your_address + "" + "Scheduled Date:" + your_schedule + "" + "Time:" + your_time \
                      + "" + "Message:" + your_message
        send_mail(
            'Appointment Request from ',  # subject name
            appointment,  # message
            your_email,  # email
            ['davidorare7@gmail.com', 'otundodavid72@gmail.com']  # recipients
        )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_time': your_time,
            'your_message': your_message
        })

    else:
        return render(request, 'home.html', {})
