from django.shortcuts import render, redirect
from disclose.models import Pet, Breed
from django.contrib.auth.decorators import login_required
from .models import AdoptionRequest
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import send_mail

def list_pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(status='P')
        breeds = Breed.objects.all()
        
        city = request.GET.get('cidade')
        breed_filter = request.GET.get('raca')

        if city:
            pets = pets.filter(city__icontains=city)

        if breed_filter:
            pets = pets.filter(breed__id=breed_filter)    
            breed_filter = Breed.objects.get(id=breed_filter)

        context = {'pets': pets,
                   'breeds': breeds,
                   'city': city,
                   'breed_filter': breed_filter}

        return render(request, 'list_pets.html', context)

@login_required
def adoption_request(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status='P')

    if not pet.exists():
        messages.add_message(request, constants.WARNING, 'Esse pet já foi adotado!')
        return redirect('adoption')

    req = AdoptionRequest(pet=pet.first(),
                          user=request.user,
                          date=datetime.now())

    req.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adoption')                      

@login_required
def see_adoption_request(request):
    if request.method == 'GET':
        adoption_requests = AdoptionRequest.objects.filter(user=request.user).filter(status='AG')
        context = {'adoption_requests': adoption_requests}
        return render(request, 'see_adoption_request.html', context)

@login_required
def process_adoption_request(request, id_request):
    status = request.GET.get('status')
    adoption_request = AdoptionRequest.objects.get(id=id_request)

    if status == 'A':
        adoption_request.status = 'AP'
        string = '''Olá, a sua solicitação para adoção foi aprovada'''
    elif status == 'R':
        adoption_request.status = 'R'
        string = '''Olá, a sua solicitação para adoção foi recusada'''

    adoption_request.save()

    email = send_mail(
        'Sua solicitação por adoção foi processada',
        string,
        'paulo.o.medeiros@hotmail.com',
        [request.user.email,],
    )

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado com sucesso')
    return redirect('/adoption/see_adoption_request')