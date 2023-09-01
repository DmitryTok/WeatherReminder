from django.contrib import admin

from weather.models import Measurement, Period, Subscription, SubType


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'period')
    search_fields = ('id', 'period')
    list_filter = ('id', 'period')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'measure')
    search_fields = ('id', 'measure')
    list_filter = ('id', 'measure')


@admin.register(SubType)
class SubTypetAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_type')
    search_fields = ('id', 'sub_type')
    list_filter = ('id', 'sub_type')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'city', 'period', 'measure', 'subscription_date', 'type_subscription')
    search_fields = ('id', 'user', 'city', 'period', 'measure', 'subscription_date', 'type_subscription')
    list_filter = ('id', 'user', 'city', 'period', 'measure', 'subscription_date', 'type_subscription')
