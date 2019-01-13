from django.contrib.auth.models import User
from django.db import transaction

from voting.models import .


@transaction.atomic
def create_certificates():
    print("Creando CERTIFICATES")
    print("---\n\n")

    # ---

    pilot = Pilot.objects.get(identifier="78458961U")
    certificate = Certificate(pilot=pilot, code="0874521478989985652", title="Cerfitificado médico",
                              exp_date="2010-05-01", company="Wings Medical")
    certificate.save()

    pilot = Pilot.objects.get(identifier="87454478P")
    certificate = Certificate(pilot=pilot, code="7412147847854123210", title="Licencia de piloto privado PPL",
                              exp_date="2008-10-13", company="Academic Pilot New York")
    certificate.save()

    pilot = Pilot.objects.get(identifier="22477451U")
    certificate = Certificate(pilot=pilot, code="0021410032059017820", title="Licencia de piloto privado PPL",
                              exp_date="2014-08-27", company="Academia de pilotos privados Santander")
    certificate.save()

    pilot = Pilot.objects.get(identifier="75321489A")
    certificate = Certificate(pilot=pilot, code="0000320005018745695", title="Cerfiticado de control de vuelo",
                              exp_date="2015-10-04", company="Universidad Espacial de Madrid")
    certificate.save()

    # ---

    certificates = Certificate.objects.all()
    print("Certificados creados correctamente: Número de certificados ", len(certificates))
    print("----------------\n\n")