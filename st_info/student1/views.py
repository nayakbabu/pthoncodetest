import json


from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import SchoolModel
from .serializers import Student1serial


class StudentRecords(GenericAPIView):

    @staticmethod
    def _serialize_test(test_inst):
        return Student1serial(test_inst, many=True).data

    def get(self, request):
        rec = SchoolModel.objects.filter(Attendance=True).values()
        return Response({'output': self._serialize_test(rec)}, status=200)

    def post(self, request):
        json_data = json.loads(request.body)
        print(json_data)
        SchoolModel.objects.create(studentname=json_data['test1'], Attendance=True, Rollno=json_data['test2']).values()
        return Response({'studentname': 'Nishan Dey',
                     'Rollno': '88',
                     'class': '12',
                     'contact': '9178493645',
                     'Attendance': '78%'}, status=200)

    def patch(self, request):
        json_data = json.loads(request.body)
        rec = SchoolModel.objects.get(id=json_data['id'])
        rec.studentname = json_data['test1']
        rec.save()
        return Response({'message': 'Am confident and disciplined'}, status=200)

    def delete(self, request):
        json_data = json.loads(request.body)
        rec = SchoolModel.objects.get(id=json_data['id'])
        rec.delete()
        return Response({'message': 'both are polite'}, status=200)
