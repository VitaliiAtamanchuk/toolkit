<template>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      dark: false,
    }
  }
}
</script>

<style lang='scss'>
  .drag-handler {
    cursor: grab;
  }
</style>
