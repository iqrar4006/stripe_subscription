from django.contrib import admin
from .models import (
    Customer,
    Monthly_plan,
    Yearly_plan,
    Purchased_plan,
    Cancelled_plan,
)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'user', 'name', 'age',
                    'locality', 'city', 'zipcode', 'state']

@admin.register(Monthly_plan)
class MonthlyPlanModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'plan_type', 'price','quality',
                    'resolution','allow_devices',]

@admin.register(Yearly_plan)
class YearlyPlanModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'plan_type', 'price','quality',
                    'resolution','allow_devices',]

@admin.register(Purchased_plan)
class PurchasedPlanModelAdmin(admin.ModelAdmin):
    list_dispaly = ['id', 'plan_type', 'price', 'allow_devices',
                    'start_date', 'end_date']

@admin.register(Cancelled_plan) 
class CancelledPlanModelAdmin(admin.ModelAdmin):
    list_dispaly =  ['id', 'plan_type', 'price', 'allow_devices',
                    'cancelled_date']

    