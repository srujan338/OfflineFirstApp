import apiClient from '@/api/client'
import type { ApiResponse, Invoice, ProcessedInvoice, ExpenditureSummary, RunMetrics } from '@/types'

export const invoicesApi = {
  list: (limit = 50, offset = 0) =>
    apiClient.get<ApiResponse<Invoice[]>>('/invoices/', { params: { limit, offset } }),

  getById: (id: number) =>
    apiClient.get<ApiResponse<Invoice>>(`/invoices/${id}`),

  process: (file: File) => {
    const fd = new FormData()
    fd.append('file', file)
    return apiClient.post<ProcessedInvoice>('/invoices/process', fd, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
  },

  updateCategory: (id: number, category: string) =>
    apiClient.put<ApiResponse<null>>(`/invoices/${id}/category`, null, { params: { category } }),
}

export const analyticsApi = {
  expenditure: () =>
    apiClient.get<ApiResponse<ExpenditureSummary>>('/analytics/expenditure'),
}

export const runsApi = {
  list: () =>
    apiClient.get<ApiResponse<RunMetrics[]>>('/runs/'),
}
