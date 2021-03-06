# Generated by Django 3.0.3 on 2020-12-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('kodeObat', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('namaOBat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Puskesmas',
            fields=[
                ('kodePkm', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('namaPkm', models.CharField(max_length=20)),
                ('alamat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DrugsQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.PositiveIntegerField()),
                ('tanggal', models.DateField()),
                ('kodeObat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudangObatService.Drugs')),
                ('kodePkm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gudangObatService.Puskesmas')),
            ],
        ),
    ]
