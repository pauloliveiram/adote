# Generated by Django 4.1.5 on 2023-01-13 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disclose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('AG', 'Aguardando Aprovação'), ('AP', 'Aprovado'), ('R', 'Recusado')], default='AG', max_length=2)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='disclose.pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]