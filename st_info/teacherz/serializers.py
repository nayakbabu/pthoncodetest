from rest_framework import serializers
from models import Teachers

class teacherserial(serializers.ModelSerializer):
    test1 = serializers.SerializerMethodField()

    class Meta:
        model = Teachers
        fields = ('id', 'staffroom_no', 'Assigned_Sub', 'test1')

        def get_test1(self, test_id):
            print(test_id)
            test_obj = Teachers.objects.get(id=test_id['id'])
            return 'shruti' + str(test_obj.staffroom)