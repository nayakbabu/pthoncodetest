from rest_framework import serializers
from.models import MusicClass


class SerialMusic(serializers.ModelSerializer):
    song1 = serializers.SerializerMethodField()
    song2 = serializers.SerializerMethodField()

    class Meta:
        model = MusicClass
        fields = ('id', 'Song_title', 'Song_Favorite', 'Singer_Name', 'Music_logo', 'song1', 'song2')

    def get_song1(self, song_id):
        fld_obj = MusicClass.objects.get(id=song_id['id'])
        return 'sounds' + str(song_id['Song_title'])

    def get_song2(self, song_id):
        if song_id['Singer_Name']:
            return False
        return True


