from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pasien
import uuid


class PasienList(APIView):
    def get(self, request):
        payload = []
        patients = Pasien.objects.all().order_by('-id')
        for p in patients:
            h = {
                'id': p.id,
                'name': p.name,
                'date': p.date,
                'gender': p.gender,
                'nik': p.nik,
                'address': p.address,
                'telp': p.telp,
                'bpjs': p.bpjs,
                'medical_record': p.medical_record
            }
            payload.append(h)
        return Response(payload)


class GetPasienDetail(APIView):
    def get(self, request, medical):
        try:
            p = Pasien.objects.get(medical_record=medical)
            h = {
                'id': p.id,
                'name': p.name,
                'date': p.date,
                'gender': p.gender,
                'nik': p.nik,
                'address': p.address,
                'telp': p.telp,
                'bpjs': p.bpjs,
                'medical_record': p.medical_record
            }
            return Response({
                'status': 'OK',
                **h
            })
        except Exception as e:
            return Response({
                'status': 'FAIL',
                'reason': str(e)
            })


class ModifyPasien(APIView):
    def post(self, request):
        medical_record = str(uuid.uuid4())[0:8]
        d = request.data
        name = d['name']
        date = d['date']
        gender = d['gender']
        nik = d['nik']
        address = d['address']
        telp = d['telp']
        bpjs = d['bpjs']
        pasien = Pasien.objects.create(name=name, date=date, gender=gender, nik=nik, address=address, telp=telp,
                                       bpjs=bpjs, medical_record=medical_record, user=request.user)
        pasien.save()
        return Response({'status': 'OK'})

    def put(self, request):
        d = request.data
        id = d['id']
        name = d['name']
        date = d['date']
        gender = d['gender']
        nik = d['nik']
        address = d['address']
        telp = d['telp']
        bpjs = d['bpjs']
        try:
            pasien = Pasien.objects.get(id=id)
            pasien.name = name
            pasien.date = date
            pasien.gender = gender
            pasien.nik = nik
            pasien.address = address
            pasien.telp = telp
            pasien.bpjs = bpjs
            pasien.save()
            return Response({'status': 'OK'})
        except Exception as e:
            return Response({'status': 'FAIL', 'reason': str(e)})
