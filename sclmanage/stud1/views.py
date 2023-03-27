import json

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import SclModel
from .serializers import StudSerial


class StudManage(GenericAPIView):

    @staticmethod
    def _serialize_test(test_inst):
        return StudSerial(test_inst, many=True).data

    def get(self, request):
        rec = SclModel.objects.filter(Stud_result=True).values()
        return Response({'Output': self._serialize_test(rec)}, status=200)

    def post(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        x = SclModel.objects.create(Stud_name=json_data['test1'], Stud_result=True, Stud_attend=json_data['test2'], Stud_scl=json_data['test3'])
        return Response({'Output': x.id}, status=200)

    def patch(self, request):
        json_data = json.loads(request.body)
        rec = SclModel.objects.get(id=json_data['id'])
        rec.Stud_name = json_data['test1']
        rec.save()
        return Response({'output': str(rec.id) + " is successfully updated."}, status=200)

    def delete(self, request):
        json_data = json.loads(request.body)
        rec = SclModel.objects.get(id=json_data['id'])
        rec.delete()
        return Response({'message': rec.Stud_name + ' is successfully deleted'}, status=200)

