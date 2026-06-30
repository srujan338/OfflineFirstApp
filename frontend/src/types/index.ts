export interface LineItem {
  id?: number
  invoice_id?: number
  description: string
  quantity: number
  price: number
  total: number
}

export interface Invoice {
  id: number
  vendor: string
  invoice_number: string
  date: string
  subtotal: number
  tax: number
  total: number
  currency: string
  category: string
  image_path: string | null
  created_at: string | null
  line_items?: LineItem[]
}

export interface ApiResponse<T> {
  success: boolean
  data: T
  message?: string
}

export interface ExpenditureSummary {
  [category: string]: number
}

export interface RunMetrics {
  id: number
  invoice_id: number | null
  ocr_time: number
  parse_time: number
  total_time: number
  memory_usage: number
  created_at: string
}

export interface ProcessedInvoice {
  invoice_id: number
  vendor: string
  invoice_number: string
  date: string
  subtotal: number
  tax: number
  total: number
  currency: string
  category: string
  line_items: LineItem[]
  image_path: string
}

export type ProcessingStatus = 'idle' | 'uploading' | 'processing' | 'completed' | 'failed'
