# Generated by Django 5.1.3 on 2024-12-13 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sambandhanewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('preferredCharacter', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('son', 'Son'), ('daughter', 'Daughter'), ('grandfather', 'Grandfather'), ('grandmother', 'Grandmother'), ('uncle', 'Uncle')], max_length=100)),
                ('gotRelation', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('issuedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sambandhanewapp.useraccount')),
            ],
        ),
    ]
