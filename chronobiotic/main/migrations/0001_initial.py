# Generated by Django 5.1.2 on 2024-11-19 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bioclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameclass', models.CharField(help_text='Enter a class(e.g. chronobiotics, radioprotectors)', max_length=128)),
            ],
            options={
                'db_table': 'class',
            },
        ),
        migrations.CreateModel(
            name='Clinicaltrials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trialsname', models.URLField(help_text='Enter a link about trials')),
            ],
            options={
                'db_table': 'trials',
            },
        ),
        migrations.CreateModel(
            name='Mechanism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanismname', models.CharField(help_text='Enter a mechanism(e.g. relax, energy, tea , coffe)', max_length=128)),
            ],
            options={
                'db_table': 'mechanism',
            },
        ),
        migrations.CreateModel(
            name='Chronobiotic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=128, unique=True)),
                ('smiles', models.CharField(max_length=256, unique=True)),
                ('molecula', models.CharField(max_length=256, unique=True)),
                ('iupacname', models.CharField(max_length=256, unique=True)),
                ('updphoto', models.ImageField(upload_to='media/')),
                ('description', models.TextField(help_text='Enter a  description of the biotic', max_length=1000)),
                ('fdastatus', models.CharField(max_length=64, null=True)),
                ('article', models.URLField(null=True)),
                ('pubchem', models.URLField(null=True)),
                ('chemspider', models.URLField(null=True)),
                ('drugbank', models.URLField(null=True)),
                ('chebi', models.URLField(null=True)),
                ('chembil', models.URLField(null=True)),
                ('uniprot', models.URLField(null=True)),
                ('engage', models.URLField(null=True)),
                ('kegg', models.URLField(null=True)),
                ('msds', models.URLField(null=True)),
                ('sider', models.URLField(null=True)),
                ('toxnet', models.URLField(null=True)),
                ('selleckchem', models.URLField(null=True)),
                ('classf', models.ManyToManyField(help_text='Select a genre for this book', to='main.bioclass')),
                ('clinictrials', models.ManyToManyField(help_text='Select a class for this biotic', to='main.clinicaltrials')),
                ('mechanisms', models.ManyToManyField(help_text='Select a synonyms of this ', to='main.mechanism')),
            ],
            options={
                'db_table': 'chronobiotic',
            },
        ),
        migrations.CreateModel(
            name='Synonyms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synonymsmname', models.CharField(help_text='Enter a synonyms(e.g.soal,soul,solar,systemofalllines)', max_length=128)),
                ('originalbiotic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.chronobiotic')),
            ],
            options={
                'db_table': 'synonyms',
            },
        ),
    ]
