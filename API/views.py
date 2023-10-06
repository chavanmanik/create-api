from .models import Student

from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
    
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer    
    
# class StudentRetrieveAPIView(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer     
    
# class StudentUpdateAPIView(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer     
    
    
# class StudentDestroyAPIView(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer     
        
   
class StudentListcreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer     
                
                
   
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer     
                                