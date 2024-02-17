from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import subprocess

# Create your views here.

class WifiAPI(View):
  def get(self, request):
    command = "netsh wlan show networks mode=bssid"  
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
  
    # 解析输出以获取网络列表  
    networks = []  
    ssid = None
    
    # 检查命令是否成功执行  
    # if result.returncode != 0:  
    for line in result.stdout.split('\n'):  
      if line.startswith("SSID"):  
        # 提取SSID  
        ssid = line.split(":")[1].strip()  
        if ssid:  
          networks.append(ssid)  

    context = {
      "networks": networks
    }
    return JsonResponse(context)

