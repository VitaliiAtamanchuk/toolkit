import request from '@/utils/request'

export function pathExplore(path) {
  return request({
    url: '/path/explore',
    method: 'POST',
    data: {
      path,
    }
  })
}