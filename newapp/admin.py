from django.contrib import admin
from .models import User, Country, State, City, UserProfile, PlantCategory, Plant, ProductCart, OrderTable, \
    PaymentTable, Feedback, Contactus


# Register your models here.
@admin.register(User)
class showUser(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Password', 'Date_Joined')


@admin.register(Country)
class showCountry(admin.ModelAdmin):
    list_display = ('Name',)


@admin.register(State)
class showState(admin.ModelAdmin):
    list_display = ('Country', 'Name')


@admin.register(City)
class showCity(admin.ModelAdmin):
    list_display = ('State', 'Name')


@admin.register(UserProfile)
class ShowUserProfile(admin.ModelAdmin):  # Capitalized class name for consistency
    list_display = ('User', 'BOD', 'Address', 'Phone_No', 'Image')  # Added commas between fields


@admin.register(PlantCategory)
class showPlantCategory(admin.ModelAdmin):
    list_display = ('CAT_Name', 'Description')


@admin.register(Plant)
class showPlant(admin.ModelAdmin):
    list_display = ('User', 'Category', 'Price', 'Description', 'Stock', 'Image')


@admin.register(ProductCart)
class showProductCart(admin.ModelAdmin):
    list_display = ('User', 'Plant', 'Price', 'Quantity', 'Order_ID', 'Order_Status')


@admin.register(OrderTable)
class showOrderTable(admin.ModelAdmin):
    list_display = ('User', 'Plant', 'Quantity', 'Total_Price', 'Order_Date', 'Delivery_Date', 'Status')


@admin.register(PaymentTable)
class showPaymentTable(admin.ModelAdmin):
    list_display = ('User', 'Booking', 'Amount', 'Payment_Mode', 'Payment_Status', 'Payment_Date')


@admin.register(Feedback)
class showFeedback(admin.ModelAdmin):
    list_display = ('User', 'Plant', 'Rating', 'Comment', 'Review_Date')


@admin.register(Contactus)
class showContactus(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Subject', 'Message', 'Phone', 'Created_At')
