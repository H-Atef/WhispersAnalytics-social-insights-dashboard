# Generated by Django 4.0.4 on 2022-07-02 10:34

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trend', models.CharField(max_length=30)),
                ('df', picklefield.fields.PickledObjectField(editable=False)),
                ('time_df', picklefield.fields.PickledObjectField(editable=False)),
                ('rltd_dict', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]
