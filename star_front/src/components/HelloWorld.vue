<template>
  <div v-bind:id="dynamicId" v-bind:class="dynamicClass" v-bind:title="dynamicTitle">测试</div>
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
  </script>

<style>
.appclass{
  color:red;
  font-size: 30px;
}
</style>