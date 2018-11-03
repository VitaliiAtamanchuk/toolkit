import TheFilters from '@/components/offer_search/TheFilters'
import TheMain from '@/components/offer_search/TheMain'

export default {
  components: {
    TheFilters,
    TheMain,
  },
  data () {
    return {
      data: [],
      breadcrumbs: [
        {text: 'Storona główna', disabled: false, to: {name: 'home'}},
        {text: 'Wyszukiwarka oferty', disabled: true},
      ]
    }
  }
}
