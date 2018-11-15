<template>
  <div>
    <v-navigation-drawer clipped app permanent floating width='450' class='grey'>
      <v-list two-line class='mx-4'>
        <v-btn color='accent' block class='my-3'>
          Git stats
          <v-icon right>open_in_new</v-icon>
        </v-btn>
        <v-btn color='accent darken-1' block class='my-3'>
          Manage
          <v-icon right>pan_tool</v-icon>
        </v-btn>
      </v-list>
      
      <v-divider/>
      <v-treeview
        v-model="tree"
        class='green lighten-3 label-big py-4 px-3'
        :active.sync="active"
        :open.sync="open"
        :items="items"
        activatable
        item-key="name"
        open-on-click
        hoverable
      >
        <template slot="prepend" slot-scope="{ item, open, leaf }">
          <v-icon v-if="!item.file">
            {{ open ? 'mdi-folder-open' : 'mdi-folder' }}
          </v-icon>
          <v-icon v-else>
            {{ files[item.file] }}
          </v-icon>
        </template>
        <template slot='append' slot-scope="{ item, open, leaf }">
          <span class='title font-italic grey--text'>TODOs: 10</span>
        </template>
      </v-treeview>
    </v-navigation-drawer>
    <v-flex xs12 md6>
      <v-card-text>
        <div class="title font-weight-medium grey--text pa-3 text-xs-center">
          Select a file
        </div>
      </v-card-text>
    </v-flex>
  </div>
</template>

<script>
  export default {
    data: () => ({
      open: ['src'],
      active: [],
      files: {
        html: 'mdi-language-html5',
        js: 'mdi-nodejs',
        json: 'mdi-json',
        md: 'mdi-markdown',
        pdf: 'mdi-file-pdf',
        png: 'mdi-file-image',
        txt: 'mdi-file-document-outline',
        xls: 'mdi-file-excel'
      },
      tree: [],
      items: [
        {
          name: '.git'
        },
        {
          name: 'node_modules'
        },
        {
          name: 'src',
          children: [
            {
              name: 'static',
              children: [{
                name: 'logo.png',
                file: 'png'
              }]
            },
            {
              name: 'favicon.ico',
              file: 'png'
            },
            {
              name: 'index.html',
              file: 'html'
            }
          ]
        },
        {
          name: '.gitignore',
          file: 'txt'
        },
        {
          name: 'babel.config.js',
          file: 'js'
        },
        {
          name: 'package.json',
          file: 'json'
        },
        {
          name: 'README.md',
          file: 'md'
        },
        {
          name: 'vue.config.js',
          file: 'js'
        },
        {
          name: 'yarn.lock',
          file: 'txt'
        }
      ]
    })
  }
</script>

<style>
.label-big * {
  font-size: 2rem;
}
</style>
