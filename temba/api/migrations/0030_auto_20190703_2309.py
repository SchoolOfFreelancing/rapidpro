# Generated by Django 2.1.8 on 2019-07-03 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api", "0029_initial")]

    operations = [
        migrations.RemoveField(model_name="webhookevent", name="event"),
        migrations.RemoveField(model_name="webhookevent", name="status"),
        migrations.RemoveField(model_name="webhookevent", name="try_count"),
    ]
