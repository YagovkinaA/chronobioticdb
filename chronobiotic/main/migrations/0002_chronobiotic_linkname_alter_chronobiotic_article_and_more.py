# Generated by Django 5.1.2 on 2024-11-19 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chronobiotic',
            name='linkname',
            field=models.SlugField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='article',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='chebi',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='chembil',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='chemspider',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='classf',
            field=models.ManyToManyField(help_text='Select a class for this molecula', to='main.bioclass'),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a  description of the biotic', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='drugbank',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='engage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='fdastatus',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='kegg',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='msds',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='pubchem',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='selleckchem',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='sider',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='toxnet',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chronobiotic',
            name='uniprot',
            field=models.URLField(blank=True, null=True),
        ),
    ]
