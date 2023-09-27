# Generated by Django 3.2.12 on 2023-09-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='advocates_roll_number',
            fields=[
                ('roll_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='case',
            fields=[
                ('case_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pre_trial_date', models.DateField()),
                ('trial_date', models.DateField()),
                ('decision_date', models.DateField()),
                ('issuance_of_decree', models.TextField(default=None, null=True)),
                ('enforcement', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='cases_instances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('cases', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='court_system.case')),
            ],
        ),
        migrations.CreateModel(
            name='charge_sheet',
            fields=[
                ('accused', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('charges', models.TextField()),
                ('offense_description', models.TextField()),
                ('other_accused', models.CharField(default=None, max_length=50, null=True)),
                ('evidence', models.TextField(default=None, null=True)),
                ('penalties', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='clients_id',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='courts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lawyers',
            fields=[
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(default=None, max_length=50, null=True)),
                ('availability', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('cases', models.ManyToManyField(null=True, through='court_system.cases_instances', to='court_system.case')),
                ('roll_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='court_system.advocates_roll_number')),
            ],
        ),
        migrations.CreateModel(
            name='demand_letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=50)),
                ('demand', models.TextField()),
                ('deadline', models.DateField()),
                ('documents', models.TextField()),
                ('statement', models.TextField()),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='court_system.clients_id')),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('cases', models.ManyToManyField(through='court_system.cases_instances', to='court_system.case')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='court_system.clients_id', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='cases_instances',
            name='client',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='court_system.client'),
        ),
        migrations.AddField(
            model_name='cases_instances',
            name='lawyer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='court_system.lawyers'),
        ),
        migrations.AddField(
            model_name='case',
            name='charge_sheet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='court_system.charge_sheet', unique=True),
        ),
        migrations.AddField(
            model_name='case',
            name='court',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='court_system.courts'),
        ),
        migrations.AddField(
            model_name='case',
            name='demand_letter',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='court_system.demand_letter', unique=True),
        ),
    ]
