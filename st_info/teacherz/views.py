import json
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from.models import Teachers
from.serializers import teacherserial


class Teacher_info(GenericAPIView):

    @staticmethod
    def _serialize_test(test_inst):
        return teacherserial(test_inst, many=True).data

    def get(self, request):
        rec = Teachers.objects.filter(Assigned_Sub=True).values()
        return Response({'Output': self._serialize_test(rec)},  status=200)

    def post(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        Teachers.objects.create(Teachername=json_data['test1'], Assigned_sub='True', Staffroom_no=json_data['test2']).values()
        return Response({'message': 'Am supposed to take classes from 8th to 10th'}, status=200)
    def patch(self, request):
        json_data = json.loads(request.body)
        rec = Teachers.objects.get(id=json_data['id'])
        rec.Assigned_sub = json_data['test1']
        rec.save()
        return Response({'message': 'Both present in the same premises'}, status=200)
