from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import TestData, Patient


class TestDataAdmin(admin.ModelAdmin):
    class Media:
        js = ('admin/js/vendor/jquery/jquery.js', 'admin/js/jquery.init.js', 'admin/js/actions.js',)
        css = {
            'all': ('admin/css/vendor/vendor.css', 'admin/css/base.css', 'admin/css/dashboard.css',)
        }

    def response_add(self, request, obj, post_url_continue=None):
        # Redirect to the home page after adding a new test data entry
        return HttpResponseRedirect(reverse('home'))

admin.site.register(TestData, TestDataAdmin)


admin.site.register(Patient)
