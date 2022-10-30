# Generated by Django 3.2.8 on 2022-07-05 19:03

from django.db import migrations, models
import elk.validators


class Migration(migrations.Migration):

    dependencies = [
        ('elk', '0003_auto_20220705_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesmodel',
            name='files',
            field=models.FileField(upload_to='files/', validators=[elk.validators.validate_file_extension]),
        ),
    ]