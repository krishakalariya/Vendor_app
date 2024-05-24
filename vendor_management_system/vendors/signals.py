from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import PurchaseOrder, Vendor, VendorPerformanceHistory
from django.db.models import Avg, Count, F


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, **kwargs):
    vendor = instance.vendor

    # Calculate On-Time Delivery Rate
    total_completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    if total_completed_orders > 0:
        on_time_deliveries = PurchaseOrder.objects.filter(
            vendor=vendor,
            status='completed',
            delivery_date__lte=F('delivery_date')
        ).count()
        vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100

    # Calculate Quality Rating Average
    quality_ratings = PurchaseOrder.objects.filter(vendor=vendor, status='completed').aggregate(Avg('quality_rating'))
    vendor.quality_rating_avg = quality_ratings['quality_rating__avg'] or 0.0

    # Calculate Average Response Time
    response_times = PurchaseOrder.objects.filter(vendor=vendor).exclude(acknowledgment_date__isnull=True).annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    ).aggregate(Avg('response_time'))
    vendor.average_response_time = response_times['response_time__avg'].total_seconds() / 3600 if response_times[
        'response_time__avg'] else 0.0

    # Calculate Fulfillment Rate
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    vendor.fulfillment_rate = (fulfilled_orders / total_orders) * 100 if total_orders > 0 else 0.0

    vendor.save()

    # Create vendor performance history
    VendorPerformanceHistory.objects.create(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate,
    )
