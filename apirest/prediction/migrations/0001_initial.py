# Generated by Django 3.0 on 2020-01-31 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.FloatField()),
                ('reassignment_count', models.FloatField()),
                ('reopen_count', models.FloatField()),
                ('sys_mod_count', models.FloatField()),
                ('made_sla', models.FloatField()),
                ('knowledge', models.FloatField()),
                ('u_priority_confirmation', models.FloatField()),
                ('sys_updated_by', models.FloatField()),
                ('category', models.FloatField()),
                ('subcategory', models.FloatField()),
                ('u_symptom', models.FloatField()),
                ('impact', models.FloatField()),
                ('urgency', models.FloatField()),
                ('contact_type_Direct_opening', models.FloatField()),
                ('contact_type_Email', models.FloatField()),
                ('contact_type_IVR', models.FloatField()),
                ('contact_type_Phone', models.FloatField()),
                ('contact_type_Self_service', models.FloatField()),
                ('incident_state_100', models.FloatField()),
                ('incident_state_Active', models.FloatField()),
                ('incident_state_Awaiting_Evidence', models.FloatField()),
                ('incident_state_Awaiting_Problem', models.FloatField()),
                ('incident_state_Awaiting_User_Info', models.FloatField()),
                ('incident_state_Awaiting_Vendor', models.FloatField()),
                ('incident_state_Closed', models.FloatField()),
                ('incident_state_New', models.FloatField()),
                ('incident_state_Resolved', models.FloatField()),
                ('isoWeekDay_1', models.FloatField()),
                ('isoWeekDay_2', models.FloatField()),
                ('isoWeekDay_3', models.FloatField()),
                ('isoWeekDay_4', models.FloatField()),
                ('isoWeekDay_5', models.FloatField()),
                ('isoWeekDay_6', models.FloatField()),
                ('isoWeekDay_7', models.FloatField()),
                ('hour', models.FloatField()),
                ('month', models.FloatField()),
                ('priority', models.FloatField()),
                ('time_before_resolution', models.FloatField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
