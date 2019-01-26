<template>
  <div>
    <v-btn color='blue' dark @click='fetchData()'>
      Refresh TODOs List <v-icon right>refresh</v-icon>
    </v-btn>
    <div class="d-flex justify-between align-center mb-3">
      <v-btn @click="openAllExpPanels">Open All</v-btn>
      <v-btn @click="closeAllExpPanels">Close All</v-btn>
    </div>
    <v-combobox
      solo
      chips
      multiple
      label='Filter by authors'
      v-model="selectedAuthors"
      :items="authors">
    </v-combobox>
    <v-expansion-panel
      v-model="panel"
      expand
    >
      <v-expansion-panel-content
        v-for="(todo,i) in filteredTodos"
        :key="i"
        class='indigo lighten-3'
      >
        <div slot="header" class='subheading'>{{todo.abs_path}} - <span class='red--text'>{{todo.num}}</span></div>
        <v-divider/>
        <v-card>
          <v-card-text>
            <v-list class='elevation-3' three-line>
              <template v-for="(item, index) in todo.todo_items">
                <v-list-tile>
                  <v-list-tile-content>
                    <v-list-tile-title class='title'>
                      {{item.line_num}}: -
                      {{item.text}}
                    </v-list-tile-title>
                    <v-list-tile-sub-title class="subheading my-1">
                      {{getAuthor(item.author)}}
                    </v-list-tile-sub-title>
                    <v-list-tile-sub-title>
                      {{ item.date }}
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
// TODO: fixed section with "Open all" & "Close all" btns
// TODO: better designed chips at author selects
import {projectGetTodos} from '@/api/project'

export default {
  props: ['id'],
  data () {
    return {
      panel: [],
      todos: [],
      selectedAuthors: [],
      authors: []
    }
  },
  created () {
    this.fetchData()
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
    fetchData () {
      projectGetTodos(this.id).then(resp => {
        this.todos = resp.data.todos
        this.authors = resp.data.authors
      })
    },
    openAllExpPanels () {
      this.panel = [...Array(this.todos.length).keys()].map(_ => true)
    },
    closeAllExpPanels () {
      this.panel = []
    },
    getAuthor (author) {
      if (author) {
        return author
      }
      return 'None'
    }
  }
}
</script>
