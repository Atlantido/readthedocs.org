# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-05 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import readthedocs.ssh.mixins
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0026_ad-free-option'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSHKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('public_key', models.TextField(help_text='Add this to your version control to give us access.', verbose_name='Public SSH Key')),
                ('private_key', encrypted_model_fields.fields.EncryptedTextField(verbose_name='Private SSH Key')),
                ('json', models.TextField(blank=True, null=True, verbose_name='Serialized API response')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sshkeys', to='projects.Project')),
            ],
            bases=(readthedocs.ssh.mixins.SSHKeyGenMixin, models.Model),
        ),
    ]
