def views(class_list):
    view = open("views.py","w")
    view.write('from django.contrib.auth.models import User, Group \nfrom rest_framework import viewsets \nfrom mainApp.serializers import UserSerializer, GroupSerializer \n\n')
    for i in class_list:
        view.write("class " +i+ "ViewSet(viewsets.ModelViewSet):\n\tqueryset = " +i+ ".objects.all()\n\tserializer_class = " +i+ "Serializer\n\n")
    view.close()

def serial(class_list):
    serial = open("serializers.py","w")
    serial.write("from django.contrib.auth.models import *\nfrom rest_framework import serializers\nfrom .models import *\n\n")
    for i in class_list:
        serial.write("class "+ i +"Serializer(serializers.ModelSerializer):\n\tclass Meta:\n\t\tmodel = "+ i +"\n\t\tfields = '__all__'\n\n")
    serial.close()

def models(class_list):
    model = open("models.py","w")
    model.write("from django.db import models\nfrom django.contrib.auth.models import User\n\nclass CommenInfo(models.Model):\n\tarchived = models.BooleanField(default=False)\n\tcreated_at = models.DateTimeField(auto_now_add=True)\n\tupdated_at = models.DateTimeField(auto_now=True)\n\n\tdef delete(self):\n\t\tself.archived = True\n\t\tsuper().save()\n\n\tclass Meta:\n\t\tabstract = True\n")
    for i in class_list:
        model.write("class "+ i +"(CommenInfo):\n\tpass\n\n")
    model.close()

def urls(class_list):
    url = open("urls.py","w")
    url.write("from django.conf.urls import url, include\nfrom rest_framework import routers\nfrom mainApp import views\n\nrouter = routers.DefaultRouter()\n")
    for i in class_list:
        url.write("router.register(r'"+i.lower()+"', views."+ i +"ViewSet)\n")
    url.write("\n\nurlpatterns = [\n\turl(r'^', include(router.urls)),\n\turl(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))\n]\n")
    url.close()

if __name__== "__main__":
    class_list = ['CustomUser','Evaluator','Question','Quiz','Answer','Option','Submission']
    views(class_list)
    serial(class_list)
    models(class_list)
    urls(class_list)
