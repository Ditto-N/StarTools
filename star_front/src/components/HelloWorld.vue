<template>
  <!-- <div v-bind:id="dynamicId" v-bind:class="dynamicClass" v-bind:title="dynamicTitle">测试</div>
  </template>
  
  <script>
  export default {
    data(){
      return{
        dynamicClass:"appclass",
        dynamicId:"appid",
        dynamicTitle:"yoyo"
      }
    }
  }
  </script> -->

  <div class="hello">
    {{ toolList }}
    <el-button type="warning">Warning</el-button>
  </div>
</template>

<script>
import Api from '../Api'
export default {
  name: 'HelloWorld',
  data() {
    return {
      toolList: []
    }
  },
  // 网页初始化
  async mounted() {
    const res = await Api.getToolList()
    this.toolList = res.data.toolList
    console.log(res.data)
  }
  // methods: {
  //   async init() {
  //     const res = await Api.getToolList()
  //     this.toolList = res.data.toolList
  //     console.log(res);
  //   }
  // }
}
</script>

<style>
.appclass{
  color:red;
  font-size: 30px;
}
</style>