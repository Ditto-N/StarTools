<template>
  <div v-if="show">
    <el-dialog
      model-value="true"
      title="单位转换器"
      width="500"
      @close="$emit('close')"
      draggable
    >
      <span>This is a message</span>
    </el-dialog>
  </div>
</template>
<script>
export default {
  props: ['show'] 
}
</script>