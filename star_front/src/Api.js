// import Vue  from 'vue';  
import axios from 'axios';  
  
axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default {  
  getToolList () {
    return ajax('/toolList', 'get')
  },
  getExchangeRate (from_currency, to_currency) {
    const api_url = 'https://www.alphavantage.co/query'
    return ajax(api_url, 'get', {
      function: "CURRENCY_EXCHANGE_RATE",
      from_currency,
      to_currency,
      apikey: "CXM65ESPPCN8HRMP"
    })
  },
  getNetworks () {
    return ajax('/wifi', 'get', {})
  }
}

function ajax(url, method, params = {}) {
  return new Promise((resolve, reject) => {
    axios({
      url,
      method,
      params
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