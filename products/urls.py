from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # PRODUCT
    # =========================

    path("", views.product_list, name="product_list"),

    path("add/",
         views.add_product,
         name="add_product"),

    path("edit/<int:id>/",
         views.edit_product,
         name="edit_product"),

    path("delete/<int:id>/",
         views.delete_product,
         name="delete_product"),


    # =========================
    # SUPPLIER
    # =========================

    path("suppliers/",
         views.supplier_list,
         name="supplier_list"),

    path("suppliers/add/",
         views.add_supplier,
         name="add_supplier"),

    path("suppliers/edit/<int:id>/",
         views.edit_supplier,
         name="edit_supplier"),

    path("suppliers/delete/<int:id>/",
         views.delete_supplier,
         name="delete_supplier"),


    # =========================
    # STOCK
    # =========================

    path("stock/",
         views.stock_list,
         name="stock_list"),

    path("stock/add/",
         views.add_stock,
         name="add_stock"),

    path("stock/edit/<int:id>/",
     views.edit_stock,
     name="edit_stock"),

     path("stock/delete/<int:id>/",
     views.delete_stock,
     name="delete_stock"),
]