from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

# Aoutor's Class -------

class author(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = author_serializer

class del_update_author(generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Author.objects.all().order_by('-id')
    serializer_class = author_serializer

@api_view(['GET'])
def auth_detail(request,id):
    
    author = get_object_or_404(Author,id=id)
    books = Book.objects.filter(author=id)
    
    ser_auth = author_serializer(author)
    ser_book = book_serializer(books,many=True)
    
    return Response({"Author":ser_auth.data,"Books":ser_book.data})
    
    
    
    # if ser_auth.is_valid():
    #     ser_book = book_serializer(book)
    #     if ser_auth.is_valid():
    #         return Response({"Author":ser_auth.data,"Books":ser_book.data})
    #     else:
    #         return Response({
    #             "Author":ser_auth.data,
    #             "Books":{"Message":"Somethig went Wrong when loading books","Error":ser_book.errors}
    #         })
            
    # else:
    #     return Response({"Message":"Somethig went Wrong","Error":ser_auth.errors})
    
    
    


# Book's Class-------------
class book(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = book_serializer

# Member -------------------
class member(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = member_serializer

@api_view(['GET'])
def member_datail(request,id):
    # id = request.data['id']
    member = get_object_or_404(Member,id=id)
    ser_data = member_serializer(member)
    
    loan = Loan.objects.filter(member = id,return_date = None)
    ser_loan = loan_serializer(loan, many=True)
    
    returned_book = Loan.objects.filter(member = id,return_date__isnull = False)
    ser_returned_book = loan_serializer(returned_book, many = True)
    
    return Response({"member":ser_data.data, "Borrowed Books":ser_loan.data, "Returned Books": ser_returned_book.data})
    


# Loan's Clss ----------
class borrow_book(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = loan_serializer

@api_view(['PATCH'])
def return_book(request,id):
    loan = get_object_or_404(Loan,id=id)
    
    if loan.return_date != None:
        ser_loan = loan_return_serializer(loan)
        return Response({"Massege":"This Book is already Returned","detail":ser_loan.data})
    
    ser_loan = loan_return_serializer(loan,data= request.data, partial = True)
    
    if ser_loan.is_valid():
        ser_loan.save()
        return Response(ser_loan.data)
    else:
        return Response({"Massage":"Something Went Wrong!","error":ser_loan.errors})