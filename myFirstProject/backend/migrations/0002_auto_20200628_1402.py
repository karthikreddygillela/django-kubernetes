# Generated by Django 2.2.4 on 2020-06-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('slug', models.CharField(default=None, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'state list',
            },
        ),
        migrations.AlterField(
            model_name='customercarddetails',
            name='card_number',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customercarddetails',
            name='cvv',
            field=models.CharField(default=None, max_length=3, null=True),
        ),
    ]
