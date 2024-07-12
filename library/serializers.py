from rest_framework import serializers
from .models import *

# Author ---------------
class author_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'
# Book ------------------
class book_serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Member------------------
class member_serializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

# Loan----------------
class loan_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = '__all__'

class loan_return_serializer(serializers.ModelSerializer):    
    class Meta:
        model = Loan
        fields = '__all__'
        
    def validate(self, data):
        
        if any(i in data for i in ['book','member','loan_date']):
            raise serializers.ValidationError({"error":"Only return_date can be updated"})
                
        return data
        