import Vue from 'vue'
import axios from 'axios'
import router from "@/router"

​Vue.prototype.axios = axios
axios.defaults.baseURL = 'http://0.0.0.0:8000'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

// 封装ajax函数，统一处理
function ajax (url, method, options, showMessage = true) {
    if (options !== undefined) {
      var { params = {}, data = {} } = optionsx
    } else {
      params = data = {}
    }
  
    return new Promise((resolve, reject) => {
      axios({
        url,
        method,
        params,
        data
      }).then(
        res => {
          // API 正常返回(status=20x), 是否错误通过有无 error 判断
          if (res.data.error !== null && res.data.data !== null) {
            // Vue.prototype.$error(res.data.data)
            reject(res)
            // 若后端返回未登录，则 session 失效，应退出当前登录用户
            if (res.data.data.startsWith('Please login')) {
              router.push({ name: 'login' })
            }
          } else {
            resolve(res)
            if (method !== 'get' && showMessage === true) {
              // Vue.prototype.$success("Succeeded")
            }
          }
        },
        res => {
          // API 请求异常，一般为 Server error 或 network error
          reject(res)
          Vue.prototype.$error(res.data.data)
        }
      )
    })
  }

  // 编写前后端接口
  export default {
    getToolList () {
      return ajax('toolList', 'get')
    }
  }