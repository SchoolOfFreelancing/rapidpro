# Generated by Django 2.2.4 on 2020-04-16 11:15

from collections import defaultdict

from django.db import migrations

BATCH_SIZE = 5000

TYPE_MANUAL = "M"
TYPE_API = "A"
TYPE_FLOW_ACTION = "F"
TYPE_TRIGGER = "T"


def populate_flowstart_type(apps, schema_editor):  # pragma: no cover
    FlowStart = apps.get_model("flows", "FlowStart")

    starts = FlowStart.objects.filter(start_type=None).only("id", "created_by", "extra", "parent_summary")

    num_updated = 0
    max_id = -1
    while True:
        batch = list(starts.filter(id__gt=max_id).order_by("id")[:BATCH_SIZE])
        if not batch:
            break

        by_type = defaultdict(list)

        for start in batch:
            if start.created_by:
                start_type = TYPE_API if start.extra else TYPE_MANUAL
            else:
                start_type = TYPE_FLOW_ACTION if start.parent_summary else TYPE_TRIGGER

            by_type[start_type].append(start.id)

        for start_type, start_ids in by_type.items():
            FlowStart.objects.filter(id__in=start_ids).update(start_type=start_type)

        num_updated += len(batch)
        print(f" > Updated {num_updated} flow starts with a type")

        max_id = batch[-1].id


def reverse(apps, schema_editor):  # pragma: no cover
    pass


def apply_manual():  # pragma: no cover
    from django.apps import apps

    populate_flowstart_type(apps, None)


class Migration(migrations.Migration):

    dependencies = [("flows", "0230_flowstart_start_type")]

    operations = [migrations.RunPython(populate_flowstart_type, reverse)]