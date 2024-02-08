<template>
  <el-container>
    <el-header>StartTool</el-header>
    <el-main>
      <div class="tool-box">
        <el-button id="tool-button"><font-awesome-icon :icon="['fas', 'recycle']" size="3x"/></el-button>
        <p style="color:#b8b6c1;">单位转换器</p>
      </div>

      <!-- <div class="tool-box" v-for="tool in toolList" :key="tool.id">
        <el-button :icon="tool.icon" />
        <div>{{ tool.title }}</div>
      </div> -->
    </el-main>
  </el-container>
</template>

<script>
// import Api from './Api'
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data() {
    return {
      toolList: []
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

.fa-recycle {
  color: #977d9a;
}

.fa-recycle:hover {
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
