from django.contrib import admin
from django.utils.html import format_html
from django.utils.timesince import timesince
from .models import Inquiry

# Customizing the Admin Header to match your brand
admin.site.site_header = "Edward Sunga | Systems Control"
admin.site.site_title = "Architect Portal"
admin.site.index_title = "Inquiry Management Infrastructure"

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    # 1. Custom List Display for high-end visibility
    list_display = ('sender_profile', 'status_badge', 'message_snippet', 'time_received')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    list_per_page = 20
    
    # 2. Bulk Actions
    actions = ['mark_as_read', 'mark_as_unread']

    # 3. Enhanced Fieldsets
    fieldsets = (
        ('Lead Intelligence', {
            'fields': ('name', 'email'),
            'description': 'Primary contact data for the potential client.'
        }),
        ('Project Requirements', {
            'fields': ('message',),
            'classes': ('wide',),
        }),
        ('System Metadata', {
            'fields': ('created_at', 'is_read'),
        }),
    )

    # --- CUSTOM DISPLAY METHODS ---

    def sender_profile(self, obj):
        """Displays name and email in a clean format"""
        return format_html(
            '<div style="line-height:1.2;">'
            '<strong style="color:#0563af;">{}</strong><br>'
            '<small style="color:#6c757d;">{}</small>'
            '</div>',
            obj.name, obj.email
        )
    sender_profile.short_description = "Prospect"

    def status_badge(self, obj):
        """Displays a professional Blue/White status badge"""
        if obj.is_read:
            return format_html(
                '<span style="padding: 4px 10px; background: #eef7ff; color: #0563af; '
                'border: 1px solid #0563af; border-radius: 50px; font-size: 10px; '
                'font-weight: 700; text-transform: uppercase;">Reviewed</span>'
            )
        return format_html(
            '<span style="padding: 4px 10px; background: #0563af; color: #fff; '
            'border-radius: 50px; font-size: 10px; font-weight: 700; '
            'text-transform: uppercase;">New Inquiry</span>'
        )
    status_badge.short_description = "Status"

    def message_snippet(self, obj):
        """Truncates the message for the list view"""
        if len(obj.message) > 60:
            return f"{obj.message[:60]}..."
        return obj.message
    message_snippet.short_description = "Project Brief Snippet"

    def time_received(self, obj):
        """Shows how long ago the message arrived"""
        return f"{timesince(obj.created_at)} ago"
    time_received.short_description = "Received"

    # --- CUSTOM ACTIONS ---

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected inquiries marked as reviewed.")
    mark_as_read.short_description = "Mark selected as Reviewed"

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, "Selected inquiries marked as New.")
    mark_as_unread.short_description = "Mark selected as New"