from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from.models import MusicClass
from.serializers import SerialMusic


class MusicData(GenericAPIView):
    
    @staticmethod
    def _serialize_test(test_inst):
        return SerialMusic(test_inst, many=True).data

    def get(self, request):
        rec = MusicClass.objects.filter().values()
        return Response({'output': self._serialize_test(rec)}, status=200)

    def post(self, request):
        MusicClass.objects.create(Song_title='Rabba', Song_Favorite=True, Singer_Name='Lata', Music_logo= 41)
        return Response({'Singer: B.Park'}, status=200)

    def patch(self, request):
        return Response({'Music_Director: Arko'}, status=200)

    def delete(self, request):
        return Response({'Movie: kesari'}, status=200)
