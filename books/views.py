import re
from turtle import title
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render ,redirect
import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request 
from .models import Book , Review,Category1,Category2,Category3
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json
import math




class BooksListView(ListView):
    model = Book
    template_name = 'list.html'
   



def index(request):
    # seo clicks
    mv=[]
    mostview=Book.objects.filter(seoclicks__gte =2).order_by('seoclicks').reverse()

    p=Paginator(mostview,6)
    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)

    n = 3
    nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
    mv.append([page, range(1, nSlides), nSlides])







    
    allProds = []

    products = None
    categories1=Category1.objects.all()
   

    categoryID = request.GET.get('category')

    if categoryID:
        products = Book.get_all_products_by_categoryid(categoryID)
    else:
        products = Book.objects.all()

    # categories2
    categories2=Category2.objects.all()
    categoryID2 = request.GET.get('category2')

    if categoryID2:
        products = Book.get_all_products_by_categoryid2(categoryID2)

    # category3
    categories3=Category3.objects.all()
    categoryID3 = request.GET.get('category3')

    if categoryID3:
        products = Book.get_all_products_by_categoryid3(categoryID3)

    n = 3
    nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
    allProds.append([products, range(1, nSlides), nSlides])
    params={ 'allProds':allProds,'categories1':categories1,'categories2':categories2,'categories3':categories3,'mostview':mostview,'mv':mv ,'page':page}
    return render(request,'list.html', params)


class SearchResultsListView(ListView):
	model = Book
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Book.objects.filter(
		Q(title__icontains=query) | Q(author__icontains=query)
		)



def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is alerady in used')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is alerady in used')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name , username=username, password=password, email=email)
                user.save()
                return redirect('signin')
        else:
            messages.info(request, 'Confirm password not matching')
            return redirect('register')
           
    return render(request,'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
             messages.info(request, 'Your username or password is incorrect')
             return redirect('signin')
    return  render(request,'signIn.html')

def review_rating(request,myid):
     if request.method == 'GET':
         current_datetime = datetime.datetime.now()  
         title=myid
         comment= request.GET.get('comment')
         user= request.GET.get('user')
         rating=request.GET.get('rating')
         created=current_datetime.strftime("%b %d, %Y | %H:%M")
         Review(title=title, comment=comment,user=user,created=created,rating=rating).save()
         return redirect(f'/productview/{title}#comment')




def productview(request,myid):
    click=Book.objects.all().filter(id=myid).values_list('seoclicks',flat=True)
    click=list(click)
    click=click[0]
    click +=1
    Book.objects.filter(id=myid).update(seoclicks=click)

    


    book=Book.objects.filter(id=myid)
    review=Review.objects.all().filter(title=myid)
    review=list(review)
    review.reverse()
    p=Paginator(review,5)
    TotalPage=p.num_pages
    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)

    # rating
    rating=Review.objects.all().filter(title=myid).values_list('rating',flat=True)
    rating=list(rating)
    def calculate_star_rating(ratings):
        stars = rating
        return round(sum(list(map(lambda a,b: a*b, stars, ratings))) / sum(ratings), 2)
    ratings = [100,200,300,400,500]
    star=calculate_star_rating(ratings)

    # comment
    lencomment=Review.objects.all().filter(title=myid).values_list('comment',flat=True)
    lencomment=list(lencomment)
    lencomment=len(lencomment)

    # similar product category1 
    product=Book.objects.filter(id=myid)
    Category1=Book.objects.values('category1')
    cats = {item['category1'] for item in Category1}
    products=Book.objects.all()
    allProds = []
    for cat in cats:
            prod = Book.objects.filter(category1=cat)
            n = 3
            nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
            allProds.append([prod, range(1, nSlides), nSlides])

        
    # similar product category2 
    product=Book.objects.filter(id=myid)
    Category2=Book.objects.values('category2')
    cats = {item['category2'] for item in Category2}
    products=Book.objects.all()
    allProds2 = []
    for cat in cats:
            prod = Book.objects.filter(category2=cat)
            n = 3
            nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
            allProds2.append([prod, range(1, nSlides), nSlides])

    # similar product category 3
    product=Book.objects.filter(id=myid)
    Category3=Book.objects.values('category3')
    cats = {item['category3'] for item in Category3}
    products=Book.objects.all()
    allProds3 = []
    for cat in cats:
            prod = Book.objects.filter(category3=cat)
            n = 3
            nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
            allProds3.append([prod, range(1, nSlides), nSlides])


    
    
    
    
    params={'product':product[0], 'Category1':Category1,'products':products, 'allProds':allProds ,'allProds2':allProds2 ,'allProds3':allProds3,'books':book,'reviews':page,'stars':star,'lencoments':lencomment,'TotalPage':TotalPage}
    return render(request,'productview.html',params)

