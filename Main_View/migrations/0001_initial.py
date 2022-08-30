# Generated by Django 3.1.4 on 2021-12-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(max_length=150, verbose_name='Review&Comment Text')),
                ('related_name', models.CharField(max_length=50, verbose_name='Customer Name')),
            ],
            options={
                'verbose_name': 'Reviews',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]