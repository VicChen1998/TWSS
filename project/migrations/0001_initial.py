# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-09 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=16)),
                ('grade', models.IntegerField(default=0, verbose_name=2048)),
                ('sum', models.IntegerField(default=0, verbose_name=128)),
            ],
            options={
                'db_table': 'TWSS_Class',
            },
        ),
        migrations.CreateModel(
            name='CompetitionGuide',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=128)),
                ('type', models.CharField(default='未记录', max_length=16)),
                ('level', models.CharField(default='未记录', max_length=16)),
                ('rank', models.CharField(default=' ', max_length=4, null=True)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
                ('students', models.CharField(default='未记录', max_length=32)),
            ],
            options={
                'db_table': 'TWSS_CompetitionGuide',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name=4)),
                ('name', models.CharField(default='未记录', max_length=8)),
                ('head_of_department', models.CharField(default=0, max_length=16)),
            ],
            options={
                'db_table': 'TWSS_Department',
            },
        ),
        migrations.CreateModel(
            name='ExperimentCourse',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=32)),
                ('year', models.IntegerField(default=0)),
                ('semester', models.IntegerField(default=0, verbose_name=2)),
                ('classes', models.CharField(default='未记录', max_length=128)),
                ('student_sum', models.IntegerField(default=0, verbose_name=1024)),
                ('period', models.IntegerField(default=0, verbose_name=128)),
                ('credit', models.IntegerField(default=0, verbose_name=8)),
                ('attribute', models.IntegerField(default=0, verbose_name=4)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
                ('comment', models.CharField(max_length=32, null=True)),
                ('department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Department')),
            ],
            options={
                'db_table': 'TWSS_ExperimentCourse',
            },
        ),
        migrations.CreateModel(
            name='PaperGuide',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=128)),
                ('type', models.CharField(default='未记录', max_length=16)),
                ('level', models.CharField(default='未记录', max_length=16)),
                ('rank', models.CharField(default=' ', max_length=4, null=True)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
                ('author', models.CharField(default='未记录', max_length=16)),
            ],
            options={
                'db_table': 'TWSS_PaperGuide',
            },
        ),
        migrations.CreateModel(
            name='PraticeCourse',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=32)),
                ('year', models.IntegerField(default=0)),
                ('semester', models.IntegerField(default=0, verbose_name=2)),
                ('classes', models.CharField(default='未记录', max_length=128)),
                ('student_sum', models.IntegerField(default=0, verbose_name=1024)),
                ('period', models.IntegerField(default=0, verbose_name=128)),
                ('credit', models.IntegerField(default=0, verbose_name=8)),
                ('attribute', models.IntegerField(default=0, verbose_name=4)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
                ('comment', models.CharField(max_length=32, null=True)),
                ('department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Department')),
            ],
            options={
                'db_table': 'TWSS_PraticeCourse',
            },
        ),
        migrations.CreateModel(
            name='TeachingAchievement',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=128)),
                ('type', models.CharField(default='未记录', max_length=16)),
                ('level', models.CharField(default='未记录', max_length=16)),
                ('rank', models.CharField(default=' ', max_length=4, null=True)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
            ],
            options={
                'db_table': 'TWSS_TeachingAchievement',
            },
        ),
        migrations.CreateModel(
            name='TeachingProject',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=128)),
                ('type', models.CharField(default='未记录', max_length=16)),
                ('level', models.CharField(default='未记录', max_length=16)),
                ('rank', models.CharField(default=' ', max_length=4, null=True)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
            ],
            options={
                'db_table': 'TWSS_TeachingProject',
            },
        ),
        migrations.CreateModel(
            name='TheoryCourse',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=32)),
                ('year', models.IntegerField(default=0)),
                ('semester', models.IntegerField(default=0, verbose_name=2)),
                ('classes', models.CharField(default='未记录', max_length=128)),
                ('student_sum', models.IntegerField(default=0, verbose_name=1024)),
                ('period', models.IntegerField(default=0, verbose_name=128)),
                ('credit', models.IntegerField(default=0, verbose_name=8)),
                ('attribute', models.IntegerField(default=0, verbose_name=4)),
                ('audit_status', models.IntegerField(default=0, verbose_name=2)),
                ('comment', models.CharField(max_length=32, null=True)),
                ('department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Department')),
            ],
            options={
                'db_table': 'TWSS_TheoryCourse',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='未记录', max_length=16)),
                ('title', models.CharField(default='未记录', max_length=16)),
                ('status', models.CharField(default='未记录', max_length=16)),
                ('password', models.CharField(default='未记录', max_length=32)),
                ('phone_number', models.CharField(default='未记录', max_length=11)),
                ('email', models.CharField(default='未记录', max_length=32)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Department')),
            ],
            options={
                'db_table': 'TWSS_User',
            },
        ),
        migrations.AddField(
            model_name='theorycourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='teachingproject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='teachingachievement',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='praticecourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='paperguide',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='experimentcourse',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='competitionguide',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='class',
            name='department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='project.Department'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
    ]
