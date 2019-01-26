<template>
  <v-container>
    <v-layout row wrap>
      <v-flex xs5 md3 class='mr-3'>
        <v-card :to="{name: 'projects'}" class='pa-3'>
          <v-responsive>
            <v-layout justify-center>
              <v-avatar color="indigo">
                <v-icon dark>book</v-icon>
              </v-avatar>
            </v-layout>
          </v-responsive>
          <v-card-title class='text-xs-center'>
            <v-layout justify-center>
              <span class='body-2 font-weight-medium'>Projects</span>
            </v-layout>
          </v-card-title>
            <v-divider />
          <v-card-text>
            <v-layout justify-center>
              <span class='caption'>Manage, check stats, predict commit message, analyze project.</span>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs5 md3 class='mr-3'>
        <v-card :to="{name: 'postgres'}" class='pa-3'>
          <v-responsive>
            <v-layout justify-center>
              <v-avatar color="pink">
                <v-icon dark>history</v-icon>
              </v-avatar>
            </v-layout>
          </v-responsive>
          <v-card-title class='text-xs-center'>
            <v-layout justify-center>
              <span class='body-2 font-weight-medium'>Postgres</span>
            </v-layout>
          </v-card-title>
            <v-divider />
          <v-card-text>
            <v-layout justify-center>
              <span class='caption'>View csvlogs.</span>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
  }
</script>
