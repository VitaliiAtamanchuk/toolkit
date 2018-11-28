<template lang="html">
  <div>
    <v-flex xs12>
      <v-btn color='red lighten-2' dark :loading='isLoading'>
        Show props names
      </v-btn>
      <v-btn color='blue darken-4' dark :loading='isLoading'>
        Fix props names
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
