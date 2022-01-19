# Generated by Django 3.2.3 on 2022-01-18 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_set',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('correct_ans', models.TextField(max_length=250)),
                ('explanation', models.TextField(max_length=500)),
                ('question_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.question_set')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('option', models.TextField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.question')),
            ],
        ),
    ]