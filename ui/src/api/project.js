import request from '@/utils/request'

export function projectCreate(path) {
  return request({
    url: '/project/add',
    method: 'POST',
    data: {
      path,
    }
  })
}

export function projectList() {
  return request({
    url: '/project/list',
    method: 'GET',
  })
}

export function projectDelete(id) {
  return request({
    url: `/project/delete/${id}`,
    method: 'DELETE'
  })
}

export function projectGetTree(id) {
  return request({
    url: `/project/get/tree/${id}`,
    method: 'GET'
  })
}

export function projectGetGitStat(id) {
  return request({
    url: `/project/get/git/stat/${id}`,
    method: 'GET'
  })
}

export function projectGetTodos(id) {
  return request({
    url: `/project/get/todos/${id}`,
    method: 'GET'
  })
}