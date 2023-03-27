import json

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import TeachModel
from .serializers import TeachSerial


class TeacherManage(GenericAPIView):

    @staticmethod
    def _serialize_test(test_inst):
        return TeachSerial(test_inst, many=True).data

    def get(self, request):
        rec = TeachModel.objects.filter(Teach_room=12).values()
        return Response({'Output': self._serialize_test(rec)}, status=200)

    def post(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        TeachModel.objects.create(Teach_name=json_data['test1'], Teach_room=json_data['test2'], Teach_sub=json_data['test3'])
        return Response({'Name': 'Garima',
                         'Room_no': 6,
                         'Sub_teach': 'Hindi'}, status=200)

    def patch(self, request):
        json_data = json.loads(request.body)
        rec =TeachModel.objects.get(id=json_data['id'])
        rec.TeachModel = json_data['test1']
        rec.save()
        return Response({'Name': 'Ashok',
                         'Room_no': 2,
                         'Sub_teach': 'Physics'}, status=200)

    def delete(self, request):
        json_data = json.loads(request.body)
        rec = TeachModel.objects. get(id=json_data['id'])
        rec.delete()
        return Response({'message': rec.Teach_name + 'is successfully deleted'}, status=200)





