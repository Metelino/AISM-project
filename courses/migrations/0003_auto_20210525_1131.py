# Generated by Django 3.1.3 on 2021-05-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_node_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(default='Odpowiedź', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(default=(), to='courses.Answer'),
        ),
    ]