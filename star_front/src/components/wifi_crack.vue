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
    </div>

    </el-dialog>
  </div>
</template>

<script>
import Api from '../Api'


export default {
  data() {
    return {
      showSearchResult: true,
      wifi: null
    }
  },

  // 读取父组件的值，即App.vue中的show
  props: ['show'],  
  methods: {
    async getNetwork() {
      this.showSearchResult = true
      const res = await Api.getNetworks()
      console.log("networks:", res.data)
    },
    async getPwd() {
      // const res = await Api.getWifiPwd(this.wifi)
      // console.log("wifi pwd:", res.data)
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
  display: flex;
  justify-content: center;
  margin-top: 20px;
  border: 1px solid #000;  
  box-shadow: 2px 4px 4px 4px rgba(65, 63, 63, 0.75);  
}

</style>