# Generated by Django 4.0.3 on 2022-03-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_googlerecharge_transid'),
    ]

    operations = [
        migrations.AddField(
            model_name='googlerecharge',
            name='googleid',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
