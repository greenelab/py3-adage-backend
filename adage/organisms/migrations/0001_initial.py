# Generated by Django 2.2.5 on 2019-09-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxonomy_id', models.PositiveIntegerField(db_index=True, help_text='Taxonomy ID assigned by NCBI', unique=True)),
                ('common_name', models.CharField(help_text="Organism common name, e.g. 'Human'", max_length=60, unique=True)),
                ('scientific_name', models.CharField(help_text="Organism scientific/binomial name, e.g. 'Homo sapiens'", max_length=60, unique=True)),
                ('slug', models.SlugField(help_text='URL slug created by calling slugify() on scientific_name in the management command when the organism is added', unique=True)),
            ],
        ),
    ]
