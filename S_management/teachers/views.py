from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def teach_sub(request):
    return Response({"Teacher_name": "Rabi",
                     "Subject_Teach": "Math"}, status=200)


@api_view(['POST'])
def teach_sub2(request):
    return Response({"Teacher_name": "Sita",
                     "Subject_Teach": "English"}, status=200)



