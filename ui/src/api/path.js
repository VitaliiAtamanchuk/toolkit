import request from '@/utils/request'

export const pathExplore = path => request({
  url: '/path/explore',
  method: 'POST',
  data: {path}
})
