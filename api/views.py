from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import VendorSerializer,POSerializer
from vendor_app.models import vendorpagemodel,purchaseordermodel
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime
from datetime import timedelta

class Vendoradd(generics.GenericAPIView):
    def post(self,request):
        vendor_name            = self.request.data['vendor_name']
        phone_number           = self.request.data['phone_number']
        address                = self.request.data['address']
        vendor_code            = self.request.data['vendor_code']
        status                 = self.request.data['status']

        mobilenum_check = vendorpagemodel.objects.filter(phone_number = phone_number,status=0)
        if mobilenum_check.exists():
            return Response({"status":"Failure"})
        else:
            create = vendorpagemodel.objects.create(phone_number = phone_number,vendor_name = vendor_name,address=address,vendor_code=vendor_code)
            return Response({'status':"Success"})

    def get(self,request):
        vendor_list = vendorpagemodel.objects.filter(status=0)
        serializer = VendorSerializer(vendor_list, many=True)
        return Response({"status": "success","data": serializer.data})
    

class Vendordatasget(generics.GenericAPIView):
    def get(self,request,id):
        vendor_list = vendorpagemodel.objects.filter(id=id,status=0)
        serializer = VendorSerializer(vendor_list, many=True)
        return Response({"status": "success","data": serializer.data})

    def put(self,request,id):
        id_val          = self.request.data['id']
        vendor_name     = self.request.data['vendor_name']
        phone_number    = self.request.data['phone_number']
        address         = self.request.data['address']
        vendor_code     = self.request.data['vendor_code']
        status          = self.request.data['status']

        mobilenum_check = vendorpagemodel.objects.filter(~Q(id=id_val),phone_number=phone_number,status=0)

        if mobilenum_check.exists():
            return Response({"status":"Failure"})
        else:
            current_time = datetime.now()
            date_time = current_time.strftime("%d/%m/%Y %H:%M:%S")
            updated_time = datetime.strptime(date_time,"%d/%m/%Y %H:%M:%S")
            update = vendorpagemodel.objects.filter(id = id_val).update(phone_number = phone_number,vendor_name = vendor_name,address=address,vendor_code=vendor_code
                       ,updated_at = updated_time)
            return Response({'status':"Success"})

    def delete(self,request,id):
        id_val  = self.request.data['id']
        delete  = vendorpagemodel.objects.filter(id=id_val).update(status=1)
        if delete:
            return Response({"status":"Success"})
        else:
            return Response({"status":"Not Delete"})

class Purchaseorderadd(generics.GenericAPIView):
     def post(self,request):
        po_number              = self.request.data['po_number']
        vendor                 = self.request.data['vendor']
        order_date             = self.request.data['order_date']
        delivery_date          = self.request.data['delivery_date']
        items                  = self.request.data['items']
        quantity               = self.request.data['quantity']
        status                 = self.request.data['status']

        po_number_check = purchaseordermodel.objects.filter(po_number = po_number)
        if po_number_check.exists():
            return Response({"status":"Failure"})
        else:
            create = purchaseordermodel.objects.create(po_number = po_number,vendor = vendor,order_date=order_date,delivery_date=delivery_date,
                                  items=items,quantity=quantity,status=status)
            return Response({'status':"Success"})

     def get(self,request):
        po_list    = purchaseordermodel.objects.filter(delete_status=0)
        serializer = POSerializer(po_list, many=True)
        return Response({"status": "success","data": serializer.data})

class POdatasget(generics.GenericAPIView):
    def get(self,request,id):
        po_list    = purchaseordermodel.objects.filter(id=id)
        serializer = POSerializer(po_list, many=True)
        return Response({"status": "success","data": serializer.data})

    def put(self,request,id):
        id_val                 = self.request.data['id']
        po_number              = self.request.data['po_number']
        vendor                 = self.request.data['vendor']
        order_date             = self.request.data['order_date']
        delivery_date          = self.request.data['delivery_date']
        items                  = self.request.data['items']
        quantity               = self.request.data['quantity']
        status                 = self.request.data['status']
       
        po_number_check = purchaseordermodel.objects.filter(~Q(id=id_val),po_number=po_number)

        if po_number_check.exists():
            return Response({"status":"Failure"})
        else:
            current_time = datetime.now()
            date_time    = current_time.strftime("%d/%m/%Y %H:%M:%S")
            updated_time = datetime.strptime(date_time,"%d/%m/%Y %H:%M:%S")
            update       = purchaseordermodel.objects.filter(id = id_val).update(po_number = po_number,vendor = vendor,order_date=order_date,delivery_date=delivery_date,
                                items=items,quantity=quantity,issue_date =updated_time,status = status,updated_at = updated_time)

            # On Time Delivery Rate:-
            if(status == "completed"):
                total_comp_count = purchaseordermodel.objects.filter(vendor=id_val,status="completed").count()
                order_date       = purchaseordermodel.objects.filter(vendor=id_val,status="completed")
                before_de_date   = 0
                for d_rate_datas in order_date:
                    if d_rate_datas.delivery_date > d_rate_datas.issue_date:
                        before_de_date += 1
                delivery_rate_update  = vendorpagemodel.objects.filter(id = id_val).update(on_time_delivery_rate = int(before_de_date)/int(total_comp_count))  
            
                # quality Rating:-
                quality_rating_count   = purchaseordermodel.objects.filter(vendor=id_val,status="completed").count()
                quality_rating_list    = purchaseordermodel.objects.filter(vendor=id_val,status="completed")
                q_rate_total = 0
                for q_rate_list in quality_rating_list:
                    q_rate_total += q_rate_list.quality_rating
                quality_rating_avg = vendorpagemodel.objects.filter(id = id_val).update(quality_rating_avg = int(q_rate_total)/int(quality_rating_count))

                
                
            return Response({'status':"Success"})

    def delete(self,request,id):
        id_val  = self.request.data['id']
        delete  = purchaseordermodel.objects.filter(id=id_val).update(delete_status=1)
        if delete:
            return Response({"status":"Success"})
        else:
            return Response({"status":"Not Delete"})

#Acknowledge:-
class Acknowledge_update(generics.GenericAPIView):
    def get(self,request,id):
        id_val = self.request.data['id']
        current_time = datetime.now()
        date_time    = current_time.strftime("%d/%m/%Y %H:%M:%S")
        updated_time = datetime.strptime(date_time,"%d/%m/%Y %H:%M:%S")
        acknowledge_update = purchaseordermodel.objects.filter(po_number=id_val).update(acknowledged_status=1,
                                acknowledgment_date = updated_time)

        ack_complete_count        = purchaseordermodel.objects.filter(po_number=id_val,status="completed").count()
        acknowledge_complete_list = purchaseordermodel.objects.filter(po_number=id_val,status="completed",acknowledged_status = 1)
        vendor_id                 = purchaseordermodel.objects.filter(po_number=id_val).values('vendor')
        ac_values = 0
        for ac_data in acknowledge_complete_list:
            ac_date_time        = ac_data.acknowledgment_date.strftime("%d/%m/%Y")
            issue_date_time     = ac_data.issue_date.strftime("%d/%m/%Y")
            ac_date             = ac_date_time.split('/')
            issue_date_time     = issue_date_time.split('/')
            days_diff           = int(ac_date[0]) - int(issue_date_time[0])
            ac_values          += int(days_diff)
        average_res_time      = vendorpagemodel.objects.filter(id = vendor_id[0]['vendor']).update(average_response_time=int(ac_values)/int(ack_complete_count))
        refulfilemnt_count    = purchaseordermodel.objects.filter(vendor=id_val,status="completed",refulfillment_status = 2).count()
        total_po_vendor_count = purchaseordermodel.objects.filter(vendor=id_val).count()
        fulfillment_rate_val  = int(refulfilemnt_count)/int(total_po_vendor_count)
        fulfillment_rate      = vendorpagemodel.objects.filter(id = id_val).update(fulfillment_rate = fulfillment_rate_val)


        return Response({"status":"Success"})

# Performance Mtrix:-
class Performance_matrix(generics.GenericAPIView):
    def get(self,request,id):
        id_val                = self.request.data['id']
        delivery_rate         = vendorpagemodel.objects.filter(id=id_val).values('on_time_delivery_rate')
        quality_rating_avg    = vendorpagemodel.objects.filter(id=id_val).values('quality_rating_avg')
        average_response_time = vendorpagemodel.objects.filter(id=id_val).values('average_response_time')
        fulfillment_rate      = vendorpagemodel.objects.filter(id=id_val).values('fulfillment_rate')

        return Response({"on_time_delivery_rate":delivery_rate[0]['on_time_delivery_rate'],
                   "quality_rating_avg":quality_rating_avg[0]['quality_rating_avg'],
                   "average_response_time":average_response_time[0]['average_response_time'],
                   "fulfillment_rate" :fulfillment_rate[0]['fulfillment_rate']})


        







