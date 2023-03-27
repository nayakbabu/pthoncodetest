from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def g_data(request):
    return Response({"Student_name": "Sasmita",
                     "Roll_no": "2023S21",
                     "Class": "6th",
                     "School_name": "D.A.V. Public School"}, status=200)


@api_view(['POST'])
def b_data(request):
    return Response({"Student_name": "Rajesh",
                     "Roll_no": "2023S35",
                     "Class": "10th",
                     "School_name": "Capital High School"}, status=200)


