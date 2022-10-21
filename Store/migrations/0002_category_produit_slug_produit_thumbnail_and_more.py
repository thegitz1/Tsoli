# Generated by Django 4.1.1 on 2022-09-14 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.AddField(
            model_name='produit',
            name='slug',
            field=models.SlugField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='models'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(default='Description du produit', null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='stock',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='titre',
            field=models.TextField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Store.category'),
        ),
    ]