# Generated by Django 4.0 on 2022-01-09 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_testeduser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testeduser',
            options={'verbose_name': 'Користувач тесту', 'verbose_name_plural': 'Користувачі тесту'},
        ),
        migrations.AlterField(
            model_name='answer',
            name='point',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue1',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue2',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue3',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue4',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue5',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='answer_variants',
            name='istrue6',
            field=models.BooleanField(default=False, verbose_name='вірний?'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_variants',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_app.answer_variants'),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='name',
            field=models.CharField(choices=[('S', 'Коротка відповідь'), ('SC', 'Одиночний вибір'), ('MC', 'Множинний вибір'), ('G', 'Insert_blanks')], default='S', max_length=2, verbose_name='Тип питання'),
        ),
    ]
