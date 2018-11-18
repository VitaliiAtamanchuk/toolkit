import axios from 'axios'

// create an axios instance
const service = axios.create({
  baseURL: 'http://localhost:8000', // api base_url
  timeout: 100000 // request timeout
})

// request interceptor
// service.interceptors.request.use(
//   config => {
//   },
//   error => {
//     // Do something with request error
//     console.log(error) // for debug
//     Promise.reject(error)
//   }
// )

// // response interceptor
// service.interceptors.response.use(
//   response => response,
//   error => {
//     console.log('err' + error) // for debug
//     return Promise.reject(error)
//   }
// )

export default service