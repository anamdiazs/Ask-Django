# Generated by Django 3.1.1 on 2020-09-18 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_create_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.create_question'),
        ),
    ]