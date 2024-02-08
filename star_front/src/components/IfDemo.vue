<template>
    <h3>条件渲染</h3>
    <div v-if="flag">Can you see me?</div>
</template>

<script>
export default {
    data(){
        return {
            flag:true
        }
    }
}
</script>