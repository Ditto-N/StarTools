<template>
  <div v-if="show">
    <el-dialog
      model-value="true"
      title="单位转换器"
      width="550"
      @close="$emit('close')"
      draggable
      center
    >
      <div style="margin-bottom: 20px;display:flex;justify-content: space-around;">
        <p>单位类型：</p>
        <el-radio-group v-model="type">
          <el-radio label="length">长度</el-radio>
          <el-radio label="area">面积</el-radio>
          <el-radio label="volume">体积</el-radio>
          <el-radio label="weight">重量</el-radio>
          <el-radio label="time">时间</el-radio>
        </el-radio-group><br/>
      </div>

      <el-input v-model="beforeNumber" style="width: 220px; margin-right:10px;">
        <template #append>
          <el-select v-model="beforeUnit" style="width: 100px">
            <el-option  
              v-for="unit in unitOptions"  
              :key="unit.value"  
              :label="unit.label"  
              :value="unit.value">  
            </el-option>  
          </el-select>
        </template>
      </el-input>

      <span>转换</span>

      <el-input v-model="afterNumber" style="width: 220px; margin-left:10px;" :disabled="true">
        <template #append>
          <el-select v-model="afterUnit" style="width: 100px">
            <el-option  
              v-for="unit in unitOptions"  
              :key="unit.value"  
              :label="unit.label"  
              :value="unit.value">  
            </el-option>  
          </el-select>
        </template>
      </el-input>

      <template #footer>
        <div class="dialog-footer">
          <el-button type="info" @click="reset" plain>重置</el-button>
          <el-button @click="convert" color="#626aef">转换</el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script>

export default {
  data() {
    return {
      beforeNumber: null, 
      afterNumber: null,
      type: "",
      beforeUnit: "",
      afterUnit: "",
      unitOptions: [],
      allOptions: {
        "length": [
          { value: 'm', label: '米' },  
          { value: 'km', label: '千米' }
        ],
        "area": [
          { value: 'sm', label: '平方米' },  
          { value: 'skm', label: '平方千米' }
        ],
        "volume": [
          { value: 'cm', label: '立方米' },  
          { value: 'ckm', label: '立方千米' }
        ],
        "weight": [
          { value: 'g', label: '克' },  
          { value: 'kg', label: '千克' },  
          { value: 'j', label: '斤' },  
          { value: 'gj', label: '公斤' },  
          { value: 't', label: '吨' }
        ],
        "time": [
          { value: 's', label: '秒' },  
          { value: 'm', label: '分' },
          { value: 'h', label: '时' }
        ]
      },
      unitConvert: {
        "length": {
          "m": 1,
          "km": 1000,
        },
        "area": {
          "sm": 1,          
          "skm": 1000000    
        },
        "volume": {
          "cm": 1,          
          "ckm": 1000000000    
        },
        "weight": {
          "g": 1,          
          "kg": 1000,          
          "j": 500,          
          "gj": 1000,          
          "t": 1000000    
        },
        "time": {
          "s": 1,          
          "m": 60,          
          "h": 3600     
        }
      }
    }
  }, 
  // 读取父组件的值，即App.vue中的show
  props: ['show'],

  // 打开对话框后的默认值
  mounted() {  
    this.type = "length"
    this.unitOptions = this.allOptions[this.type] 
    this.beforeUnit = this.unitOptions[0].value
    this.afterUnit = this.unitOptions[0].value
  },
  watch: {  
    // 监听单位类型的变化，更新单位选项
    type(newUnit) {  
      this.unitOptions = this.allOptions[newUnit]
      this.beforeUnit = this.unitOptions[0].value
      this.afterUnit = this.unitOptions[0].value
    }
  },  
  methods: {
    reset() {
      this.beforeNumber = null
      this.afterNumber = null
    },
    convert() {
      // 根据单位类型，先转换为最小单位值
      const minValue = this.beforeNumber * (this.unitConvert[this.type])[this.beforeUnit]
      // 单位转换 
      this.afterNumber = minValue / (this.unitConvert[this.type])[this.afterUnit]
    }
  }
}
</script>
<style scoped>
</style>