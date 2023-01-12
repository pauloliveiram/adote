from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tag, Breed, Pet
from django.contrib import messages
from django.contrib.messages import constants

@login_required
def new_pet(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        breeds = Breed.objects.all()

        context = {'tags': tags, 
                   'breeds': breeds}

        return render(request, 'new_pet.html', context)
    elif request.method == 'POST':
        photo = request.FILES.get('foto')
        name = request.POST.get('nome')
        description = request.POST.get('descricao')
        state = request.POST.get('estado')
        city = request.POST.get('cidade')
        phone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        breed = request.POST.get('raca')

        pet = Pet(
            user = request.user,
            photo=photo,
            name=name,
            description=description,
            state=state,
            city=city,
            phone=phone,
            breed_id=breed,
        )

        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)

        pet.save()

        tags = Tag.objects.all()
        breeds = Breed.objects.all()

        context = {
            'tags': tags,
            'breeds': breeds,
        }

        messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
        return render(request, 'new_pet.html', context)    