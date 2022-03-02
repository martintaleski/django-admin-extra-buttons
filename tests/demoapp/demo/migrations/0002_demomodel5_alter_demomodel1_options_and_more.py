# Generated by Django 4.0.2 on 2022-03-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoModel5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Choice Example',
                'verbose_name_plural': 'Choice Examples',
            },
        ),
        migrations.AlterModelOptions(
            name='demomodel1',
            options={'verbose_name': 'Button Example', 'verbose_name_plural': 'Button Examples'},
        ),
        migrations.AlterModelOptions(
            name='demomodel2',
            options={'verbose_name': 'Link Example', 'verbose_name_plural': 'Link Examples'},
        ),
        migrations.AlterModelOptions(
            name='demomodel3',
            options={'verbose_name': 'View Example', 'verbose_name_plural': 'View Examples'},
        ),
        migrations.AlterModelOptions(
            name='demomodel4',
            options={'verbose_name': 'Wizard Example', 'verbose_name_plural': 'Wizard Examples'},
        ),
    ]
