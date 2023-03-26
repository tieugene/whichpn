from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpSoS',
            fields=[
                ('tin', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='TIN')),
                ('name', models.CharField(max_length=239, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'OpSoS',
                'verbose_name_plural': 'OpSoSes',
                'db_table': 'opsos',
                'ordering': ('tin',),
            },
        ),
        migrations.CreateModel(
            name='SNRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndc', models.PositiveSmallIntegerField(db_index=True, verbose_name='NDC')),
                ('beg', models.PositiveIntegerField(db_index=True, verbose_name='SN from')),
                ('end', models.PositiveIntegerField(db_index=True, verbose_name='SN to')),
                ('region', models.CharField(max_length=526, verbose_name='Region')),
                ('opsos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.opsos',
                                            verbose_name='OpSoS')),
            ],
            options={
                'verbose_name': 'SN Range',
                'verbose_name_plural': 'SN Ranges',
                'db_table': 'snrange',
                'ordering': ('ndc', 'beg'),
                'unique_together': {('ndc', 'beg')},
            },
        ),
    ]
