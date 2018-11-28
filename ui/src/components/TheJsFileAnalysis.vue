<template lang="html">
  <div>
    <v-flex xs12>
      <v-btn color='red lighten-2' dark :loading='isLoading'>
        TODO:
      </v-btn>
    </v-flex>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isLoading: false,
    }
  }
}
</script>

<style lang="css">
</style>
