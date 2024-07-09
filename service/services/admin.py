from django.contrib import admin

from .models import Service, Plan, Subscription


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['plan_type', 'discount_percent']
    search_fields = ['plan_type']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['client', 'service', 'plan']
    search_fields = ['client__company_name', 'service__name', 'plan__plan_type']
