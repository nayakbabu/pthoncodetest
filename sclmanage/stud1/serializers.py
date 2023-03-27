from rest_framework import serializers
from .models import SclModel


class StudSerial(serializers.ModelSerializer):
    test1 = serializers.SerializerMethodField()
    test2 = serializers.SerializerMethodField()

    class Meta:
        model = SclModel
        fields = ('id', 'Stud_name', 'Stud_result', 'Stud_attend', 'test1', 'test2')

    def get_test1(self, test_id):
        print(test_id)
        test_obj = SclModel.objects.get(id=test_id['id'])
        return 'smruti' + str(test_obj.Stud_name)

    def get_test2(self, test_id):
        print(test_id)
        if test_id['Stud_attend']:
            return False
        return True


