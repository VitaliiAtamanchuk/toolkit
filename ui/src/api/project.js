import request from '@/utils/request'

export const projectCreate = path => request({
  url: '/project/add',
  method: 'POST',
  data: {path}
})

export const projectList = () => request({
  url: '/project/list',
  method: 'GET',
})

export const projectDelete = id => request({
  url: `/project/delete/${id}`,
  method: 'DELETE'
})

export const projectGetTree = id => request({
  url: `/project/get/tree/${id}`,
  method: 'GET'
})

export const projectGetGitStat = id => request({
  url: `/project/get/git/stat/${id}`,
  method: 'GET'
})

export const projectGetTodos = id => request({
  url: `/project/get/todos/${id}`,
  method: 'GET'
})
