import request from '@/utils/request'

export const pyIsortDiff = path => request({
  url: '/code-analysis/py-isort-diff',
  method: 'POST',
  data: {path}
})

export const pyIsortFix = path => request({
  url: '/code-analysis/py-isort-fix',
  method: 'POST',
  data: {path}
})

export const pyMcCabe = (path, complexity) => request({
  url: '/code-analysis/py-mccabe',
  method: 'POST',
  data: {path, complexity}
})

export const getFileTodos = (projectId, path) => request({
  url: '/code-analysis/get-file-todos',
  method: 'POST',
  data: {project_id: projectId, path}
})


export const getVueFileHierarchy = (projectId, path) => request({
  url: '/code-analysis/get-vue-file-hierarchy',
  method: 'POST',
  data: {project_id: projectId, path}
})
