<template lang="html">
  <div class='pa-3'>
    <v-divider class='mb-5' />
    <v-layout row wrap class='mb-4'>
      <v-btn-toggle v-model="dateRangeSelected" class='indigo lighten-1' dark>
        <v-btn flat value="Day">
          Day
        </v-btn>
        <v-btn flat value="Week">
          Week
        </v-btn>
        <v-btn flat value="Month">
          Month
        </v-btn>
        <v-btn flat value="Year">
          Year
        </v-btn>
      </v-btn-toggle>
      <v-btn-toggle v-model="chartTypeSelected" class='ml-5 indigo lighten-1' dark>
        <v-btn flat value="line">
          line
        </v-btn>
        <v-btn flat value="area">
          area
        </v-btn>
        <v-btn flat value="bar">
          bar
        </v-btn>
      </v-btn-toggle>

      <v-btn-toggle v-model="valTypeSelected" class='ml-5 indigo lighten-1' dark multiple>
        <v-btn flat value="lines">
          lines
        </v-btn>
        <v-btn flat value="insertions">
          insertions
        </v-btn>
        <v-btn flat value="deletions">
          deletions
        </v-btn>
      </v-btn-toggle>
    </v-layout>
    <v-card class='px-4 py-3'>
      <apexcharts width="650" :type="chartTypeSelected"
        :options="chartOptions" :series="series" />
    </v-card>
  </div>
</template>

<script>
import moment from 'moment'
import VueApexCharts from 'vue-apexcharts'
import _ from 'lodash'

export default {
  components: {
    apexcharts: VueApexCharts,
  },
  props: {
    stats: {type: Array, required: true}
  },
  data () {
    return {
      chartTypeSelected: 'area',
      chartOptions: {
        colors: ['#008FFB', '#D84315', '#81C784', '#ffc247'],
        grid: {
          show:false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Git statistics chart',
          align: 'left'
        },
        xaxis: {
          type: 'datetime',
        },
        yaxis: {
          opposite: true
        },
        tooltip: {
          x: {
            format: 'dd MMMM yyyy'
          },
        }
      },
      valTypeSelected: ['lines'],
      dateRangeSelected: 'Month'
    }
  },
  computed: {
    series () {
      const lines = []
      const insertions = []
      const deletions = []
      const labels = []
      const index = []
      let items = this.stats.reduce( (acc, item) => {
        const date = item['date']
        let {dateGroup, startDate} = this.getDate(date)
        if (typeof acc[dateGroup] === 'undefined') {
          acc[dateGroup] = {
            files: 0,
            lines: 0,
            insertions: 0,
            deletions: 0,
            startDate: startDate
          }
        }
        acc[dateGroup].files += item['files']
        acc[dateGroup].lines += item['lines']
        acc[dateGroup].insertions += item['insertions']
        acc[dateGroup].deletions += item['deletions']
        return acc
      }, {})
      console.log('------------------------')
      for (let i in items) {
        console.log(items[i])
        index.unshift(+(100000 * items[i].files / items[i].lines).toFixed(0))
        labels.unshift(items[i].startDate)
        lines.unshift(items[i].lines)
        insertions.unshift(items[i].insertions)
        deletions.unshift(items[i].deletions)
      }

      this.chartOptions.labels = labels
      this.chartOptions = _.cloneDeep(this.chartOptions)

      const retVal = []
      if (this.valTypeSelected.indexOf('lines') > -1) {
        retVal.push({
          name: "lines",
          data: lines
        })
      }
      retVal.push({
        name: "index (files/lines)",
        data: index
      })
      if (this.valTypeSelected.indexOf('insertions') > -1) {
        retVal.push({
          name: "insertions",
          data: insertions
        })
      }
      if (this.valTypeSelected.indexOf('deletions') > -1) {
        retVal.push({
          name: "deletions",
          data: deletions
        })
      }
      return retVal
    }
  },
  methods: {
    getDate (date) {
      let dateGroup = null
      let startDate = null
      if (this.dateRangeSelected == 'Day') {
        dateGroup = date.substr(0, 10)
        startDate = dateGroup
      } else if (this.dateRangeSelected == 'Week') {
        dateGroup = moment(date).year()+'-'+moment(date).week()
        startDate = moment(date).startOf('week').format('YYYY-MM-DD hh:mm')
      } else if (this.dateRangeSelected == 'Month') {
        const month = parseInt(moment(date).month()) + 1
        dateGroup = moment(date).year() + '-' + month.toString()
        startDate = dateGroup + '-01'
      } else if (this.dateRangeSelected == 'Year') {
        dateGroup = moment(date).year()
        startDate = dateGroup + '-01' + '-01'
      }
      return {dateGroup, startDate}
    }
  }
}
</script>

<style lang="css">
</style>
