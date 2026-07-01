import axios from 'axios'

// In production, VITE_API_URL is set to the deployed backend URL (e.g. https://your-app.onrender.com)
// In development, it defaults to '' and the Vite dev server proxies /api to localhost:8000
const API_BASE = (import.meta.env.VITE_API_URL || '') + '/api/v1'

const apiClient = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
})

apiClient.interceptors.response.use(
  (res) => res,
  (err) => {
    const message = err.response?.data?.detail || err.message || 'Something went wrong'
    return Promise.reject(new Error(message))
  },
)

export default apiClient