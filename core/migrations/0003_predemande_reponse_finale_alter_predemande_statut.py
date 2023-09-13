# Generated by Django 4.2.4 on 2023-09-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_predemande_activee_remove_predemande_validee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='predemande',
            name='reponse_finale',
            field=models.CharField(blank=True, choices=[('001', 'Rejetée par le directeur de la structure'), ('002', "Rejetée par le service d'achat"), ('003', "Validée par le service d'achat")], max_length=40, null=True, verbose_name='Réponse finale'),
        ),
        migrations.AlterField(
            model_name='predemande',
            name='statut',
            field=models.CharField(choices=[('001', 'En cours'), ('002', "Annulée par l'utilisateur"), ('004', 'Validée par le directeur de la structure'), ('005', 'Clôturée')], default='001', max_length=40, verbose_name='Statut'),
        ),
    ]
