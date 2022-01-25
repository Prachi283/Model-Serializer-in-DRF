#  ModelSerializer Validation 

from rest_framework import serializers
from .models import Employee

# # Validator in ModelSerializer Class
# def starts_with_p(value):
# 	if value[0].lower() != 'p':
# 		raise serializers.ValidationError('Position must be starts with letter-p')

class EmpSerializer(serializers.ModelSerializer):
	# name=serializers.CharField(read_only=True)
	 # name=serializers.CharField(validators=starts_with_p)
	class Meta:
		model=Employee
		fields="__all__"
		# read_only_fields=['name','emp_id','post','email']
		# extra_kwargs={'name':{'read_only':True}}
# class EmpSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Employee
# 		fields="__all__"


		#  Field-Level Validation
	def validate_emp(self,value):
		if value>=500:
			raise serializers.ValidationError('Check your Employee ID again !')
		return value 

		#  Object-Level Validation

	# def validate(self,data):
	# 	nm=data.get('name')
	# 	if nm.upper() == False:
	# 		raise serializers.ValidationError('Name must be starts with a capital letter !')
	# 	return data
