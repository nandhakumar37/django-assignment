from rest_framework import serializers
from vendor_app.models import vendorpagemodel,purchaseordermodel

class VendorSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = vendorpagemodel
		fields = ('vendor_name', 'phone_number','address','vendor_code','on_time_delivery_rate','quality_rating_avg',
			                'average_response_time','fulfillment_rate','status','created_at','updated_at')


class POSerializer(serializers.ModelSerializer):
	# specify model and fields
	class Meta:
		model = purchaseordermodel
		fields = ('po_number', 'vendor','order_date','delivery_date','items','quantity',
			                'status','quality_rating')