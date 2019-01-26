<template lang="html">
  <div class='pa-3'>
    <v-divider class='mb-4' />
    <v-combobox
      solo
      chips
      multiple
      label='Filter by authors'
      v-model="selectedAuthors"
      :items="authors">
    </v-combobox>
    <v-expansion-panel v-model="panel" expand class='elevation-0'>
      <v-expansion-panel-content
        v-for="(todo,i) in filteredTodos"
        :key="i"
      >
        <div slot="header" class='body-1 indigo--text text--darken-4 font-weight-bold'>
          {{getAbsPath(todo.abs_path)}} -
          <v-chip color="indigo darken-4" text-color="white" small>
            {{todo.num}}
          </v-chip>
        </div>
        <v-divider/>
        <v-card>
          <v-card-text>
            <v-list class='' three-line>
              <template v-for="(item, index) in todo.todo_items">
                <v-list-tile>
                  <v-list-tile-avatar>
                    <span class="indigo darken-4 white--text px-3 pa-2 mr-2">
                      #{{index+1}}
                    </span>
                  </v-list-tile-avatar>
                  <v-list-tile-content>
                    <v-list-tile-title class='body-1 font-weight-bold' :title='item.text'>
                      {{item.line_num}}: -
                      {{item.text}}
                    </v-list-tile-title>
                    <v-list-tile-sub-title class="caption my-1 font-weight-bold">
                      {{getAuthor(item.author)}}
                    </v-list-tile-sub-title>
                    <v-list-tile-sub-title class="caption font-italic font-weight-medium">
                      {{ item.date | formatDate('MMMM DD, YYYY') }}
                    </v-list-tile-sub-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-divider/>
              </template>
            </v-list>
          </v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </div>
</template>

<script>
export default {
  props: {
    authors: {type: Array, required: true},
    todos: {type: Array, required: true}
  },
  data () {
    return {
      panel: [],
      selectedAuthors: []
    }
  },
  computed: {
    filteredTodos () {
      let _todos = []
      for (let todo of this.todos) {
        let items = todo.todo_items.filter(item => {
          if (this.selectedAuthors.length) {
            return this.selectedAuthors.includes(item.author)
          }
          return true
        })
        if (items.length) {
          _todos.push({
            abs_path: todo.abs_path,
            num: items.length,
            todo_items: items
          })
        }
      }
      return _todos
    }
  },
  methods: {
    getAuthor (author) {
      if (author) {
        return author
      }
      return 'None'
    },
    getAbsPath (path) {
      return path.slice(28)
    }
  }
}
</script>

<style lang="css">
</style>
