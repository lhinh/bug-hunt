# Generated by Django 3.0.3 on 2020-04-28 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200427_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachments',
            name='attachment_type_id',
        ),
        migrations.AddField(
            model_name='attachments',
            name='attachment_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bugreports',
            name='attachment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Attachments'),
        ),
        migrations.AlterField(
            model_name='attachments',
            name='location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='AttachmentTypes',
        ),
    ]