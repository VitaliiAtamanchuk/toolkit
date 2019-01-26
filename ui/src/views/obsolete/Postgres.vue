<template lang="html">
  <v-container>
    <h1>Enter path to postgres CSV logs</h1>
    <PathInput :path.sync='path' />
  </v-container>
</template>

<script>
export default {
  data () {
    return {
      path: ''
    }
  }
}
</script>

<style lang="css">
</style>
