from django.shortcuts import render

from django.views import View
from home.models import Tool
from django.http import JsonResponse

class ToolListAPI(View):
  def get(self, request):
    tools_info = Tool.objects.values('id', 'title','description')
    context = {
      "toolList": list(tools_info)
    }
    return JsonResponse(context)