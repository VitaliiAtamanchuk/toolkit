  <v-layout wrap row>
    <v-flex xs12>
      <v-parallax height="250" :src="require('@/assets/black_img.jpg')">
        <span class='text-xs-center display-1'>Wyszukiwarka ofert</span>
      </v-parallax>
      <v-text-field
        solo
        label="Jakiej oferty szukasz?"
        append-icon="search"
        autofocus
        clearable />
    </v-flex>
    <v-flex xs3 offset-xs1 class='pr-5'>
      {{data}}
      <v-breadcrumbs>
        <v-icon slot="divider">chevron_right</v-icon>
        <v-breadcrumbs-item
          v-for="item in breadcrumbs"
          :to="item.to"
          :disabled="item.disabled"
          :key="item.text"
        >
          {{ item.text }}
        </v-breadcrumbs-item>
      </v-breadcrumbs>
      <TheFilters />
    </v-flex>
    <v-flex xs7 class='px-2 mt-2'>
      <TheMain asdSds='as' />
    </v-flex>
  </v-layout>
