# Generated by Django 3.2.3 on 2022-01-20 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('correct_ans', models.CharField(max_length=250)),
                ('explanation', models.CharField(max_length=500)),
                ('question_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.question_set')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.question')),
            ],
        ),
    ]
