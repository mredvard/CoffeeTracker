from django.contrib import admin

from .models import Cup, Table, Room, Log


class CupInline(admin.TabularInline):
    model = Cup
    fields = ('completed', 'title', 'created_by', 'owl',)
    extra = 1


class LogInline(admin.TabularInline):
    model = Log
    fields = ('date_created', 'description', 'created_by')
    readonly_fields = ('date_created', )
    extra = 0


class CupAdmin(admin.ModelAdmin):
    inlines = [
        LogInline,
    ]
    list_display = (
        'id',
        'owl',
        'completed',
        'title',
        'date_created',
    )
    list_filter = (
        'completed',
        'table',
        'owl',
    )


class TableAdmin(admin.ModelAdmin):
    inlines = [
        CupInline,
    ]
    list_display = (
        'id',
        'owl',
        'title',
        'date_created',
    )
    list_filter = (
        'owl',
    )


class LogAdmin(admin.ModelAdmin):
    list_display = (
        'date_created',
        'description',
        'cup',
        'created_by'
    )
    list_filter = (
        'created_by',
        'date_created',
    )

admin.site.register(Cup, CupAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Room)
