# Generated by Django 4.0.4 on 2022-06-27 03:23

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat_bot_b', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbot_model',
            name='intents',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
