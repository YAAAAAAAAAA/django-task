# Generated by Django 2.2.4 on 2019-09-05 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestTrials',
            fields=[
                ('orden_code', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('planet_of_learning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('planet_habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Planet')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('test_trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TestTrials')),
            ],
        ),
        migrations.CreateModel(
            name='DiscipleTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciple', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='core.Recruit')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciples', to='core.Sith')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.Questions')),
                ('recruit', models.ManyToManyField(related_name='answers', to='core.Recruit')),
            ],
        ),
    ]
