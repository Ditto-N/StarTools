// import Vue  from 'vue';  
import axios from 'axios';  
  
axios.defaults.baseURL = 'http://47.109.85.237:8000'

export default {  
  getToolList () {
    return ajax('/toolList', 'get')
  }
}

function ajax(url, method) {
  return new Promise((resolve, reject) => {
    axios({
      url,
      method
    }).then(
      res => {
        if (res.data.error !== null && res.data.data !== null) {
          resolve(res)
        } else {
          reject(res)
        }
      }
    )
  })
}