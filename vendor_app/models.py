from django.db import models
from django.utils import timezone
from jsonfield import JSONField


class vendorpagemodel(models.Model):
    id                      = models.AutoField(primary_key =True)
    vendor_name             = models.CharField(max_length = 200, blank=True, null=True)
    phone_number            = models.CharField(max_length = 10, blank=True, null=True)
    address                 = models.CharField(max_length = 200, blank=True, null=True)
    vendor_code             = models.CharField(max_length = 200, blank=True, null=True)
    on_time_delivery_rate   = models.FloatField(default = 0, blank=True, null=True)
    quality_rating_avg      = models.FloatField(default = 0, blank=True, null=True)
    average_response_time   = models.FloatField(default = 0, blank=True, null=True)
    fulfillment_rate        = models.FloatField(default = 0, blank=True, null=True)
    status                  = models.IntegerField(default = 0, blank=True, null=True) #(0 - active,1-inactive(delete))
    completed_status_count  = models.IntegerField(default = 0, blank=True, null=True)
    created_at              = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at              = models.DateTimeField(blank=True, null=True)
     
    class Meta:
        db_table = 'vendor'



class purchaseordermodel(models.Model):
    id                  = models.AutoField(primary_key =True)
    po_number           = models.CharField(max_length = 200, blank=True, null=True)
    vendor              = models.IntegerField(default = 0, blank=True, null=True)
    order_date          = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    delivery_date       = models.DateTimeField(blank=True, null=True)
    items               = models.JSONField(default=dict)
    quantity            = models.IntegerField(default = 0, blank=True, null=True)
    status              = models.CharField(max_length = 200, blank=True, null=True)
    delete_status       = models.IntegerField(default = 0, blank=True, null=True)
    quality_rating      = models.FloatField(default = 0, blank=True, null=True)
    issue_date          = models.DateTimeField(blank=True, null=True)
    acknowledged_status = models.IntegerField(default = 0, blank=True, null=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)
    refulfillment_status= models.IntegerField(default = 0, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at          = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Purchase_Order'