from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

import subprocess

import pywifi

# Create your views here.

class WifiAPI(View):
  def get(self, request, *args, **kwargs):
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

    # wifi=pywifi.PyWiFi() 
    # ifaces=wifi.interfaces()[0]
    # print("======ifaces.name: ",ifaces.name())  
    # ifaces.scan()  
    # # time.sleep(3)   
    # result = ifaces.scan_results()
    # mac_list = []

    # for data in result:
    #   mac_list.append(data.bssid)

    return JsonResponse(context)
  
  # 未完成wifi密码破解功能
  def post(self, request, *args, **kwargs):
    SSID = request.GET.get('ssid')
    context = {
      "sss": "112"
    }
    print("aaa")
    return JsonResponse(context)

