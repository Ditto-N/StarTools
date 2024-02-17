<template>
  <div v-if="show">
    <el-dialog
    model-value="true"
    title="汇率换算"
    width="550"
    @close="$emit('close')"
    draggable
    center
    >

      <el-input v-model="beforeMoney" style="width: 220px; margin-right:10px;">
        <template #append>
          <el-select v-model="beforeCurrency" style="width: 100px">
            <el-option  
              v-for="currency in currencyOptions"  
              :key="currency.value"  
              :label="currency.label"  
              :value="currency.value">  
            </el-option>  
          </el-select>
        </template>
      </el-input>

      <span>转换</span>

      <el-input v-model="afterMoney" style="width: 220px; margin-left:10px;" :disabled="true">
        <template #append>
          <el-select v-model="afterCurrency" style="width: 100px">
            <el-option  
              v-for="currency in currencyOptions"  
              :key="currency.value"  
              :label="currency.label"  
              :value="currency.value">  
            </el-option>  
          </el-select>
        </template>
      </el-input>

      <template #footer>
        <div class="dialog-footer">
          <el-button type="info" @click="reset" plain>重置</el-button>
          <el-button @click="convert" color="#626aef">换算</el-button>
        </div>
      </template>

    </el-dialog>
  </div>
</template>
<script>
import Api from '../Api'
import { ElMessage } from 'element-plus'
import { ElLoading } from 'element-plus'

export default {
  data() {
    return {
      beforeMoney: null,
      afterMoney: null,
      beforeCurrency: "",
      afterCurrency: "",
      currencyOptions: [
        { value: 'CNY', label: '人民币' },
        { value: 'EUR', label: '欧元' },
        { value: 'USD', label: '美元' },
        { value: 'JPY', label: '日元' },
        { value: 'THB', label: '泰铢' },
        { value: 'RUB', label: '卢比' }
      ]
    }
  }, 

  // 读取父组件的值，即App.vue中的show
  props: ['show'],

  // 打开对话框后的默认值
  mounted() {  
    this.beforeCurrency = this.currencyOptions[0].value
    this.afterCurrency = this.currencyOptions[0].value
  },  
  methods: {
    reset() {
      this.beforeMoney = null
      this.afterMoney = null
    },
    async convert() {
      const loadingInstance = ElLoading.service({
        lock: true,
        text: '汇率换算中',
        background: 'rgba(0, 0, 0, 0.7)',
      })

      const res = await Api.getExchangeRate(this.beforeCurrency, this.afterCurrency)

      loadingInstance.close()

      if (res.data.Information) {
        ElMessage.error(res.data.Information)
      } else {
        const rate = res.data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        this.afterMoney = this.beforeMoney * rate
      }
    }
  }
}
</script>
