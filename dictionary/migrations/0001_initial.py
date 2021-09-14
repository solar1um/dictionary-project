# Generated by Django 3.2.7 on 2021-09-14 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_meaning', models.TextField(max_length=500)),
                ('current_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_wrd', to='dictionary.word')),
            ],
        ),
    ]
