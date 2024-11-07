
from django.urls import path
from .views import  RetrieveCategory,ListCategory,UpdateCategory,CreateCategory,DeleteCategory, ProductList,ProductCreate,DeleteProduct,UpdateProduct,RetrieveProduct,UserRegisterApi,LoginApiView
urlpatterns = [



    # category related urls
    path('categories',ListCategory.as_view()),
    path('category/<str:name>',RetrieveCategory.as_view()),
    path('category/update/<str:name>',UpdateCategory.as_view()),
    path('categories/create',CreateCategory.as_view()),
    path('category/delete/<str:name>',DeleteCategory.as_view()),

    #Product related urls

    path('products',ProductList.as_view()),
    path('products/create',ProductCreate.as_view()),
    path('products/<int:id>',RetrieveProduct.as_view()),
    path('products/update/<int:id>',UpdateProduct.as_view()),
    path('products/delete/<int:id>',DeleteProduct.as_view()),


    #user reltated urls
    path('api/register',UserRegisterApi.as_view()),
    path('api/login',LoginApiView.as_view())
]
