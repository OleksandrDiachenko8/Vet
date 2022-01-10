# Generated by Django 4.0 on 2022-01-04 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant1', models.CharField(max_length=30, verbose_name='Варiант 1')),
                ('variant2', models.CharField(max_length=30, verbose_name='Варiант 2')),
                ('variant3', models.CharField(max_length=30, verbose_name='Варiант 3')),
                ('variant4', models.CharField(max_length=30, verbose_name='Варiант 4')),
            ],
            options={
                'verbose_name': 'Варiанти',
                'verbose_name_plural': 'Варiанти',
            },
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Тип питання')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Тип питання',
                'verbose_name_plural': 'Типи питань',
            },
        ),
        migrations.CreateModel(
            name='TestedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Користувач тесту',
                'verbose_name_plural': 'Користувачі тесту',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Назва тесту')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тести',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(null=True)),
                ('test_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.tests')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testeduser')),
            ],
            options={
                'verbose_name': 'Результат тесту',
                'verbose_name_plural': 'Результати тесту',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('question_picture', models.ImageField(blank=True, upload_to=None)),
                ('right_answer', models.CharField(max_length=30)),
                ('max_points', models.IntegerField()),
                ('answer_variants', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='test_app.answer_variants')),
                ('question_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.questioncategory')),
                ('test_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.tests')),
            ],
            options={
                'verbose_name': 'Питання',
                'verbose_name_plural': 'Питання',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=20)),
                ('point', models.IntegerField(null=True)),
                ('question_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.question')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testeduser')),
            ],
            options={
                'verbose_name': 'Відповідь користувача',
                'verbose_name_plural': 'Відповіді користувача',
            },
        ),
    ]
