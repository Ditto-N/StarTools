<template>
  <div v-if="show">
    <el-dialog
    model-value="true"
    title="Wifi 破解"
    width="250"
    @close="$emit('close')"
    draggable
    center
    >
    
    <div class="search-button">
      <el-button type="info" @click="getNetwork" >搜索</el-button>
      <el-button @click="getPwd" color="#626aef">获取密码</el-button>
    </div>

    <div v-show="showSearchResult" class="search-list">
      <p>请选择要破解的WIFI</p>
      <div>
        <el-button 
          v-for="(wifi, index) in wifiList"  
          :key="index"  
          class="wifi"
          style="margin-left: 0px;"
          @click="switchWifi(index)"
        >
          {{ wifi }} 
        </el-button>
      </div>
      <p v-show="this.pwd != null">{{ this.wifi }}的密码为：{{ this.pwd }}</p>
    </div>

    </el-dialog>
  </div>
</template>

<script>
import Api from '../Api'


export default {
  data() {
    return {
      showSearchResult: false,
      wifi: null,
      wifiList: [],
      pwd: null
    }
  },

  // 读取父组件的值，即App.vue中的show
  props: ['show'],  
  methods: {
    async getNetwork() {
      this.showSearchResult = true
      const res = await Api.getNetworks()
      this.wifiList = res.data.networks
    },
    async getPwd() {
      const res = await Api.getWifiPwd(this.wifi)
      this.pwd = res.data.pwd
      console.log("wifi pwd:", this.pwd)
    },
    switchWifi(index) {
      this.wifi = this.wifiList[index]
    }
  }
}

</script>

<style>
.search-button {
  display: flex;
  justify-content: center;
}

.search-list {
  text-align: center;
  margin-top: 20px;
  border: 1px solid #000;  
  box-shadow: 2px 4px 4px 4px rgba(65, 63, 63, 0.75);  
}

.wifi {
  border: 0.5px solid #000;
  width: 100%;
}


</style>