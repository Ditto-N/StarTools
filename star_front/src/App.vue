<template>
  <el-container>
    <el-header>StartTool</el-header>
    <el-main style="display: flex; justify-content:flex-start">
      <div class="tool-box">
        <el-button id="tool-button" @click="showUnitConvertBox=true"><font-awesome-icon class="icon" :icon="['fas', 'recycle']" size="3x"/></el-button>
        <p style="color:#b8b6c1;">单位转换器</p>
        <unit-convert :show.sync="showUnitConvertBox" @close="showUnitConvertBox=false"></unit-convert>
      </div>
      <div class="tool-box">
        <el-button id="tool-button" @click="showExchangeRateConvertBox=true"><font-awesome-icon class="icon" :icon="['fas', 'coins']" size="3x"/></el-button>
        <p style="color:#b8b6c1;">汇率换算</p>
        <exchange-rate-convert :show.sync="showExchangeRateConvertBox" @close="showExchangeRateConvertBox=false"></exchange-rate-convert>
      </div>
      <div class="tool-box">
        <el-button id="tool-button" @click="showWifiCrackBox=true"><font-awesome-icon class="icon" :icon="['fas', 'wifi']" size="3x"/></el-button>
        <p style="color:#b8b6c1;">WIFI 破解</p>
        <wifi-crack :show.sync="showWifiCrackBox" @close="showWifiCrackBox=false"></wifi-crack>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import UnitConvert from './components/unit_convert.vue'
import ExchangeRateConvert from './components/exchange_rate_convert.vue'
import WifiCrack from './components/wifi_crack.vue'

export default {
  name: 'App',
  components: {  
    UnitConvert,
    ExchangeRateConvert,
    WifiCrack
  },
  data() {
    return {
      showUnitConvertBox: false,
      showExchangeRateConvertBox: false,
      showWifiCrackBox: false
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* margin-top: 60px; */
}

body {
  overflow: hidden;   /* 隐藏滑动条 */
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #fff0d0;
  background-color: #2b3763;
}

.tool-box {
  width: 100px;
  height: 100px;
  margin-top: 20px;
}

#tool-button {
  background-color: transparent;
  border-color: transparent;
}

.icon {
  color: #977d9a;
}

.icon:hover {
  color: #fff0d0;
}

.el-header {
  display: flex; 
  height: 200px;
  background-color: #6b60a0;
  text-align: left;
  align-items: center;
  font-size: 24px;
  border-radius: 5px;
  color:#fff0d0;
}

.el-main {
  display: flex;
  justify-content: space-between;
  height: 100%;
  color:#fff0d0;
}

</style>
