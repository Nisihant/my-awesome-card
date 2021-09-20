# Generated by Django 3.2.7 on 2021-09-20 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=200)),
                ('sub_category', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=200)),
                ('pub_date', models.DateField()),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='', verbose_name='shop/media')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category', verbose_name='catogories')),
            ],
        ),
    ]
