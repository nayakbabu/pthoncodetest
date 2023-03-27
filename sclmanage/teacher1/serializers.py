from rest_framework import serializers
from .models import TeachModel


class TeachSerial(serializers.ModelSerializer):
    test1 = serializers.SerializerMethodField()
    test2 = serializers.SerializerMethodField()

    class Meta:
        model = TeachModel
        fields = ('id', 'Teach_room', 'Teach_name', 'test1','test2')

    def get_test1(self, test_id):
        print(test_id)
        test_obj = TeachModel.objects.get(id=test_id['id'])
        return 'smruti' + str(test_obj.Teach_room)

    def get_test2(self, test_id):
        print(test_id)
        if test_id['Teach_room']:
            return False
        return True


