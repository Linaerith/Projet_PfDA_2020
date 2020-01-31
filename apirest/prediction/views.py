from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from prediction.models import Event_Log
from prediction.serializers import EventSerializer


def predict_time_before_resolution(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ['active', 'reassignment_count', 'reopen_count', 'sys_mod_count',
       'made_sla', 'knowledge', 'u_priority_confirmation', 'sys_updated_by',
       'category', 'subcategory', 'u_symptom', 'impact', 'urgency', 'priority',
       'contact_type_Direct_opening', 'contact_type_Email', 'contact_type_IVR',
       'contact_type_Phone', 'contact_type_Self_service', 'incident_state_100',
       'incident_state_Active', 'incident_state_Awaiting_Evidence',
       'incident_state_Awaiting_Problem', 'incident_state_Awaiting_User_Info',
       'incident_state_Awaiting_Vendor', 'incident_state_Closed',
       'incident_state_New', 'incident_state_Resolved', 'isoWeekDay_1', 'isoWeekDay_2',
       'isoWeekDay_3', 'isoWeekDay_4', 'isoWeekDay_5', 'isoWeekDay_6',
       'isoWeekDay_7', 'hour', 'month']
    path_to_model   = "../jupyter/model_RF.pkl"
    path_for_scaler = "../jupyter/scaler.pkl"
    import numpy as np
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    unscaled_data   = np.array(unscaled_data).reshape(1,-1)
    model           = joblib.load(path_to_model)
    time_before_resolution = model.predict(unscaled_data)
    return time_before_resolution


@csrf_exempt
def predict(request):
    """
    Renvoie un event avec le temps de resolution restant completee
    (Attend un temps innexistante)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = EventSerializer(data=data)
        if serializer.is_valid():
            data["time_before_resolution"]        = predict_time_before_resolution(data)
            serializer          = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)



@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = Event_Log.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event_Log.objects.get(pk=pk)
    except Event_Log.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)
