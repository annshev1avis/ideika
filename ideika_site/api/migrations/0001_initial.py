# Generated by Django 4.2.1 on 2024-04-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('is_banned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CardInUserCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField(default=False)),
                ('added_dt', models.DateTimeField(auto_now_add=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.card')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50, null=True, unique=True)),
                ('registrate_date', models.DateField(auto_now_add=True)),
                ('collection_cards', models.ManyToManyField(related_name='users_like', through='api.CardInUserCollection', to='api.card')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_text', models.TextField()),
                ('direction', models.BooleanField(choices=[(0, 'Админу'), (1, 'Пользователю')], default=0)),
                ('is_watched', models.BooleanField(default=False)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.user')),
            ],
        ),
        migrations.AddField(
            model_name='cardinusercollection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category'),
        ),
        migrations.AddField(
            model_name='card',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user'),
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='cards', to='api.tag'),
        ),
    ]