# Generated by Django 3.1.3 on 2021-05-20 11:01

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, null=True)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('other', 'inna'), ('infa', 'informatyka'), ('matma', 'matematyka'), ('fizyka', 'fizyka'), ('biologia', 'biologia'), ('chemia', 'chemia')], default='other', max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True)),
                ('node_count', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('content', models.CharField(default='', max_length=2000)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('node_type', models.CharField(choices=[('lesson', 'Lekcja'), ('test', 'Test')], default='lesson', max_length=20)),
                ('node_number', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, null=True)),
                ('answers', models.ManyToManyField(to='courses.Answer')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.node')),
            ],
        ),
        migrations.CreateModel(
            name='LessonFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_type', multiselectfield.db.fields.MultiSelectField(choices=[('0', 'Wzrokowiec'), ('1', 'Kinestetyk'), ('2', 'S??uchowiec')], default='0', max_length=5)),
                ('lesson_file', models.FileField(upload_to=courses.models.get_upload_path)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.node')),
            ],
        ),
    ]
