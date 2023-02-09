from variables.models import Variable

from ..models import Measurement


# ----------------------------------------------------------------------------------------------------------------#
# TODO: hacer post put(patch) y delete
# TODO: Include all of the attributes for measurment object in the constructor, you can get them from the msrmnt.
# TODO: Do not forget to make the matching postman tests
# -----------------------------------------------------------------------------------------------------------------#

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement


def get_measurement(msrmnt_pk):
    measurement = Measurement.objects.get(pk=msrmnt_pk)
    return measurement


def update_measurement(msrmnt_pk, new_msrmnt):
    measurement = get_measurement(msrmnt_pk)
    measurement.value = new_msrmnt["value"]
    measurement.save()
    return measurement


def create_measurement(msrmnt):
    measurement = Measurement(value=msrmnt["value"], variable_id=msrmnt["variable_id"])
    measurement.save()
    return measurement
