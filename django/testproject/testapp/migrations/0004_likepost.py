# Generated by Django 3.1 on 2020-10-20 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20201020_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likepostid', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='likepostid', to='testapp.userpost')),
                ('likeuserid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likeuserid', to='testapp.userdetails')),
            ],
        ),
    ]