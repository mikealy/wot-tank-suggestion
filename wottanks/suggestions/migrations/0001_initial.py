# Generated by Django 3.0.4 on 2020-04-28 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statparser', '0002_auto_20200425_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='TankRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank1average', models.DecimalField(decimal_places=5, default=0, max_digits=6)),
                ('tank2average', models.DecimalField(decimal_places=5, default=0, max_digits=6)),
                ('playercount', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tank1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tankrelation_primary', to='statparser.Tank')),
                ('tank2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tankrelation_secondary', to='statparser.Tank')),
            ],
        ),
    ]
