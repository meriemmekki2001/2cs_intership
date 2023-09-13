# Generated by Django 4.2.4 on 2023-09-07 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comptes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreDemande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinationCompte', models.CharField(choices=[('MGX', 'Moyens Généraux'), ('INT', 'Interconnexions')], default='MGX', max_length=15, verbose_name='Compte de Destination')),
                ('natureAchat', models.CharField(choices=[('001', 'Investissement'), ('002', 'Service'), ('003', 'Consommable'), ('004', 'Autre')], default='001', max_length=14, verbose_name="Nature de l'Achat")),
                ('na_autre', models.CharField(blank=True, max_length=255, null=True)),
                ('miseDiso', models.CharField(choices=[('001', 'Consommable interne'), ('002', 'Revente client'), ('003', 'Stock'), ('004', 'Autre')], default='001', max_length=18, verbose_name='mise Dispo')),
                ('md_autre', models.CharField(blank=True, max_length=255, null=True)),
                ('affectationAchat', models.CharField(choices=[('001', 'Famille accés internet'), ('002', 'Famille Communication unifié'), ('003', 'Famille CLOUD')], default='001', max_length=30, verbose_name="Affectation de l'Achat")),
                ('activee', models.BooleanField(default=True, verbose_name='activé')),
                ('validee', models.BooleanField(default=False, verbose_name='validé')),
                ('creee_le', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de soumition')),
                ('modifee_le', models.DateTimeField(default=django.utils.timezone.now, verbose_name='dernière modification')),
                ('cree_par', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='comptes.structure')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250, verbose_name='Désignation')),
                ('qtt', models.IntegerField(verbose_name='Quantité')),
                ('pre_demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit', to='core.predemande')),
            ],
        ),
    ]
