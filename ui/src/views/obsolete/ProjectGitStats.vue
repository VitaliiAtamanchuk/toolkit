<template>
  <div>
    <v-layout row wrap>
      <v-combobox solo label='Select authors' chips />
      <v-select solo label='Group by date range' chips
        :items='dateRanges' v-model='dateRangeSelected'/>
      <v-select solo label="Type of values" chips
        :items='valTypes' v-model='valTypeSelected'/>
    </v-layout>
    <d3-bar-chart
    app-name="GIT Stats"
    :d3-data="d3Data"/>
  </div>
</template>

<script>
import D3BarChart from '@/components/D3BarChart'
import moment from 'moment'
import {projectGetGitStat} from '@/api/project'

export default {
  props: ['id'],
  components: {'d3-bar-chart': D3BarChart},
  data () {
    return {
      valTypes: ['lines', 'insertions', 'deletions'],
      valTypeSelected: 'lines',
      dateRanges: ['None', 'Day', 'Week', 'Month', 'Year'],
      dateRangeSelected: 'None',
      options: {},
      stats: [],
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    getDate (date) {
      let dateGroup = null
      if (this.dateRangeSelected == 'Day') {
        dateGroup = date.substr(0, 10)
      } else if (this.dateRangeSelected == 'Week') {
        dateGroup = moment(date).year()+'-'+moment(date).week()
      } else if (this.dateRangeSelected == 'Month') {
        const month = parseInt(moment(date).month()) + 1
        dateGroup = moment(date).year()+'-'+month.toString()
      } else if (this.dateRangeSelected == 'Year') {
        dateGroup = moment(date).year()
      } else {
        dateGroup = date
      }
      return dateGroup
    },
    fetchData () {
      projectGetGitStat(this.id).then(resp => {
        this.stats = resp.data.stats
      })
    },
    formatTooltipData (date, value) {
      return `<div>${value} ${this.valTypeSelected}</div><div>${date}</div>`
    }
  },
  computed: {
    d3Data () {
      let d3DataX = []
      let d3DataY = []
      let d3Tooltip = []
      console.log('-----------------------------')
      console.log(this.stats)
      let items = this.stats.reduce( (acc, item) => {
        const date = item['date']
        const value = item[this.valTypeSelected]
        let dateGroup = this.getDate(date)
        if (typeof acc[dateGroup] === 'undefined') {
          acc[dateGroup] = 0
        }
        acc[dateGroup] += value
        return acc
      }, {});
      for (let i in items) {
        let date = i
        let value = items[i]
        d3DataX.unshift(date)
        d3DataY.unshift(value)
        d3Tooltip.unshift(this.formatTooltipData(date, value))
      }
      return {
        x: d3DataX,
        y: d3DataY,
        tooltip: d3Tooltip
      }
    }
  }
}
</script>
