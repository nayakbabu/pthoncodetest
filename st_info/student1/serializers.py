from rest_framework import serializers
from models import SchoolModel


class Student1serial(serializers.ModelSerializer):
    test1 = serializers.SerializerMethodField()

    class Meta:
        model = SchoolModel
        fields = ('id', 'studentname', 'Attendance', 'Rollno')

        def get_test1(self, test_id):
            print(test_id)
            test_obj = SchoolModel.objects.get(id=test_id['id'])
            return 'shruti' + str(test_obj.studentname)