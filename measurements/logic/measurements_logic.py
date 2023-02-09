from variables.models import Variable

from ..models import Measurement



def get_measurements():
    measurement = Measurement.objects.all()
    return measurement


def get_measurement(msrmnt_pk):
    measurement = Measurement.objects.get(pk=msrmnt_pk)
    return measurement


def update_measurement(msrmnt_pk, new_msrmnt):
    measurement = get_measurement(msrmnt_pk)
    measurement.value = new_msrmnt["value"]
    measurement.variable_id = new_msrmnt["variable_id"]
    measurement.unit = new_msrmnt["unit"]
    measurement.place = new_msrmnt["place"]
    measurement.save()
    return measurement


def create_measurement(msrmnt):
    measurement = Measurement(value=msrmnt["value"],
                              variable_id=msrmnt["variable_id"],
                              unit=msrmnt["unit"],
                              place=msrmnt["place"])

    measurement.save()
    return measurement


def delete_measurement(msrmnt_pk):
    measurement = Measurement.objects.get(pk=msrmnt_pk)
    measurement.delete()
    return measurement
